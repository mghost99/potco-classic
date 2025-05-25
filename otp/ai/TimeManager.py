from pandac.PandaModules import *
from direct.showbase.DirectObject import *
from direct.distributed.ClockDelta import *
from direct.task import Task
from direct.distributed import DistributedObject
from direct.directnotify import DirectNotifyGlobal
from otp.otpbase import OTPGlobals
from libotp import CFSpeech
from libotp import CFTimeout
from direct.showbase import PythonUtil
import time
import os

class TimeManager(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('TimeManager')
    neverDisable = 1

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.updateFreq = base.config.GetFloat('time-manager-freq', 1800)
        self.minWait = base.config.GetFloat('time-manager-min-wait', 10)
        self.maxUncertainty = base.config.GetFloat('time-manager-max-uncertainty', 1)
        self.maxAttempts = base.config.GetInt('time-manager-max-attempts', 5)
        self.extraSkew = base.config.GetInt('time-manager-extra-skew', 0)
        if self.extraSkew != 0:
            self.notify.info('Simulating clock skew of %0.3f s' % self.extraSkew)

        self.reportFrameRateInterval = base.config.GetDouble('report-frame-rate-interval', 300.0)
        self.talkResult = 0
        self.thisContext = -1
        self.nextContext = 0
        self.attemptCount = 0
        self.start = 0
        self.lastAttempt = -self.minWait
        self.setFrameRateInterval(self.reportFrameRateInterval)

    def generate(self):
        if self.cr.timeManager != None:
            self.cr.timeManager.delete()

        self.cr.timeManager = self
        DistributedObject.DistributedObject.generate(self)
        self.accept(OTPGlobals.SynchronizeHotkey, self.handleHotkey)
        self.accept('clock_error', self.handleClockError)
        if self.updateFreq > 0:
            self.startTask()

    def disable(self):
        self.ignore(OTPGlobals.SynchronizeHotkey)
        self.ignore('clock_error')
        self.stopTask()
        taskMgr.remove('frameRateMonitor')
        if self.cr.timeManager == self:
            self.cr.timeManager = None

        DistributedObject.DistributedObject.disable(self)

    def delete(self):
        self.ignore(OTPGlobals.SynchronizeHotkey)
        self.ignore('clock_error')
        self.stopTask()
        taskMgr.remove('frameRateMonitor')
        if self.cr.timeManager == self:
            self.cr.timeManager = None

        DistributedObject.DistributedObject.delete(self)

    def startTask(self):
        self.stopTask()
        taskMgr.doMethodLater(self.updateFreq, self.doUpdate, 'timeMgrTask')

    def stopTask(self):
        taskMgr.remove('timeMgrTask')

    def doUpdate(self, task):
        self.synchronize('timer')
        taskMgr.doMethodLater(self.updateFreq, self.doUpdate, 'timeMgrTask')
        return Task.done

    def handleHotkey(self):
        self.lastAttempt = -self.minWait
        if self.synchronize('user hotkey'):
            self.talkResult = 1
        else:
            base.localAvatar.setChatAbsolute('Too soon.', CFSpeech | CFTimeout)

    def handleClockError(self):
        self.synchronize('clock error')

    def synchronize(self, description):
        now = globalClock.getRealTime()
        if now - self.lastAttempt < self.minWait:
            self.notify.debug('Not resyncing (too soon): %s' % description)
            return 0

        self.talkResult = 0
        self.thisContext = self.nextContext
        self.attemptCount = 0
        self.nextContext = self.nextContext + 1 & 255
        self.notify.info('Clock sync: %s' % description)
        self.start = now
        self.lastAttempt = now
        self.sendUpdate('requestServerTime', [self.thisContext])
        return 1

    def serverTime(self, context, timestamp, timeOfDay):
        end = globalClock.getRealTime()
        aiTimeSkew = timeOfDay - self.cr.getServerTimeOfDay()
        if context != self.thisContext:
            self.notify.info('Ignoring TimeManager response for old context %d' % context)
            return

        elapsed = end - self.start
        self.attemptCount += 1
        self.notify.info('Clock sync roundtrip took %0.3f ms' % (elapsed * 1000.0))
        self.notify.info('AI time delta is %s from server delta' % PythonUtil.formatElapsedSeconds(aiTimeSkew))
        average = (self.start + end) / 2.0 - self.extraSkew
        uncertainty = (end - self.start) / 2.0 + abs(self.extraSkew)
        globalClockDelta.resynchronize(average, timestamp, uncertainty)
        self.notify.info('Local clock uncertainty +/- %.3f s' % globalClockDelta.getUncertainty())
        if globalClockDelta.getUncertainty() > self.maxUncertainty:
            if self.attemptCount < self.maxAttempts:
                self.notify.info('Uncertainty is too high, trying again.')
                self.start = globalClock.getRealTime()
                self.sendUpdate('requestServerTime', [self.thisContext])
                return

            self.notify.info('Giving up on uncertainty requirement.')

        if self.talkResult:
            base.localAvatar.setChatAbsolute('latency %0.0f ms, sync \xc2\xb1%0.0f ms' % (elapsed * 1000.0, globalClockDelta.getUncertainty() * 1000.0), CFSpeech | CFTimeout)

        messenger.send('gotTimeSync')

    def setDisconnectReason(self, disconnectCode):
        self.notify.info('Client disconnect reason %s.' % disconnectCode)
        self.sendUpdate('setDisconnectReason', [
            disconnectCode])

    def setExceptionInfo(self):
        info = PythonUtil.describeException()
        self.notify.info('Client exception: %s' % info)
        self.sendUpdate('setExceptionInfo', [
            info])
        self.cr.flush()

    def d_setSignature(self, signature, hash, pyc):
        self.sendUpdate('setSignature', [
            signature,
            hash,
            pyc])

    def setFrameRateInterval(self, frameRateInterval):
        if frameRateInterval == 0:
            return

        if not base.frameRateMeter:
            maxFrameRateInterval = base.config.GetDouble('max-frame-rate-interval', 30.0)
            globalClock.setAverageFrameRateInterval(min(frameRateInterval, maxFrameRateInterval))

        taskMgr.remove('frameRateMonitor')
        task = taskMgr.add(self.frameRateMonitor, 'frameRateMonitor')
        task.delayTime = frameRateInterval

    def frameRateMonitor(self, task):
        from otp.avatar.Avatar import Avatar
        vendorId = 0
        deviceId = 0
        processMemory = 0
        pageFileUsage = 0
        physicalMemory = 0
        pageFaultCount = 0
        osInfo = (os.name, 0, 0, 0)
        cpuSpeed = (0, 0)
        if getattr(base, 'pipe', None):
            di = base.pipe.getDisplayInformation()
            if di.getDisplayState() == DisplayInformation.DSSuccess:
                vendorId = di.getVendorId()
                deviceId = di.getDeviceId()

            di.updateMemoryInformation()
            oomb = 1.0 / (1024.0 * 1024.0)
            processMemory = di.getProcessMemory() * oomb
            pageFileUsage = di.getPageFileUsage() * oomb
            physicalMemory = di.getPhysicalMemory() * oomb
            pageFaultCount = di.getPageFaultCount() / 1000.0
            osInfo = (os.name, di.getOsPlatformId(), di.getOsVersionMajor(), di.getOsVersionMinor())
            di.updateCpuFrequency(0)
            ooghz = 1e-09
            cpuSpeed = (di.getMaximumCpuFrequency() * ooghz, di.getCurrentCpuFrequency() * ooghz)

        self.d_setFrameRate(globalClock.getAverageFrameRate(), globalClock.calcFrameRateDeviation(), len(Avatar.ActiveAvatars), base.locationCode or '', time.time() - base.locationCodeChanged, globalClock.getRealTime(), base.gameOptionsCode, vendorId, deviceId, processMemory, pageFileUsage, physicalMemory, pageFaultCount, osInfo, cpuSpeed)
        return task.again

    def d_setFrameRate(self, fps, deviation, numAvs, locationCode, timeInLocation, timeInGame, gameOptionsCode, vendorId, deviceId, processMemory, pageFileUsage, physicalMemory, pageFaultCount, osInfo, cpuSpeed):
        info = '%0.1f fps|%0.3fd|%s avs|%s|%d|%d|%s|0x%04x|0x%04x|%0.1fMB|%0.1fMB|%0.1fMB|%d|%s|%s' % (fps, deviation, numAvs, locationCode, timeInLocation, timeInGame, gameOptionsCode, vendorId, deviceId, processMemory, pageFileUsage, physicalMemory, pageFaultCount, '%s.%d.%d.%d' % osInfo, '%0.03f,%0.03f' % cpuSpeed)
        print('frame rate: %s' % info)
        # TODO
        '''self.sendUpdate('setFrameRate', [
            fps,
            deviation,
            numAvs,
            locationCode,
            timeInLocation,
            timeInGame,
            gameOptionsCode,
            vendorId,
            deviceId,
            processMemory,
            pageFileUsage,
            physicalMemory,
            pageFaultCount,
            osInfo,
            cpuSpeed])'''
