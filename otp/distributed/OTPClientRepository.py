import sys
import time
import string
import types
import random
import gc
import os
from pandac.PandaModules import *
from pandac.PandaModules import *
from direct.gui.DirectGui import *
from otp.distributed.OtpDoGlobals import *
from direct.interval.IntervalGlobal import ivalMgr
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.ClientRepositoryBase import ClientRepositoryBase
from direct.fsm.ClassicFSM import ClassicFSM
from direct.fsm.State import State
from direct.task import Task
from direct.distributed import DistributedSmoothNode
from direct.showbase import PythonUtil, GarbageReport, BulletinBoardWatcher
from direct.showbase.ContainerLeakDetector import ContainerLeakDetector
from direct.showbase import MessengerLeakDetector
from direct.showbase.GarbageReportScheduler import GarbageReportScheduler
from direct.showbase import LeakDetectors
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator
from otp.avatar import Avatar
from otp.avatar.DistributedPlayer import DistributedPlayer
from otp.login import TTAccount
from otp.login import AccountServerConstants
from otp.login.CreateAccountScreen import CreateAccountScreen
from otp.login import LoginScreen
from otp.otpgui import OTPDialog
from otp.avatar import DistributedAvatar
from otp.otpbase import OTPLocalizer
from otp.login import LoginGSAccount
from otp.login import LoginGoAccount
from otp.login.LoginWebPlayTokenAccount import LoginWebPlayTokenAccount
from otp.login.LoginDISLTokenAccount import LoginDISLTokenAccount
from otp.login import LoginTTAccount
from otp.login import HTTPUtil
from otp.otpbase import OTPGlobals
from otp.otpbase import OTPLauncherGlobals
from otp.uberdog import OtpAvatarManager
from otp.distributed import OtpDoGlobals
from .PotentialAvatar import PotentialAvatar
import enum

class OTPClientRepository(ClientRepositoryBase):
    notify = directNotify.newCategory('OTPClientRepository')
    notify.setDebug(True)
    avatarLimit = 6
    class WishNameResult(enum.Enum):
        Failure = 1
        PendingApproval = 2
        Approved = 3
        Rejected = 4

    def __init__(self, serverVersion, launcher = None, playGame = None):
        ClientRepositoryBase.__init__(self)
        self.handler = None
        self.launcher = launcher
        base.launcher = launcher
        self.__currentAvId = 0
        self.productName = config.GetString('product-name', 'DisneyOnline-US')
        self.createAvatarClass = None
        self.systemMessageSfx = None
        if self.productName == 'DisneyOnline-US':
            if self.launcher and self.launcher.isDummy():
                if self.launcher.getDeployment() == 'UK':
                    self.productName = 'DisneyOnline-UK'

                if self.launcher.getDeployment() == 'AP':
                    self.productName = 'DisneyOnline-AP'

            elif self.launcher and not self.launcher.isDummy():
                if self.launcher.getRegistry('DEPLOYMENT') == 'UK':
                    self.productName = 'DisneyOnline-UK'

                if self.launcher.getRegistry('DEPLOYMENT') == 'AP':
                    self.productName = 'DisneyOnline-AP'

        self.blue = None
        if self.launcher:
            self.blue = self.launcher.getBlue()

        fakeBlue = config.GetString('fake-blue', '')
        if fakeBlue:
            self.blue = fakeBlue

        self.playToken = None
        if self.launcher:
            self.playToken = self.launcher.getPlayToken()

        fakePlayToken = config.GetString('fake-playtoken', '')
        if fakePlayToken:
            self.playToken = fakePlayToken

        self.DISLToken = None
        if self.launcher:
            self.DISLToken = self.launcher.getDISLToken()

        fakeDISLToken = config.GetString('fake-DISLToken', '')
        fakeDISLPlayerName = config.GetString('fake-DISL-PlayerName', '')
        if fakeDISLToken:
            self.DISLToken = fakeDISLToken
        elif fakeDISLPlayerName:
            defaultId = 42
            defaultNumAvatars = 4
            defaultNumAvatarSlots = 4
            defaultNumConcur = 1
            subCount = config.GetInt('fake-DISL-NumSubscriptions', 1)
            playerAccountId = config.GetInt('fake-DISL-PlayerAccountId', defaultId)
            self.DISLToken = 'ACCOUNT_NAME=%s' % fakeDISLPlayerName + '&ACCOUNT_NUMBER=%s' % playerAccountId + '&ACCOUNT_NAME_APPROVAL=%s' % config.GetString('fake-DISL-PlayerNameApproved', 'YES') + '&SWID=%s' % config.GetString('fake-DISL-SWID', '{1763AC36-D73F-41C2-A54A-B579E58B69C8}') + '&FAMILY_NUMBER=%s' % config.GetString('fake-DISL-FamilyAccountId', '-1') + '&familyAdmin=%s' % config.GetString('fake-DISL-FamilyAdmin', '1') + '&PIRATES_ACCESS=%s' % config.GetString('fake-DISL-PiratesAccess', 'FULL') + '&PIRATES_MAX_NUM_AVATARS=%s' % config.GetInt('fake-DISL-MaxAvatars', defaultNumAvatars) + '&PIRATES_NUM_AVATAR_SLOTS=%s' % config.GetInt('fake-DISL-MaxAvatarSlots', defaultNumAvatarSlots) + '&expires=%s' % config.GetString('fake-DISL-expire', '1577898000') + '&OPEN_CHAT_ENABLED=%s' % config.GetString('fake-DISL-OpenChatEnabled', 'YES') + '&CREATE_FRIENDS_WITH_CHAT=%s' % config.GetString('fake-DISL-CreateFriendsWithChat', 'YES') + '&CHAT_CODE_CREATION_RULE=%s' % config.GetString('fake-DISL-ChatCodeCreation', 'YES') + '&FAMILY_MEMBERS=%s' % config.GetString('fake-DISL-FamilyMembers') + '&PIRATES_SUB_COUNT=%s' % subCount
            for i in range(subCount):
                self.DISLToken += '&PIRATES_SUB_%s_ACCESS=%s' % (i, config.GetString('fake-DISL-Sub-%s-Access' % i, 'FULL')) + '&PIRATES_SUB_%s_ACTIVE=%s' % (i, config.GetString('fake-DISL-Sub-%s-Active' % i, 'YES')) + '&PIRATES_SUB_%s_ID=%s' % (i, config.GetInt('fake-DISL-Sub-%s-Id' % i, playerAccountId) + config.GetInt('fake-DISL-Sub-Id-Offset', 0)) + '&PIRATES_SUB_%s_LEVEL=%s' % (i, config.GetInt('fake-DISL-Sub-%s-Level' % i, 3)) + '&PIRATES_SUB_%s_NAME=%s' % (i, config.GetString('fake-DISL-Sub-%s-Name' % i, fakeDISLPlayerName)) + '&PIRATES_SUB_%s_NUM_AVATARS=%s' % (i, config.GetInt('fake-DISL-Sub-%s-NumAvatars' % i, defaultNumAvatars)) + '&PIRATES_SUB_%s_NUM_CONCUR=%s' % (i, config.GetInt('fake-DISL-Sub-%s-NumConcur' % i, defaultNumConcur)) + '&PIRATES_SUB_%s_OWNERID=%s' % (i, config.GetInt('fake-DISL-Sub-%s-OwnerId' % i, playerAccountId)) + '&PIRATES_SUB_%s_FOUNDER=%s' % (i, config.GetString('fake-DISL-Sub-%s-Founder' % i, 'YES'))

            self.DISLToken += '&WL_CHAT_ENABLED=%s' % config.GetString('fake-DISL-WLChatEnabled', 'YES') + '&valid=true'
            print(self.DISLToken)

        self.requiredLogin = config.GetString('required-login', 'auto')
        if self.requiredLogin == 'auto':
            self.notify.info('required-login auto.')
        elif self.requiredLogin == 'green':
            self.notify.error('The green code is out of date')
        elif self.requiredLogin == 'blue':
            if not self.blue:
                self.notify.error('The tcr does not have the required blue login')

        elif self.requiredLogin == 'playToken':
            if not self.playToken:
                self.notify.error('The tcr does not have the required playToken login')

        elif self.requiredLogin == 'DISLToken':
            if not self.DISLToken:
                self.notify.error('The tcr does not have the required DISL token login')

        elif self.requiredLogin == 'gameServer':
            self.notify.info('Using game server name/password.')
            self.DISLToken = None
        else:
            self.notify.error('The required-login was not recognized.')
        self.computeValidateDownload()
        self.wantMagicWords = base.config.GetString('want-magic-words', '')
        if self.launcher and hasattr(self.launcher, 'http'):
            self.http = self.launcher.http
        else:
            self.http = HTTPClient()
        self.allocateDcFile()
        self.accountOldAuth = config.GetBool('account-old-auth', 0)
        self.accountOldAuth = config.GetBool('%s-account-old-auth' % game.name, self.accountOldAuth)
        if self.accountOldAuth:
            self.loginInterface = LoginGSAccount.LoginGSAccount(self)
            self.notify.info('loginInterface: LoginGSAccount')
        elif self.blue:
            self.loginInterface = LoginGoAccount.LoginGoAccount(self)
            self.notify.info('loginInterface: LoginGoAccount')
        elif self.playToken:
            self.loginInterface = LoginWebPlayTokenAccount(self)
            self.notify.info('loginInterface: LoginWebPlayTokenAccount')
        elif self.DISLToken:
            self.loginInterface = LoginDISLTokenAccount(self)
            self.notify.info('loginInterface: LoginDISLTokenAccount')
        else:
            self.loginInterface = LoginTTAccount.LoginTTAccount(self)
            self.notify.info('loginInterface: LoginTTAccount')
        self.secretChatAllowed = base.config.GetBool('allow-secret-chat', 0)
        self.openChatAllowed = base.config.GetBool('allow-open-chat', 0)
        self.secretChatNeedsParentPassword = base.config.GetBool('secret-chat-needs-parent-password', 0) or self.launcher and self.launcher.getNeedPwForSecretKey()
        self.parentPasswordSet = base.config.GetBool('parent-password-set', 0) or self.launcher and self.launcher.getParentPasswordSet()
        self.userSignature = base.config.GetString('signature', 'none')
        self.freeTimeExpiresAt = -1
        self.__isPaid = 0
        self.periodTimerExpired = 0
        self.periodTimerStarted = None
        self.periodTimerSecondsRemaining = None
        self.parentMgr.registerParent(OTPGlobals.SPRender, base.render)
        self.parentMgr.registerParent(OTPGlobals.SPHidden, NodePath())
        self.timeManager = None
        if config.GetBool('detect-leaks', 0) or config.GetBool('client-detect-leaks', 0):
            self.startLeakDetector()

        if config.GetBool('detect-messenger-leaks', 0) or config.GetBool('ai-detect-messenger-leaks', 0):
            self.messengerLeakDetector = MessengerLeakDetector.MessengerLeakDetector('client messenger leak detector')
            if config.GetBool('leak-messages', 0):
                MessengerLeakDetector._leakMessengerObject()

        if config.GetBool('run-garbage-reports', 0) or config.GetBool('client-run-garbage-reports', 0):
            noneValue = -1.0
            reportWait = config.GetFloat('garbage-report-wait', noneValue)
            reportWaitScale = config.GetFloat('garbage-report-wait-scale', noneValue)
            if reportWait == noneValue:
                reportWait = 60.0 * 2.0

            if reportWaitScale == noneValue:
                reportWaitScale = None

            self.garbageReportScheduler = GarbageReportScheduler(waitBetween = reportWait, waitScale = reportWaitScale)

        self.activeDistrictMap = {}
        self.serverVersion = serverVersion
        self.waitingForDatabase = None
        self.loginFSM = ClassicFSM('loginFSM', [
            State('loginOff', self.enterLoginOff, self.exitLoginOff, [
                'connect']),
            State('connect', self.enterConnect, self.exitConnect, [
                'login',
                'failedToConnect',
                'failedToGetServerConstants']),
            State('login', self.enterLogin, self.exitLogin, [
                'noConnection',
                'waitForGameList',
                'createAccount',
                'reject',
                'failedToConnect',
                'shutdown']),
            State('createAccount', self.enterCreateAccount, self.exitCreateAccount, [
                'noConnection',
                'waitForGameList',
                'login',
                'reject',
                'failedToConnect',
                'shutdown']),
            State('failedToConnect', self.enterFailedToConnect, self.exitFailedToConnect, [
                'connect',
                'shutdown']),
            State('failedToGetServerConstants', self.enterFailedToGetServerConstants, self.exitFailedToGetServerConstants, [
                'connect',
                'shutdown',
                'noConnection']),
            State('shutdown', self.enterShutdown, self.exitShutdown, [
                'loginOff']),
            State('waitForGameList', self.enterWaitForGameList, self.exitWaitForGameList, [
                'noConnection',
                'waitForShardList',
                'missingGameRootObject']),
            State('missingGameRootObject', self.enterMissingGameRootObject, self.exitMissingGameRootObject, [
                'waitForGameList',
                'shutdown']),
            State('waitForShardList', self.enterWaitForShardList, self.exitWaitForShardList, [
                'noConnection',
                'waitForAvatarList',
                'noShards']),
            State('noShards', self.enterNoShards, self.exitNoShards, [
                'noConnection',
                'noShardsWait',
                'shutdown']),
            State('noShardsWait', self.enterNoShardsWait, self.exitNoShardsWait, [
                'noConnection',
                'waitForShardList',
                'shutdown']),
            State('reject', self.enterReject, self.exitReject, []),
            State('noConnection', self.enterNoConnection, self.exitNoConnection, [
                'login',
                'connect',
                'shutdown']),
            State('afkTimeout', self.enterAfkTimeout, self.exitAfkTimeout, [
                'waitForAvatarList',
                'shutdown']),
            State('periodTimeout', self.enterPeriodTimeout, self.exitPeriodTimeout, [
                'shutdown']),
            State('waitForAvatarList', self.enterWaitForAvatarList, self.exitWaitForAvatarList, [
                'noConnection',
                'chooseAvatar',
                'shutdown']),
            State('chooseAvatar', self.enterChooseAvatar, self.exitChooseAvatar, [
                'noConnection',
                'createAvatar',
                'waitForAvatarList',
                'waitForSetAvatarResponse',
                'waitForDeleteAvatarResponse',
                'shutdown',
                'login']),
            State('createAvatar', self.enterCreateAvatar, self.exitCreateAvatar, [
                'noConnection',
                'chooseAvatar',
                'waitForSetAvatarResponse',
                'shutdown']),
            State('waitForDeleteAvatarResponse', self.enterWaitForDeleteAvatarResponse, self.exitWaitForDeleteAvatarResponse, [
                'noConnection',
                'chooseAvatar',
                'shutdown']),
            State('rejectRemoveAvatar', self.enterRejectRemoveAvatar, self.exitRejectRemoveAvatar, [
                'noConnection',
                'chooseAvatar',
                'shutdown']),
            State('waitForSetAvatarResponse', self.enterWaitForSetAvatarResponse, self.exitWaitForSetAvatarResponse, [
                'noConnection',
                'playingGame',
                'shutdown']),
            State('playingGame', self.enterPlayingGame, self.exitPlayingGame, [
                'noConnection',
                'waitForAvatarList',
                'login',
                'shutdown',
                'afkTimeout',
                'periodTimeout',
                'noShards'])], 'loginOff', 'loginOff')
        self.gameFSM = ClassicFSM('gameFSM', [
            State('gameOff', self.enterGameOff, self.exitGameOff, [
                'waitOnEnterResponses']),
            State('waitOnEnterResponses', self.enterWaitOnEnterResponses, self.exitWaitOnEnterResponses, [
                'playGame',
                'tutorialQuestion',
                'gameOff']),
            State('tutorialQuestion', self.enterTutorialQuestion, self.exitTutorialQuestion, [
                'playGame',
                'gameOff']),
            State('playGame', self.enterPlayGame, self.exitPlayGame, [
                'gameOff',
                'closeShard',
                'switchShards']),
            State('switchShards', self.enterSwitchShards, self.exitSwitchShards, [
                'gameOff',
                'waitOnEnterResponses']),
            State('closeShard', self.enterCloseShard, self.exitCloseShard, [
                'gameOff',
                'waitOnEnterResponses'])], 'gameOff', 'gameOff')
        self.loginFSM.getStateNamed('playingGame').addChild(self.gameFSM)
        self.loginFSM.enterInitialState()
        self.loginScreen = None
        self.music = None
        self.gameDoneEvent = 'playGameDone'
        self.playGame = playGame(self.gameFSM, self.gameDoneEvent)
        self.shardInterestHandle = None
        self.uberZoneInterest = None
        self.wantSwitchboard = config.GetBool('want-switchboard', 0)
        self.wantSwitchboardHacks = base.config.GetBool('want-switchboard-hacks', 0)

        self.__pendingGenerates = {}
        self.__pendingMessages = {}
        self.__doId2pendingInterest = {}

        self.centralLogger = self.generateGlobalObject(OtpDoGlobals.OTP_DO_ID_CENTRAL_LOGGER, 'CentralLogger')
        self.csm = None

    def startLeakDetector(self):
        if hasattr(self, 'leakDetector'):
            return False

        firstCheckDelay = config.GetFloat('leak-detector-first-check-delay', 2 * 60.0)
        self.leakDetector = ContainerLeakDetector('client container leak detector', firstCheckDelay = firstCheckDelay)
        self.garbageLeakDetector = LeakDetectors.GarbageLeakDetector()
        self.renderLeakDetector = LeakDetectors.SceneGraphLeakDetector(render)
        self.hiddenLeakDetector = LeakDetectors.SceneGraphLeakDetector(hidden)
        self.cppMemoryUsageLeakDetector = LeakDetectors.CppMemoryUsage()
        self.taskLeakDetector = LeakDetectors.TaskLeakDetector()
        return True

    def getGameDoId(self):
        return self.GameGlobalsId

    def enterLoginOff(self):
        self.handler = self.handleMessageType
        self.shardInterestHandle = None

    def exitLoginOff(self):
        self.handler = None

    def computeValidateDownload(self):
        if self.launcher:
            hash = HashVal()
            hash.mergeWith(launcher.launcherFileDbHash)
            hash.mergeWith(launcher.serverDbFileHash)
            self.validateDownload = hash.asHex()
        else:
            self.validateDownload = ''
            basePath = os.path.expandvars('$TOONTOWN') or './toontown'
            downloadParFilename = Filename.expandFrom(basePath + '/src/configfiles/download.par')
            if downloadParFilename.exists():
                downloadPar = open(downloadParFilename.toOsSpecific())
                for line in downloadPar.readlines():
                    i = line.find('VALIDATE_DOWNLOAD=')
                    if i != -1:
                        self.validateDownload = line[i + 18:].strip()
                        break

    def getServerVersion(self):
        return self.serverVersion

    def enterConnect(self, serverList):
        self.serverList = serverList
        dialogClass = OTPGlobals.getGlobalDialogClass()
        self.connectingBox = dialogClass(message = OTPLocalizer.CRConnecting)
        self.connectingBox.show()
        self.renderFrame()
        self.handler = self.handleConnecting
        self.connect(self.serverList, successCallback = self._sendHello, failureCallback = self.failedToConnect)

    def _sendHello(self):
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_HELLO)
        datagram.addUint32(self.hashVal)
        datagram.addString(self.serverVersion)
        self.send(datagram)

    def handleConnecting(self, msgtype, di):
        if msgtype == CLIENT_HELLO_RESP:
            self._handleConnected()
        else:
            self.handleMessageType(msgtype, di)

    def failedToConnect(self, statusCode, statusString):
        self.loginFSM.request('failedToConnect', [
            statusCode,
            statusString])

    def exitConnect(self):
        self.connectingBox.cleanup()
        del self.connectingBox

    def handleSystemMessage(self, di):
        message = ClientRepositoryBase.handleSystemMessage(self, di)
        whisper = WhisperPopup(message, OTPGlobals.getInterfaceFont(), WhisperPopup.WTSystem)
        whisper.manage(base.marginManager)
        if not self.systemMessageSfx:
            self.systemMessageSfx = base.loader.loadSfx('phase_3.5/audio/sfx/GUI_whisper_3.mp3')

        if self.systemMessageSfx:
            base.playSfx(self.systemMessageSfx)

    def getConnectedEvent(self):
        return 'OTPClientRepository-connected'

    def _handleConnected(self):
        messenger.send(self.getConnectedEvent())
        self.gotoFirstScreen()

    def gotoFirstScreen(self):

        try:
            self.accountServerConstants = AccountServerConstants.AccountServerConstants(self)
        except TTAccount.TTAccountException as e:
            self.notify.debug(str(e))
            self.loginFSM.request('failedToGetServerConstants', [e])
            return

        self.startReaderPollTask()
        self.startHeartbeat()
        newInstall = launcher.getIsNewInstallation()
        newInstall = base.config.GetBool('new-installation', newInstall)
        self.loginFSM.request('login')

    def enterLogin(self):
        self.renderFrame()
        self.loginDoneEvent = 'loginDone'
        self.accept(self.loginDoneEvent, self.__handleLoginDone)
        self.csm.performLogin(self.loginDoneEvent)
        self.waitForDatabaseTimeout(requestName='WaitOnCSMLoginResponse')

        if config.GetBool('want-login-screen', 0):
            self.loginScreen = LoginScreen.LoginScreen(self, self.loginDoneEvent)
            self.accept(self.loginDoneEvent, self.__handleLoginDone)
            self.loginScreen.load()
            self.loginScreen.enter()

    def setGameType(self):
        if self.createAvatarClass:
            className = self.createAvatarClass.__name__
            dclass = self.dclassesByName[className]
            if className != 'DistributedToon':
                datagram = PyDatagram()
                datagram.addUint16(CLIENT_SET_AVTYPE)
                datagram.addUint16(dclass.getNumber())
                self.send(datagram)

    def __handleLoginDone(self, doneStatus):
        mode = doneStatus['mode']
        if mode == 'success':
            self.setIsNotNewInstallation()
            self.loginFSM.request('waitForGameList')
        elif mode == 'getChatPassword':
            self.loginFSM.request('parentPassword')
        elif mode == 'freeTimeExpired':
            self.loginFSM.request('freeTimeInform')
        elif mode == 'createAccount':
            self.loginFSM.request('createAccount', [
                {
                    'back': 'login',
                    'backArgs': []}])
        elif mode == 'reject':
            self.loginFSM.request('reject')
        elif mode == 'quit':
            self.loginFSM.request('shutdown')
        elif mode == 'failure':
            self.loginFSM.request('failedToConnect', [
                -1,
                '?'])
        else:
            self.notify.error('Invalid doneStatus mode from loginScreen: ' + str(mode))

    def exitLogin(self):
        if self.loginScreen:
            self.loginScreen.exit()
            self.loginScreen.unload()
            self.loginScreen = None
            self.renderFrame()

        self.ignore(self.loginDoneEvent)
        del self.loginDoneEvent
        self.handler = None

    def enterCreateAccount(self, createAccountDoneData = {'back': 'login', 'backArgs': []}):
        self.createAccountDoneData = createAccountDoneData
        self.createAccountDoneEvent = 'createAccountDone'
        self.createAccountScreen = None
        self.createAccountScreen = CreateAccountScreen(self, self.createAccountDoneEvent)
        self.accept(self.createAccountDoneEvent, self.__handleCreateAccountDone)
        self.createAccountScreen.load()
        self.createAccountScreen.enter()

    def __handleCreateAccountDone(self, doneStatus):
        mode = doneStatus['mode']
        if mode == 'success':
            self.setIsNotNewInstallation()
            self.loginFSM.request('waitForGameList')
        elif mode == 'reject':
            self.loginFSM.request('reject')
        elif mode == 'cancel':
            self.loginFSM.request(self.createAccountDoneData['back'], self.createAccountDoneData['backArgs'])
        elif mode == 'failure':
            self.loginFSM.request(self.createAccountDoneData['back'], self.createAccountDoneData['backArgs'])
        elif mode == 'quit':
            self.loginFSM.request('shutdown')
        else:
            self.notify.error('Invalid doneStatus mode from CreateAccountScreen: ' + str(mode))

    def exitCreateAccount(self):
        if self.createAccountScreen:
            self.createAccountScreen.exit()
            self.createAccountScreen.unload()
            self.createAccountScreen = None
            self.renderFrame()

        self.ignore(self.createAccountDoneEvent)
        del self.createAccountDoneEvent
        self.handler = None

    def enterFailedToConnect(self, statusCode, statusString):
        self.handler = self.handleMessageType
        url = self.serverList[0]
        self.notify.warning('Failed to connect to %s (%s %s).  Notifying user.' % (url.cStr(), statusCode, statusString))
        if statusCode == 1403 or statusCode == 1405 or statusCode == 1400:
            message = OTPLocalizer.CRNoConnectProxyNoPort % (url.getServer(), url.getPort(), url.getPort())
            style = OTPDialog.CancelOnly
        else:
            message = OTPLocalizer.CRNoConnectTryAgain % (url.getServer(), url.getPort())
            style = OTPDialog.TwoChoice
        dialogClass = OTPGlobals.getGlobalDialogClass()
        self.failedToConnectBox = dialogClass(message = message, doneEvent = 'failedToConnectAck', text_wordwrap = 18, style = style)
        self.failedToConnectBox.show()
        self.notify.info(message)
        self.accept('failedToConnectAck', self.__handleFailedToConnectAck)

    def __handleFailedToConnectAck(self):
        doneStatus = self.failedToConnectBox.doneStatus
        if doneStatus == 'ok':
            self.loginFSM.request('connect', [
                self.serverList])
        elif doneStatus == 'cancel':
            self.loginFSM.request('shutdown')
        else:
            self.notify.error('Unrecognized doneStatus: ' + str(doneStatus))

    def exitFailedToConnect(self):
        self.handler = None
        self.ignore('failedToConnectAck')
        self.failedToConnectBox.cleanup()
        del self.failedToConnectBox

    def enterFailedToGetServerConstants(self, e):
        self.handler = self.handleMessageType
        url = AccountServerConstants.AccountServerConstants.getServerURL()
        statusCode = 0
        if isinstance(e, HTTPUtil.ConnectionError):
            statusCode = e.statusCode
            self.notify.warning('Got status code %s from connection to %s.' % (statusCode, url.cStr()))
        else:
            self.notify.warning("Didn't get status code from connection to %s." % url.cStr())
        if statusCode == 1403 or statusCode == 1400:
            message = OTPLocalizer.CRServerConstantsProxyNoPort % (url.cStr(), url.getPort())
            style = OTPDialog.CancelOnly
        elif statusCode == 1405:
            message = OTPLocalizer.CRServerConstantsProxyNoCONNECT % url.cStr()
            style = OTPDialog.CancelOnly
        else:
            message = OTPLocalizer.CRServerConstantsTryAgain % url.cStr()
            style = OTPDialog.TwoChoice
        dialogClass = OTPGlobals.getGlobalDialogClass()
        self.failedToGetConstantsBox = dialogClass(message = message, doneEvent = 'failedToGetConstantsAck', text_wordwrap = 18, style = style)
        self.failedToGetConstantsBox.show()
        self.accept('failedToGetConstantsAck', self.__handleFailedToGetConstantsAck)
        self.notify.warning('Failed to get account server constants. Notifying user.')

    def __handleFailedToGetConstantsAck(self):
        doneStatus = self.failedToGetConstantsBox.doneStatus
        if doneStatus == 'ok':
            self.loginFSM.request('connect', [
                self.serverList])
        elif doneStatus == 'cancel':
            self.loginFSM.request('shutdown')
        else:
            self.notify.error('Unrecognized doneStatus: ' + str(doneStatus))

    def exitFailedToGetServerConstants(self):
        self.handler = None
        self.ignore('failedToGetConstantsAck')
        self.failedToGetConstantsBox.cleanup()
        del self.failedToGetConstantsBox

    def enterShutdown(self, errorCode = None):
        self.handler = self.handleMessageType
        self.sendDisconnect()
        self.notify.info('Exiting cleanly')
        base.exitShow(errorCode)

    def exitShutdown(self):
        if hasattr(self, 'garbageWatcher'):
            self.garbageWatcher.destroy()
            del self.garbageWatcher

        self.handler = None

    def enterWaitForGameList(self):
        self.gameDoDirectory = self.addInterest(self.GameGlobalsId, OTP_ZONE_ID_MANAGEMENT, 'game directory', 'GameList_Complete')
        self.acceptOnce('GameList_Complete', self.waitForGetGameListResponse)

    def waitForGetGameListResponse(self):
        if self.isGameListCorrect():
            if base.config.GetBool('game-server-tests', 0):
                from otp.distributed import GameServerTestSuite
                GameServerTestSuite.GameServerTestSuite(self)

            self.loginFSM.request('waitForShardList')
        else:
            self.loginFSM.request('missingGameRootObject')

    def isGameListCorrect(self):
        return 1

    def exitWaitForGameList(self):
        self.handler = None

    def enterMissingGameRootObject(self):
        self.notify.warning('missing some game root objects.')
        self.handler = self.handleMessageType
        dialogClass = OTPGlobals.getGlobalDialogClass()
        self.missingGameRootObjectBox = dialogClass(message = OTPLocalizer.CRMissingGameRootObject, doneEvent = 'missingGameRootObjectBoxAck', style = OTPDialog.TwoChoice)
        self.missingGameRootObjectBox.show()
        self.accept('missingGameRootObjectBoxAck', self.__handleMissingGameRootObjectAck)

    def __handleMissingGameRootObjectAck(self):
        doneStatus = self.missingGameRootObjectBox.doneStatus
        if doneStatus == 'ok':
            self.loginFSM.request('waitForGameList')
        elif doneStatus == 'cancel':
            self.loginFSM.request('shutdown')
        else:
            self.notify.error('Unrecognized doneStatus: ' + str(doneStatus))

    def exitMissingGameRootObject(self):
        self.handler = None
        self.ignore('missingGameRootObjectBoxAck')
        self.missingGameRootObjectBox.cleanup()
        del self.missingGameRootObjectBox

    def enterWaitForShardList(self):
        if not self.isValidInterestHandle(self.shardInterestHandle):
            self.shardInterestHandle = self.addInterest(self.GameGlobalsId, OTP_ZONE_ID_DISTRICTS, 'LocalShardList', 'ShardList_Complete')
            self.acceptOnce('ShardList_Complete', self._wantShardListComplete)
        else:
            self._wantShardListComplete()

    def exitWaitForShardList(self):
        self.ignore('ShardList_Complete')
        self.handler = None

    def _shardsAreReady(self):
        for shard in list(self.activeDistrictMap.values()):
            if shard.available:
                return True
        else:
            return False

    def _wantShardListComplete(self):
        if self._shardsAreReady():
            self.loginFSM.request('waitForAvatarList')
        else:
            self.loginFSM.request('noShards')

    def enterNoShards(self):
        self.handler = self.handleMessageType
        dialogClass = OTPGlobals.getGlobalDialogClass()
        self.noShardsBox = dialogClass(message = OTPLocalizer.CRNoDistrictsTryAgain, doneEvent = 'noShardsAck', style = OTPDialog.TwoChoice)
        self.noShardsBox.show()
        self.accept('noShardsAck', self.__handleNoShardsAck)

    def __handleNoShardsAck(self):
        doneStatus = self.noShardsBox.doneStatus
        if doneStatus == 'ok':
            self.loginFSM.request('noShardsWait')
        elif doneStatus == 'cancel':
            self.loginFSM.request('shutdown')
        else:
            self.notify.error('Unrecognized doneStatus: ' + str(doneStatus))

    def exitNoShards(self):
        self.handler = None
        self.ignore('noShardsAck')
        self.noShardsBox.cleanup()
        del self.noShardsBox

    def enterNoShardsWait(self):
        dialogClass = OTPGlobals.getGlobalDialogClass()
        self.connectingBox = dialogClass(message = OTPLocalizer.CRConnecting)
        self.connectingBox.show()
        self.renderFrame()
        self.noShardsWaitTaskName = 'noShardsWait'

        def doneWait(task, self = self):
            self.loginFSM.request('waitForShardList')

        if __dev__:
            delay = 0.0
        else:
            delay = 6.5 + random.random() * 2.0
        taskMgr.doMethodLater(delay, doneWait, self.noShardsWaitTaskName)

    def exitNoShardsWait(self):
        taskMgr.remove(self.noShardsWaitTaskName)
        del self.noShardsWaitTaskName
        self.connectingBox.cleanup()
        del self.connectingBox

    def enterReject(self):
        self.handler = self.handleMessageType
        self.notify.warning('Connection Rejected')
        launcher.setPandaErrorCode(13)
        sys.exit()

    def exitReject(self):
        self.handler = None

    def enterNoConnection(self):
        self.resetInterestStateForConnectionLoss()
        self.shardInterestHandle = None
        self.handler = self.handleMessageType
        self.__currentAvId = 0
        self.stopHeartbeat()
        self.stopReaderPollTask()
        gameUsername = '???' # TODO: Pull playtoken?
        if self.bootedIndex != None and self.bootedIndex in OTPLocalizer.CRBootedReasons:
            message = OTPLocalizer.CRBootedReasons[self.bootedIndex] % {
                'name': gameUsername}
        elif self.bootedText != None:
            message = OTPLocalizer.CRBootedReasonUnknownCode % self.bootedIndex
        else:
            message = OTPLocalizer.CRLostConnection
        reconnect = 1
        if self.bootedIndex == 152:
            reconnect = 0

        style = OTPDialog.Acknowledge
        if reconnect and self.loginInterface.supportsRelogin():
            message += OTPLocalizer.CRTryConnectAgain
            style = OTPDialog.TwoChoice

        dialogClass = OTPGlobals.getGlobalDialogClass()
        self.lostConnectionBox = dialogClass(doneEvent = 'lostConnectionAck', message = message, text_wordwrap = 18, style = style)
        self.lostConnectionBox.show()
        self.accept('lostConnectionAck', self.__handleLostConnectionAck)
        self.notify.warning('Lost connection to server. Notifying user.')

    def __handleLostConnectionAck(self):
        if self.lostConnectionBox.doneStatus == 'ok' and self.loginInterface.supportsRelogin():
            self.loginFSM.request('connect', [
                self.serverList])
        else:
            self.loginFSM.request('shutdown')

    def exitNoConnection(self):
        self.handler = None
        self.ignore('lostConnectionAck')
        self.lostConnectionBox.cleanup()

    def enterAfkTimeout(self):
        self.sendSetAvatarIdMsg(0)
        msg = OTPLocalizer.AfkForceAcknowledgeMessage
        dialogClass = OTPGlobals.getDialogClass()
        self.afkDialog = dialogClass(text = msg, command = self.__handleAfkOk, style = OTPDialog.Acknowledge)
        self.handler = self.handleMessageType

    def __handleAfkOk(self, value):
        self.loginFSM.request('waitForAvatarList')

    def exitAfkTimeout(self):
        if self.afkDialog:
            self.afkDialog.cleanup()
            self.afkDialog = None

        self.handler = None

    def enterPeriodTimeout(self):
        self.sendSetAvatarIdMsg(0)
        self.sendDisconnect()
        msg = OTPLocalizer.PeriodForceAcknowledgeMessage
        dialogClass = OTPGlobals.getDialogClass()
        self.periodDialog = dialogClass(text = msg, command = self.__handlePeriodOk, style = OTPDialog.Acknowledge)
        self.handler = self.handleMessageType

    def __handlePeriodOk(self, value):
        base.exitShow()

    def exitPeriodTimeout(self):
        if self.periodDialog:
            self.periodDialog.cleanup()
            self.periodDialog = None

        self.handler = None

    def enterWaitForAvatarList(self):
        self._requestAvatarList()

    def _requestAvatarList(self):
        self.csm.requestAvatars()
        self.waitForDatabaseTimeout(requestName = 'WaitForAvatarList')
        self.acceptOnce(OtpAvatarManager.OtpAvatarManager.OnlineEvent, self._requestAvatarList)

    def sendGetAvatarsMsg(self):
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_GET_AVATARS)
        self.send(datagram)

    def exitWaitForAvatarList(self):
        self.cleanupWaitingForDatabase()
        self.ignore(OtpAvatarManager.OtpAvatarManager.OnlineEvent)
        self.handler = None

    def handleAvatarsList(self, avatars):
        self.avList = avatars
        self.loginFSM.request('chooseAvatar', [self.avList])

    def handleWaitForAvatarList(self, msgType, di):
        if msgType == CLIENT_GET_AVATARS_RESP:
            self.handleGetAvatarsRespMsg(di)
        elif msgType == CLIENT_GET_AVATARS_RESP2:
            pass
        else:
            self.handleMessageType(msgType, di)

    def handleGetAvatarsRespMsg(self, di):
        returnCode = di.getUint8()
        if returnCode == 0:
            avatarTotal = di.getUint16()
            avList = []
            for i in range(0, avatarTotal):
                avNum = di.getUint32()
                avNames = [
                    '',
                    '',
                    '',
                    '']
                avNames[0] = di.getString()
                avNames[1] = di.getString()
                avNames[2] = di.getString()
                avNames[3] = di.getString()
                avDNA = di.getString()
                avPosition = di.getUint8()
                aname = di.getUint8()
                potAv = PotentialAvatar(avNum, avNames, avDNA, avPosition, aname)
                avList.append(potAv)

            self.avList = avList
            self.loginFSM.request('chooseAvatar', [
                self.avList])
        else:
            self.notify.error('Bad avatar list return code: ' + str(returnCode))
            self.loginFSM.request('shutdown')

    def handleGetAvatarsResp2Msg(self, di):
        returnCode = di.getUint8()
        if returnCode == 0:
            avatarTotal = di.getUint16()
            avList = []
            for i in range(0, avatarTotal):
                avNum = di.getUint32()
                avNames = [
                    '',
                    '',
                    '',
                    '']
                avNames[0] = di.getString()
                avDNA = None
                avPosition = di.getUint8()
                aname = None
                potAv = PotentialAvatar(avNum, avNames, avDNA, avPosition, aname)
                avList.append(potAv)

            self.avList = avList
            self.loginFSM.request('chooseAvatar', [
                self.avList])
        else:
            self.notify.error('Bad avatar list return code: ' + str(returnCode))
            self.loginFSM.request('shutdown')

    def enterChooseAvatar(self, avList):
        pass

    def exitChooseAvatar(self):
        pass

    def enterCreateAvatar(self, avList, index, newDNA = None):
        pass

    def exitCreateAvatar(self):
        pass

    def sendCreateAvatarMsg(self, avDNA, avName, avPosition):
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_CREATE_AVATAR)
        datagram.addUint16(0)
        datagram.addString(avDNA.makeNetString())
        datagram.addUint8(avPosition)
        self.newName = avName
        self.newDNA = avDNA
        self.newPosition = avPosition
        self.send(datagram)

    def sendCreateAvatar2Msg(self, avClass, avDNA, avName, avPosition):
        className = avClass.__name__
        dclass = self.dclassesByName[className]
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_CREATE_AVATAR2)
        datagram.addUint16(0)
        datagram.addUint8(avPosition)
        datagram.addUint16(dclass.getNumber())
        self.newName = avName
        self.newDNA = avDNA
        self.newPosition = avPosition
        self.send(datagram)

    def enterWaitForDeleteAvatarResponse(self, potAv):
        self.csm.sendDeleteAvatar(potAv.id)
        self.waitForDatabaseTimeout(requestName = 'WaitForDeleteAvatarResponse')

    def sendDeleteAvatarMsg(self, avId):
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_DELETE_AVATAR)
        datagram.addUint32(avId)
        self.send(datagram)

    def exitWaitForDeleteAvatarResponse(self):
        self.cleanupWaitingForDatabase()
        self.handler = None

    def handleWaitForDeleteAvatarResponse(self, msgType, di):
        if msgType == CLIENT_DELETE_AVATAR_RESP:
            self.handleGetAvatarsRespMsg(di)
        else:
            self.handleMessageType(msgType, di)

    def enterRejectRemoveAvatar(self, reasonCode):
        self.notify.warning('Rejected removed avatar. (%s)' % (reasonCode,))
        self.handler = self.handleMessageType
        dialogClass = OTPGlobals.getGlobalDialogClass()
        self.rejectRemoveAvatarBox = dialogClass(message = '%s\n(%s)' % (OTPLocalizer.CRRejectRemoveAvatar, reasonCode), doneEvent = 'rejectRemoveAvatarAck', style = OTPDialog.Acknowledge)
        self.rejectRemoveAvatarBox.show()
        self.accept('rejectRemoveAvatarAck', self.__handleRejectRemoveAvatar)

    def __handleRejectRemoveAvatar(self):
        self.loginFSM.request('chooseAvatar')

    def exitRejectRemoveAvatar(self):
        self.handler = None
        self.ignore('rejectRemoveAvatarAck')
        self.rejectRemoveAvatarBox.cleanup()
        del self.rejectRemoveAvatarBox

    def enterWaitForSetAvatarResponse(self, potAv):
        self.sendSetAvatarMsg(potAv)
        self.waitForDatabaseTimeout(requestName = 'WaitForSetAvatarResponse')

    def exitWaitForSetAvatarResponse(self):
        self.cleanupWaitingForDatabase()
        self.handler = None

    def sendSetAvatarMsg(self, potAv):
        self.sendSetAvatarIdMsg(potAv.id)
        self.avData = potAv

    def sendSetAvatarIdMsg(self, avId):
        if avId != self.__currentAvId:
            self.__currentAvId = avId
            self.csm.sendChooseAvatar(avId)
            if avId == 0:
                self.stopPeriodTimer()
            else:
                self.startPeriodTimer()

    def handleAvatarResponseMsg(self, di):
        pass

    def handleWaitForSetAvatarResponse(self, msgType, di):
        if msgType == CLIENT_GET_AVATAR_DETAILS_RESP:
            self.handleAvatarResponseMsg(di)
        elif msgType == CLIENT_GET_PET_DETAILS_RESP:
            self.handleAvatarResponseMsg(di)
        elif msgType == CLIENT_GET_FRIEND_LIST_RESP:
            self.handleGetFriendsList(di)
        elif msgType == CLIENT_GET_FRIEND_LIST_EXTENDED_RESP:
            self.handleGetFriendsListExtended(di)
        elif msgType == CLIENT_FRIEND_ONLINE:
            self.handleFriendOnline(di)
        elif msgType == CLIENT_FRIEND_OFFLINE:
            self.handleFriendOffline(di)
        else:
            self.handleMessageType(msgType, di)

    def enterPlayingGame(self):
        pass

    def exitPlayingGame(self):
        pass

    def detectLeaks(self, okTasks = None, okEvents = None):
        if not base.config.GetBool('enforce-clean-exit', 1):
            self.notify.warning('Not enforcing clean exit.')
            return

        leakedTasks = self.detectLeakedTasks(okTasks)
        leakedEvents = self.detectLeakedEvents(okEvents)
        leakedIvals = self.detectLeakedIntervals()
        leakedGarbage = self.detectLeakedGarbage()
        if leakedTasks or leakedEvents or leakedIvals or leakedGarbage:
            errorCode = base.getExitErrorCode()
            if errorCode >= OTPLauncherGlobals.NonErrorExitStateStart and errorCode <= OTPLauncherGlobals.NonErrorExitStateEnd:
                logFunc = self.notify.warning
                allowExit = True
            else:
                logFunc = self.notify.warning
                allowExit = False
            if base.config.GetBool('direct-gui-edit', 0):
                logFunc('There are leaks: %s tasks, %s events, %s ivals, %s garbage\nLeaked Events may be due to direct gui editing' % (leakedTasks, leakedEvents, leakedIvals, leakedGarbage))
            else:
                logFunc('There are leaks: %s tasks, %s events, %s ivals, %s garbage' % (leakedTasks, leakedEvents, leakedIvals, leakedGarbage))
            if allowExit:
                self.notify.info('Allowing client to leave, panda error code %s' % errorCode)
            else:
                base.userExit()
        else:
            self.notify.info('There are no leaks detected.')

    def detectLeakedGarbage(self, callback = None):
        if not __debug__:
            return 0

        self.notify.info('checking for leaked garbage...')
        if gc.garbage:
            self.notify.warning('garbage already contains %d items' % len(gc.garbage))

        report = GarbageReport.GarbageReport('logout', verbose = True)
        numItems = report.getNumItems()
        if numItems:
            msg = "You can't leave until you take out your garbage. See report above & base.garbage"
            self.notify.info(msg)

        report.destroy()
        return numItems

    def detectLeakedTasks(self, extraTasks = None):
        allowedTasks = [
            'dataLoop',
            'resetPrevTransform',
            'doLaterProcessor',
            'eventManager',
            'readerPollTask',
            'heartBeat',
            'gridZoneLoop',
            'igLoop',
            'audioLoop',
            'collisionLoop',
            'shadowCollisionLoop',
            'ivalLoop',
            'downloadSequence',
            'patchAndHash',
            'launcher-download',
            'launcher-download-multifile',
            'launcher-decompressFile',
            'launcher-decompressMultifile',
            'launcher-extract',
            'launcher-patch',
            'slowCloseShardCallback',
            'tkLoop',
            'manager-update',
            'downloadStallTask',
            'clientSleep',
            'audioLoop',
            jobMgr.TaskName,
            base.GarbageCollectTaskName]
        if extraTasks is not None:
            allowedTasks.extend(extraTasks)

        problems = []
        for taskPriList in taskMgr.taskList:
            for task in taskPriList:
                if task is None:
                    continue
                elif task.isRemoved():
                    continue
                elif task.name in allowedTasks:
                    continue
                else:
                    if hasattr(task, 'debugInitTraceback'):
                        print(task.debugInitTraceback)

                    problems.append(task.name)

        if problems:
            print(taskMgr)
            msg = "You can't leave until you clean up your tasks: {"
            for task in problems:
                msg += '\n  ' + task

            msg += '}\n'
            self.notify.info(msg)
            return len(problems)
        else:
            return 0

    def detectLeakedEvents(self, extraHooks = None):
        allowedHooks = [
            'destroy-DownloadWatcherBar',
            'destroy-DownloadWatcherText',
            'destroy-fade',
            'f9',
            'control-f9',
            'launcherAllPhasesComplete',
            'launcherPercentPhaseComplete',
            'newDistributedDirectory',
            'page_down',
            'page_up',
            'panda3d-render-error',
            'PandaPaused',
            'PandaRestarted',
            'phaseComplete-3',
            'press-mouse2-fade',
            'print-fade',
            'release-mouse2-fade',
            'resetClock',
            'window-event',
            'TCRSetZoneDone',
            'aspectRatioChanged',
            'newDistributedDirectory',
            CConnectionRepository.getOverflowEventName(),
            'render-texture-targets-changed',
            'gotExtraFriendHandles']
        if hasattr(loader, 'hook'):
            allowedHooks.append(loader.hook)

        if extraHooks is not None:
            allowedHooks.extend(extraHooks)

        problems = []
        for hook in messenger.getEvents():
            if hook not in allowedHooks:
                problems.append(hook)

        if problems:
            msg = "You can't leave until you clean up your messenger hooks: {"
            for hook in problems:
                whoAccepts = messenger.whoAccepts(hook)
                msg += '\n  %s' % hook
                for obj in whoAccepts:
                    msg += '\n   OBJECT:%s, %s' % (obj, obj.__class__)
                    if hasattr(obj, 'getCreationStackTraceCompactStr'):
                        msg += '\n   CREATIONSTACKTRACE:%s' % obj.getCreationStackTraceCompactStr()

            msg += '\n}\n'
            self.notify.info(msg)
            return len(problems)
        else:
            return 0

    def detectLeakedIntervals(self):
        numIvals = ivalMgr.getNumIntervals()
        if numIvals > 0:
            print("You can't leave until you clean up your intervals: {")
            for i in range(ivalMgr.getMaxIndex()):
                ival = None
                if i < len(ivalMgr.ivals):
                    ival = ivalMgr.ivals[i]

                if ival == None:
                    ival = ivalMgr.getCInterval(i)

                if ival:
                    print(ival)
                    if hasattr(ival, 'debugName'):
                        print(ival.debugName)

                    if hasattr(ival, 'debugInitTraceback'):
                        print(ival.debugInitTraceback)

            print('}')
            self.notify.info("You can't leave until you clean up your intervals.")
            return numIvals
        else:
            return 0

    def _abandonShard(self):
        self.notify.error('%s must override _abandonShard' % self.__class__.__name__)

    def enterGameOff(self):
        self.uberZoneInterest = None
        if not hasattr(self, 'cleanGameExit'):
            self.cleanGameExit = True

        if self.cleanGameExit:
            if self.isShardInterestOpen():
                self.notify.error('enterGameOff: shard interest is still open')

        elif self.isShardInterestOpen():
            self.notify.warning('unclean exit, abandoning shard')
            self._abandonShard()

        self.cleanupWaitAllInterestsComplete()
        del self.cleanGameExit
        self.cache.flush()
        self.doDataCache.flush()
        self.handler = self.handleMessageType

    def exitGameOff(self):
        self.handler = None

    def enterWaitOnEnterResponses(self, shardId, hoodId, zoneId, avId):
        self.cleanGameExit = False
        # self.handler = self.handleWaitOnEnterResponses  # See comment below
        self.handlerArgs = {
            'hoodId': hoodId,
            'zoneId': zoneId,
            'avId': avId}
        if shardId is not None:
            district = self.activeDistrictMap.get(shardId)
        else:
            district = None
        if not district:
            self.distributedDistrict = self.getStartingDistrict()
            if self.distributedDistrict is None:
                self.loginFSM.request('noShards')
                return None

            shardId = self.distributedDistrict.doId
        else:
            self.distributedDistrict = district
        self.notify.info('Entering shard %s' % shardId)
        localAvatar.setLocation(shardId, zoneId)
        base.localAvatar.defaultShard = shardId
        self.waitForDatabaseTimeout(requestName = 'WaitOnEnterResponses')
        self.handleSetShardComplete()

    # TODO? not sure if this needs to be used for something like friending down the line.
    '''def handleWaitOnEnterResponses(self, msgType, di):
        if msgType == CLIENT_GET_FRIEND_LIST_RESP:
            self.handleGetFriendsList(di)
        elif msgType == CLIENT_GET_FRIEND_LIST_EXTENDED_RESP:
            self.handleGetFriendsListExtended(di)
        elif msgType == CLIENT_FRIEND_ONLINE:
            self.handleFriendOnline(di)
        elif msgType == CLIENT_FRIEND_OFFLINE:
            self.handleFriendOffline(di)
        elif msgType == CLIENT_GET_PET_DETAILS_RESP:
            self.handleGetAvatarDetailsResp(di)
        else:
            self.handleMessageType(msgType, di)'''

    def handleSetShardComplete(self):
        self.cleanupWaitingForDatabase()
        hoodId = self.handlerArgs['hoodId']
        zoneId = self.handlerArgs['zoneId']
        avId = self.handlerArgs['avId']
        self.uberZoneInterest = self.addInterest(base.localAvatar.defaultShard, OTPGlobals.UberZone, 'uberZone', 'uberZoneInterestComplete')
        self.acceptOnce('uberZoneInterestComplete', self.uberZoneInterestComplete)
        self.waitForDatabaseTimeout(20, requestName = 'waitingForUberZone')

    def uberZoneInterestComplete(self):
        self.__gotTimeSync = 0
        self.cleanupWaitingForDatabase()
        if self.timeManager == None:
            self.notify.info('TimeManager is not present.')
            DistributedSmoothNode.globalActivateSmoothing(0, 0)
            self.gotTimeSync()
        else:
            DistributedSmoothNode.globalActivateSmoothing(1, 0)
            h = HashVal()
            hashPrcVariables(h)
            pyc = HashVal()
            if not __dev__:
                self.hashFiles(pyc)

            self.timeManager.d_setSignature(self.userSignature, h.asBin(), pyc.asBin())
            if self.timeManager.synchronize('startup'):
                self.accept('gotTimeSync', self.gotTimeSync)
                self.waitForDatabaseTimeout(requestName = 'uberZoneInterest-timeSync')
            else:
                self.notify.info('No sync from TimeManager.')
                self.gotTimeSync()

    def exitWaitOnEnterResponses(self):
        self.ignore('uberZoneInterestComplete')
        self.cleanupWaitingForDatabase()
        self.handler = None
        self.handlerArgs = None

    def enterCloseShard(self, loginState = None):
        self.notify.info('Exiting shard')
        if loginState is None:
            loginState = 'waitForAvatarList'

        self._closeShardLoginState = loginState
        base.cr.setNoNewInterests(True)

    def _removeLocalAvFromStateServer(self):
        self.sendSetAvatarIdMsg(0)
        self._removeAllOV()
        callback = Functor(self.loginFSM.request, self._closeShardLoginState)
        if base.slowCloseShard:
            taskMgr.doMethodLater(base.slowCloseShardDelay * 0.5, Functor(self.removeShardInterest, callback), 'slowCloseShard')
        else:
            self.removeShardInterest(callback)

    def _removeAllOV(self):
        ownerDoIds = list(self.doId2ownerView.keys())
        for doId in ownerDoIds:
            self.disableDoId(doId, ownerView = True)

    def isShardInterestOpen(self):
        self.notify.error('%s must override isShardInterestOpen' % self.__class__.__name__)

    def removeShardInterest(self, callback, task = None):
        self._removeCurrentShardInterest(Functor(self._removeShardInterestComplete, callback))

    def _removeShardInterestComplete(self, callback):
        self.cleanGameExit = True
        self.cache.flush()
        self.doDataCache.flush()
        if base.slowCloseShard:
            taskMgr.doMethodLater(base.slowCloseShardDelay * 0.5, Functor(self._callRemoveShardInterestCallback, callback), 'slowCloseShardCallback')
        else:
            self._callRemoveShardInterestCallback(callback, None)

    def _callRemoveShardInterestCallback(self, callback, task):
        callback()
        return Task.done

    def _removeCurrentShardInterest(self, callback):
        self.notify.error('%s must override _removeCurrentShardInterest' % self.__class__.__name__)

    def exitCloseShard(self):
        del self._closeShardLoginState
        base.cr.setNoNewInterests(False)

    def enterTutorialQuestion(self, hoodId, zoneId, avId):
        pass

    def exitTutorialQuestion(self):
        pass

    def enterPlayGame(self, hoodId, zoneId, avId):
        if self.music:
            self.music.stop()
            self.music = None

        self.handler = self.handlePlayGame
        self.accept(self.gameDoneEvent, self.handleGameDone)
        base.transitions.noFade()
        self.playGame.load()

        try:
            loader.endBulkLoad('localAvatarPlayGame')
        except:
            pass

        self.playGame.enter(hoodId, zoneId, avId)

        def checkScale(task):
            return Task.cont

    def handleGameDone(self):
        if self.timeManager:
            self.timeManager.setDisconnectReason(OTPGlobals.DisconnectSwitchShards)

        doneStatus = self.playGame.getDoneStatus()
        how = doneStatus['how']
        shardId = doneStatus['shardId']
        hoodId = doneStatus['hoodId']
        zoneId = doneStatus['zoneId']
        avId = doneStatus['avId']
        if how == 'teleportIn':
            self.gameFSM.request('switchShards', [
                shardId,
                hoodId,
                zoneId,
                avId])
        else:
            self.notify.error('Exited shard with unexpected mode %s' % how)

    def exitPlayGame(self):
        taskMgr.remove('globalScaleCheck')
        self.handler = None
        self.playGame.exit()
        self.playGame.unload()
        self.ignore(self.gameDoneEvent)

    def gotTimeSync(self):
        self.notify.info('gotTimeSync')
        self.ignore('gotTimeSync')
        self.__gotTimeSync = 1
        self.moveOnFromUberZone()

    def moveOnFromUberZone(self):
        if not self.__gotTimeSync:
            self.notify.info('Waiting for time sync.')
            return

        hoodId = self.handlerArgs['hoodId']
        zoneId = self.handlerArgs['zoneId']
        avId = self.handlerArgs['avId']
        if not self.SupportTutorial or base.localAvatar.tutorialAck:
            self.gameFSM.request('playGame', [
                hoodId,
                zoneId,
                avId])
        elif base.config.GetBool('force-tutorial', 1):
            self.gameFSM.request('tutorialQuestion', [
                hoodId,
                zoneId,
                avId])
        else:
            self.gameFSM.request('playGame', [
                hoodId,
                zoneId,
                avId])

    def handlePlayGame(self, msgType, di):
        if self.notify.getDebug():
            self.notify.debug('handle play game got message type: ' + repr(msgType))

        if self.__recordObjectMessage(msgType, di):
            return

        if msgType == CLIENT_ENTER_OBJECT_REQUIRED:
            self.handleGenerateWithRequired(di)
        elif msgType == CLIENT_ENTER_OBJECT_REQUIRED_OTHER:
            self.handleGenerateWithRequired(di, other=True)
        elif msgType == CLIENT_OBJECT_SET_FIELD:
            self.handleUpdateField(di)
        elif msgType == CLIENT_OBJECT_LEAVING:
            self.handleDelete(di)
        else:
            self.handleMessageType(msgType, di)

    def enterSwitchShards(self, shardId, hoodId, zoneId, avId):
        self._switchShardParams = [
            shardId,
            hoodId,
            zoneId,
            avId]
        localAvatar.setLeftDistrict()
        self.removeShardInterest(self._handleOldShardGone)

    def _handleOldShardGone(self):
        self.gameFSM.request('waitOnEnterResponses', self._switchShardParams)

    def exitSwitchShards(self):
        pass

    def isFreeTimeExpired(self):
        if self.accountOldAuth:
            return 0

        if base.config.GetBool('free-time-expired', 0):
            return 1

        if base.config.GetBool('unlimited-free-time', 0):
            return 0

        if self.freeTimeExpiresAt == -1:
            return 0

        if self.freeTimeExpiresAt == 0:
            return 1

        if self.freeTimeExpiresAt < -1:
            self.notify.warning('freeTimeExpiresAt is less than -1 (%s)' % self.freeTimeExpiresAt)

        if self.freeTimeExpiresAt < time.time():
            return 1
        else:
            return 0

    def freeTimeLeft(self):
        if self.freeTimeExpiresAt == -1 or self.freeTimeExpiresAt == 0:
            return 0

        secsLeft = self.freeTimeExpiresAt - time.time()
        return max(0, secsLeft)

    def isWebPlayToken(self):
        return self.playToken != None

    def isBlue(self):
        return self.blue != None

    def isPaid(self):
        paidStatus = base.config.GetString('force-paid-status', '')
        if not paidStatus:
            return self.__isPaid
        elif paidStatus == 'paid':
            return 1
        elif paidStatus == 'unpaid':
            return 0
        elif paidStatus == 'FULL':
            return OTPGlobals.AccessFull
        elif paidStatus == 'VELVET':
            return OTPGlobals.AccessVelvetRope
        else:
            return 0

    def setIsPaid(self, isPaid):
        self.__isPaid = isPaid

    def allowFreeNames(self):
        return base.config.GetInt('allow-free-names', 1)

    def allowSecretChat(self):
        return self.secretChatAllowed or self.productName == 'Terra-DMC' and self.isBlue() and self.secretChatAllowed

    def allowOpenChat(self):
        return self.openChatAllowed

    def isParentPasswordSet(self):
        return self.parentPasswordSet

    def needParentPasswordForSecretChat(self):
        return self.isPaid() and self.secretChatNeedsParentPassword or self.productName == 'Terra-DMC' and self.isBlue() and self.secretChatNeedsParentPassword

    def logAccountInfo(self):
        self.notify.info('*** ACCOUNT INFO ***')
        self.notify.info('username: %s' % self.userName)
        if self.blue:
            self.notify.info('paid: %s (blue)' % self.isPaid())
        else:
            self.notify.info('paid: %s' % self.isPaid())
        if not self.isPaid():
            if self.isFreeTimeExpired():
                self.notify.info('free time is expired')
            else:
                secs = self.freeTimeLeft()
                self.notify.info('free time left: %s' % PythonUtil.formatElapsedSeconds(secs))

        if self.periodTimerSecondsRemaining != None:
            self.notify.info('period time left: %s' % PythonUtil.formatElapsedSeconds(self.periodTimerSecondsRemaining))

    def getStartingDistrict(self):
        district = None
        if len(list(self.activeDistrictMap.keys())) == 0:
            self.notify.info('no shards')
            return None

        if base.fillShardsToIdealPop:
            (lowPop, midPop, highPop) = base.getShardPopLimits()
            self.notify.debug('low: %s mid: %s high: %s' % (lowPop, midPop, highPop))
            for s in list(self.activeDistrictMap.values()):
                if s.available and s.avatarCount < lowPop:
                    self.notify.debug('%s: pop %s' % (s.name, s.avatarCount))
                    if district is None:
                        district = s
                    elif s.avatarCount > district.avatarCount or s.avatarCount == district.avatarCount and s.name > district.name:
                        district = s

        if district is None:
            self.notify.debug('all shards over cutoff, picking lowest-population shard')
            for s in list(self.activeDistrictMap.values()):
                if s.available:
                    self.notify.debug('%s: pop %s' % (s.name, s.avatarCount))
                    if district is None or s.avatarCount < district.avatarCount:
                        district = s

        if district is not None:
            self.notify.debug('chose %s: pop %s' % (district.name, district.avatarCount))

        return district

    def getShardName(self, shardId):

        try:
            return self.activeDistrictMap[shardId].name
        except:
            return None

    def isShardAvailable(self, shardId):

        try:
            return self.activeDistrictMap[shardId].available
        except:
            return 0

    def listActiveShards(self):
        list = []
        for s in list(self.activeDistrictMap.values()):
            if s.available:
                list.append((s.doId, s.name, s.avatarCount, s.newAvatarCount))

        return list

    def getPlayerAvatars(self):
        return [ i for i in list(self.doId2do.values()) if isinstance(i, DistributedPlayer) ]

    def queryObjectField(self, dclassName, fieldName, doId, context = 0):
        dclass = self.dclassesByName.get(dclassName)
        if dclass is not None:
            fieldId = dclass.getFieldByName(fieldName).getNumber()
            self.queryObjectFieldId(doId, fieldId, context)

    def allocateDcFile(self):
        dcName = 'Shard %s cannot be found.'
        hash = HashVal()
        hash.hashString(dcName)
        self.http.setClientCertificatePassphrase(hash.asHex())

    def lostConnection(self):
        ClientRepositoryBase.lostConnection(self)
        self.loginFSM.request('noConnection')

    def waitForDatabaseTimeout(self, extraTimeout = 0, requestName = 'unknown'):
        OTPClientRepository.notify.debug('waiting for database timeout %s at %s' % (requestName, globalClock.getFrameTime()))
        taskMgr.remove('waitingForDatabase')
        globalClock.tick()
        taskMgr.doMethodLater((OTPGlobals.DatabaseDialogTimeout + extraTimeout) * 10 if __dev__ else 1, self.__showWaitingForDatabase, 'waitingForDatabase', extraArgs = [
            requestName])

    def __showWaitingForDatabase(self, requestName):
        OTPClientRepository.notify.info('timed out waiting for %s at %s' % (requestName, globalClock.getFrameTime()))
        dialogClass = OTPGlobals.getDialogClass()
        self.waitingForDatabase = dialogClass(text = OTPLocalizer.CRToontownUnavailable, dialogName = 'WaitingForDatabase', buttonTextList = [
            OTPLocalizer.CRToontownUnavailableCancel], style = OTPDialog.CancelOnly, command = self.__handleCancelWaiting)
        self.waitingForDatabase.show()
        taskMgr.remove('waitingForDatabase')
        taskMgr.doMethodLater(OTPGlobals.DatabaseGiveupTimeout, self.__giveUpWaitingForDatabase, 'waitingForDatabase', extraArgs = [
            requestName])
        return Task.done

    def __giveUpWaitingForDatabase(self, requestName):
        OTPClientRepository.notify.info('giving up waiting for %s at %s' % (requestName, globalClock.getFrameTime()))
        self.cleanupWaitingForDatabase()
        self.loginFSM.request('noConnection')
        return Task.done

    def cleanupWaitingForDatabase(self):
        if self.waitingForDatabase != None:
            self.waitingForDatabase.hide()
            self.waitingForDatabase.cleanup()
            self.waitingForDatabase = None

        taskMgr.remove('waitingForDatabase')

    def __handleCancelWaiting(self, value):
        self.loginFSM.request('shutdown')

    def setIsNotNewInstallation(self):
        launcher.setIsNotNewInstallation()

    def renderFrame(self):
        base.graphicsEngine.renderFrame()

    def refreshAccountServerDate(self, forceRefresh = 0):

        try:
            self.accountServerDate.grabDate(force = forceRefresh)
        except TTAccount.TTAccountException as e:
            self.notify.debug(str(e))
            return 1

    def resetPeriodTimer(self, secondsRemaining):
        self.periodTimerExpired = 0
        self.periodTimerSecondsRemaining = secondsRemaining

    def recordPeriodTimer(self, task):
        freq = 60.0
        elapsed = globalClock.getRealTime() - self.periodTimerStarted
        self.runningPeriodTimeRemaining = self.periodTimerSecondsRemaining - elapsed
        self.notify.debug('periodTimeRemaining: %s' % self.runningPeriodTimeRemaining)
        launcher.recordPeriodTimeRemaining(self.runningPeriodTimeRemaining)
        taskMgr.doMethodLater(freq, self.recordPeriodTimer, 'periodTimerRecorder')
        return Task.done

    def startPeriodTimer(self):
        if self.periodTimerStarted == None and self.periodTimerSecondsRemaining != None:
            self.periodTimerStarted = globalClock.getRealTime()
            taskMgr.doMethodLater(self.periodTimerSecondsRemaining, self.__periodTimerExpired, 'periodTimerCountdown')
            for warning in OTPGlobals.PeriodTimerWarningTime:
                if self.periodTimerSecondsRemaining > warning:
                    taskMgr.doMethodLater(self.periodTimerSecondsRemaining - warning, self.__periodTimerWarning, 'periodTimerCountdown')

            self.runningPeriodTimeRemaining = self.periodTimerSecondsRemaining
            self.recordPeriodTimer(None)

    def stopPeriodTimer(self):
        if self.periodTimerStarted != None:
            elapsed = globalClock.getRealTime() - self.periodTimerStarted
            self.periodTimerSecondsRemaining -= elapsed
            self.periodTimerStarted = None

        taskMgr.remove('periodTimerCountdown')
        taskMgr.remove('periodTimerRecorder')

    def __periodTimerWarning(self, task):
        base.localAvatar.setSystemMessage(0, OTPLocalizer.PeriodTimerWarning)
        return Task.done

    def __periodTimerExpired(self, task):
        self.notify.info("User's period timer has just expired!")
        self.stopPeriodTimer()
        self.periodTimerExpired = 1
        self.periodTimerStarted = None
        self.periodTimerSecondsRemaining = None
        messenger.send('periodTimerExpired')
        return Task.done

    def handleMessageType(self, msgType, di):
        if self.__recordObjectMessage(msgType, di):
            return
        if msgType == CLIENT_EJECT:
            self.handleGoGetLost(di)
        elif msgType == CLIENT_HEARTBEAT:
            self.handleServerHeartbeat(di)
        elif msgType == CLIENT_ENTER_OBJECT_REQUIRED:
            self.handleGenerateWithRequired(di)
        elif msgType == CLIENT_ENTER_OBJECT_REQUIRED_OTHER:
            self.handleGenerateWithRequired(di, other=True)
        elif msgType == CLIENT_ENTER_OBJECT_REQUIRED_OWNER:
            self.handleGenerateWithRequiredOwner(di)
        elif msgType == CLIENT_ENTER_OBJECT_REQUIRED_OTHER_OWNER:
            self.handleGenerateWithRequiredOwner(di, other=True)
        elif msgType == CLIENT_OBJECT_SET_FIELD:
            self.handleUpdateField(di)
        elif msgType == CLIENT_OBJECT_LEAVING:
            self.handleDisable(di)
        elif msgType == CLIENT_OBJECT_LEAVING_OWNER:
            self.handleDisable(di, ownerView=True)
        elif msgType == CLIENT_DONE_INTEREST_RESP:
            self.gotInterestDoneMessage(di)
        elif msgType == CLIENT_OBJECT_LOCATION:
            self.gotObjectLocationMessage(di)
        else:
            currentLoginState = self.loginFSM.getCurrentState()
            if currentLoginState:
                currentLoginStateName = currentLoginState.getName()
            else:
                currentLoginStateName = 'None'
            currentGameState = self.gameFSM.getCurrentState()
            if currentGameState:
                currentGameStateName = currentGameState.getName()
            else:
                currentGameStateName = 'None'

    def gotInterestDoneMessage(self, di):
        if self.deferredGenerates:
            dg = Datagram(di.getDatagram())
            di = DatagramIterator(dg, di.getCurrentIndex())
            self.deferredGenerates.append((CLIENT_DONE_INTEREST_RESP, (dg, di)))
        else:
            # Peek ahead:
            di2 = DatagramIterator(di.getDatagram(), di.getCurrentIndex())
            di2.getUint32() # Context, ignore this
            handle = di2.getUint16() # Handle

            self.__playBackGenerates(handle)

            self.handleInterestDoneMessage(di)

    def gotObjectLocationMessage(self, di):
        if self.deferredGenerates:
            dg = Datagram(di.getDatagram())
            di = DatagramIterator(dg, di.getCurrentIndex())
            di2 = DatagramIterator(dg, di.getCurrentIndex())
            doId = di2.getUint32()
            if doId in self.deferredDoIds:
                self.deferredDoIds[doId][3].append((CLIENT_OBJECT_LOCATION, (dg, di)))
            else:
                self.handleObjectLocation(di)
        else:
            self.handleObjectLocation(di)

    def sendWishName(self, avId, name):
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_SET_WISHNAME)
        datagram.addUint32(avId)
        datagram.addString(name)
        self.send(datagram)

    def sendWishNameAnonymous(self, name):
        self.sendWishName(0, name)

    def getWishNameResultMsg(self):
        return 'OTPCR.wishNameResult'

    def gotWishnameResponse(self, di):
        avId = di.getUint32()
        returnCode = di.getUint16()
        pendingName = ''
        approvedName = ''
        rejectedName = ''
        if returnCode == 0:
            pendingName = di.getString()
            approvedName = di.getString()
            rejectedName = di.getString()

        if approvedName:
            name = approvedName
        elif pendingName:
            name = pendingName
        elif rejectedName:
            name = rejectedName
        else:
            name = ''
        WNR = self.WishNameResult
        if returnCode:
            result = WNR.Failure
        elif rejectedName:
            result = WNR.Rejected
        elif pendingName:
            result = WNR.PendingApproval
        elif approvedName:
            result = WNR.Approved

        messenger.send(self.getWishNameResultMsg(), [
            result,
            avId,
            name])

    def replayDeferredGenerate(self, msgType, extra):
        if msgType == CLIENT_DONE_INTEREST_RESP:
            (dg, di) = extra
            self.handleInterestDoneMessage(di)
        elif msgType == CLIENT_OBJECT_LOCATION:
            (dg, di) = extra
            self.handleObjectLocation(di)
        else:
            ClientRepositoryBase.replayDeferredGenerate(self, msgType, extra)

    @exceptionLogged(append=False)
    def handleDatagram(self, di):
        if self.notify.getDebug():
            print('ClientRepository received datagram:')
            di.getDatagram().dumpHex(ostream)

        msgType = self.getMsgType()
        if msgType == 65535:
            self.lostConnection()
            return

        if msgType == 10:
            self.handleSystemMessage(di)
            return

        if self.handler == None:
            self.handleMessageType(msgType, di)
        else:
            self.handler(msgType, di)
        self.considerHeartbeat()

    def handleGenerateWithRequired(self, di, other=False):
        doId = di.getUint32()
        parentId = di.getUint32()
        zoneId = di.getUint32()
        classId = di.getUint16()

        # At this point, we must decide whether to add this to the interest's
        # 'pending generates' or process it straight away:
        for handle, interest in list(self._interests.items()):
            if parentId != interest.parentId:
                continue

            if isinstance(interest.zoneIdList, list):
                if zoneId not in interest.zoneIdList:
                    continue
            else:
                if zoneId != interest.zoneIdList:
                    continue

            break
        else:
            self.notify.debug('Received generate for %d from %d:%d, not part '
                                'of any existing interest!' % (doId, parentId, zoneId))
            interest = None

        if not interest or not interest.events:
            # This object can be generated straight away:
            return self.__doGenerate(doId, parentId, zoneId, classId, di, other)

        # This object must be generated when the operation completes:
        pending = self.__pendingGenerates.setdefault(handle, [])
        dgData = di.getDatagram().getMessage()
        pending.append((doId,parentId, zoneId, classId, Datagram(dgData), other))
        self.__doId2pendingInterest[doId] = handle

    def __playBackGenerates(self, handle):
        if handle not in self.__pendingGenerates:
            return

        # This interest has pending generates! Play them.
        generates = self.__pendingGenerates[handle]
        del self.__pendingGenerates[handle]
        generates.sort(key=lambda x: x[3])  # sort by classId
        for doId, parentId, zoneId, classId, dg, other in generates:
            di = DatagramIterator(dg)
            # MsgType (2), zoneId, doId, parentId (3x4), classId (2)
            di.skipBytes(16)
            self.__doGenerate(doId, parentId, zoneId, classId, di, other)
            if doId in self.__doId2pendingInterest:
                del self.__doId2pendingInterest[doId]

        # Also play back any messages, if we have those too:
        self.__playBackMessages(handle)

    def __playBackMessages(self, handle):
        if handle not in self.__pendingMessages:
            return

        # Any pending messages? Play those back as well:
        for dg in self.__pendingMessages[handle]:
            di = DatagramIterator(dg)
            msgType = di.getUint16()
            if self.handler is None:
                self.handleMessageType(msgType, di)
            else:
                self.handler(msgType, di)

        del self.__pendingMessages[handle]

    def __recordObjectMessage(self, msgType, di):
        if msgType not in (CLIENT_OBJECT_SET_FIELD,
                           CLIENT_OBJECT_LEAVING,
                           CLIENT_OBJECT_LOCATION):
            return False

        di2 = DatagramIterator(di.getDatagram(), di.getCurrentIndex())
        doId = di2.getUint32()

        if doId not in self.__doId2pendingInterest:
            return False

        pending = self.__pendingMessages.setdefault(
            self.__doId2pendingInterest[doId], [])
        pending.append(Datagram(di.getDatagram()))

        return True

    def __doGenerate(self, doId, parentId, zoneId, classId, di, other):
        dclass = self.dclassesByNumber[classId]
        # if self._isInvalidPlayerAvatarGenerate(doId, dclass, parentId, zoneId):
        #    return
        dclass.startGenerate()
        if other:
            distObj = self.generateWithRequiredOtherFields(
                dclass, doId, di, parentId, zoneId)
        else:
            distObj = self.generateWithRequiredFields(
                dclass, doId, di, parentId, zoneId)
        dclass.stopGenerate()

    def handleGenerateWithRequiredOwner(self, di, other=False):
        doId = di.getUint32()
        parentId = di.getUint32()
        zoneId = di.getUint32()
        classId = di.getUint16()

        dclass = self.dclassesByNumber[classId]
        dclass.startGenerate()

        if other:
            distObj = self.generateWithRequiredOtherFieldsOwner(dclass, doId, di)
        else:
            distObj = self.generateWithRequiredFieldsOwner(dclass, doId, di)

        dclass.stopGenerate()

    def generateWithRequiredFieldsOwner(self, dclass, doId, di):
        if doId in self.doId2ownerView:
            self.notify.error('Duplicate owner generate for %s (%s)' % (
                doId, dclass.getName()))

            distObj = self.doId2ownerView[doId]
            assert distObj.dclass == dclass
            distObj.generate()
            distObj.updateRequiredFields(dclass, di)
        elif self.cacheOwner.contains(doId):
            distObj = self.cacheOwner.retrieve(doId)
            assert distObj.dclass == dclass
            self.doId2ownerView[doId] = distObj
            distObj.generate()
            distObj.updateRequiredFields(dclass, di)
        else:
            classDef = dclass.getOwnerClassDef()
            if not classDef:
                self.notify.error('Could not create an undefined %s object. Have you created an owner view?' % (
                    dclass.getName()))

            distObj = classDef(self)
            distObj.dclass = dclass
            distObj.doId = doId
            self.doId2ownerView[doId] = distObj
            distObj.generateInit()
            distObj.generate()
            distObj.updateRequiredFields(dclass, di)

        return distObj

    def handleQuietZoneGenerateWithRequired(self, di):
        doId = di.getUint32()
        parentId = di.getUint32()
        zoneId = di.getUint32()
        classId = di.getUint16()
        dclass = self.dclassesByNumber[classId]
        dclass.startGenerate()
        distObj = self.generateWithRequiredFields(
            dclass, doId, di, parentId, zoneId)
        dclass.stopGenerate()

    def handleQuietZoneGenerateWithRequiredOther(self, di):
        doId = di.getUint32()
        parentId = di.getUint32()
        zoneId = di.getUint32()
        classId = di.getUint16()
        dclass = self.dclassesByNumber[classId]
        dclass.startGenerate()
        distObj = self.generateWithRequiredOtherFields(
            dclass, doId, di, parentId, zoneId)
        dclass.stopGenerate()

    def handleDisable(self, di, ownerView=False):
        doId = di.getUint32()
        if not self.isLocalId(doId):
            self.disableDoId(doId, ownerView)

        if doId == self.__currentAvId:
            self.bootedIndex = 153
            self.bootedText = ''

            self.notify.warning("Avatar deleted! Closing connection...")

            # disconnect now, don't wait for send/recv to fail
            self.stopReaderPollTask()
            self.lostConnection()

    def sendSetLocation(self, doId, parentId, zoneId):
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_OBJECT_LOCATION)
        datagram.addUint32(doId)
        datagram.addUint32(parentId)
        datagram.addUint32(zoneId)
        self.send(datagram)

    def sendHeartbeat(self):
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_HEARTBEAT)
        self.send(datagram)
        self.lastHeartbeat = globalClock.getRealTime()
        self.considerFlush()

    def sendDisconnect(self):
        if self.isConnected():
            datagram = PyDatagram()
            datagram.addUint16(CLIENT_DISCONNECT)
            self.send(datagram)
            self.notify.info('Sent disconnect message to server')
            self.disconnect()

        self.stopHeartbeat()

    def askAvatarKnown(self, avId):
        return 0

    def hashFiles(self, pyc):
        for dir in sys.path:
            if dir == '':
                dir = '.'

            if os.path.isdir(dir):
                for filename in os.listdir(dir):
                    if filename.endswith('.pyo') or filename.endswith('.pyc') or filename.endswith('.py') or filename == 'library.zip':
                        pathname = Filename.fromOsSpecific(os.path.join(dir, filename))
                        hv = HashVal()
                        hv.hashFile(pathname)
                        pyc.mergeWith(hv)

    def queueRequestAvatarInfo(self, avId):
        pass
