from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.task.Task import Task
from direct.fsm import ClassicFSM
from direct.fsm import State
from direct.directnotify import DirectNotifyGlobal
from otp.otpbase import OTPLocalizer
from otp.otpbase import OTPGlobals
from otp.uberdog.RejectCode import RejectCode
from pirates.piratesbase import PiratesGlobals
from pirates.piratesbase import PLocalizer
from pirates.piratesgui import GuiPanel
from pirates.piratesgui import PiratesGuiGlobals
from pirates.battle.DistributedBattleNPC import DistributedBattleNPC
from pirates.piratesgui.RequestButton import RequestButton

class GuildInviterButton(RequestButton):
    
    def __init__(self, text, command):
        RequestButton.__init__(self, text, command)
        self.initialiseoptions(GuildInviterButton)



class GuildInviter(GuiPanel.GuiPanel):
    notify = DirectNotifyGlobal.directNotify.newCategory('GuildInviter')
    
    def __init__(self, avId, avName):
        GuiPanel.GuiPanel.__init__(self, 'Guild Invite', 0.5, 0.5)
        self.initialiseoptions(GuildInviter)
        self.setPos(0.15, 0, 0.25)
        self.avId = avId
        self.avName = avName
        self.avDisableName = 'disable-%s' % avId
        self.fsm = ClassicFSM.ClassicFSM('GuildInviter', [
            State.State('off',
                        self.enterOff,
                        self.exitOff),
            State.State('getStarted',
                        self.enterGetNewGuild,
                        self.exitGetNewGuild),
            State.State('begin',
                        self.enterBegin,
                        self.exitBegin),
            State.State('tooMany',
                        self.enterTooMany,
                        self.exitTooMany),
            State.State('notYet',
                        self.enterNotYet,
                        self.exitNotYet),
            State.State('checkAvailability',
                        self.enterCheckAvailability,
                        self.exitCheckAvailability),
            State.State('notAvailable',
                        self.enterNotAvailable,
                        self.exitNotAvailable),
            State.State('notAcceptingGuilds',
                        self.enterNotAcceptingGuilds,
                        self.exitNotAcceptingGuilds),
            State.State('wentAway',
                        self.enterWentAway,
                        self.exitWentAway),
            State.State('busy',
                        self.enterBusy,
                        self.exitBusy),
            State.State('alreadyInGuild',
                        self.enterAlreadyInGuild,
                        self.exitAlreadyInGuild),
            State.State('guildFull',
                        self.enterGuildFull,
                        self.exitGuildFull),
            State.State('alreadyInvited',
                        self.enterAlreadyInvited,
                        self.exitAlreadyInvited),
            State.State('askingNPC',
                        self.enterAskingNPC,
                        self.exitAskingNPC),
            State.State('endGuildship',
                        self.enterEndGuildship,
                        self.exitEndGuildship),
            State.State('guildNoMore',
                        self.enterGuildsNoMore,
                        self.exitGuildsNoMore),
            State.State('self',
                        self.enterSelf,
                        self.exitSelf),
            State.State('ignored',
                        self.enterIgnored,
                        self.exitIgnored),
            State.State('asking',
                        self.enterAsking,
                        self.exitAsking),
            State.State('yes',
                        self.enterYes,
                        self.exitYes),
            State.State('no',
                        self.enterNo,
                        self.exitNo),
            State.State('otherTooMany',
                        self.enterOtherTooMany,
                        self.exitOtherTooMany),
            State.State('maybe',
                        self.enterMaybe,
                        self.exitMaybe),
            State.State('down',
                        self.enterDown,
                        self.exitDown),
            State.State('cancel',
                        self.enterCancel,
                        self.exitCancel)], 'off', 'off')
        self.message = DirectLabel(parent = self,
                                   relief = None,
                                   text = '',
                                   text_scale = PiratesGuiGlobals.TextScaleLarge,
                                   text_align = TextNode.ACenter,
                                   text_fg = PiratesGuiGlobals.TextFG2,
                                   text_shadow = PiratesGuiGlobals.TextShadow,
                                   text_wordwrap = 11,
                                   pos = (0.25, 0, 0.35),
                                   textMayChange = 1)
        self.context = None
        self.bOk = GuildInviterButton(text = OTPLocalizer.GuildInviterOK, command = self.__handleOk)
        self.bOk.reparentTo(self)
        self.bOk.setPos(0.2, 0, 0.05)
        self.bOk.hide()
        self.bCancel = GuildInviterButton(text = OTPLocalizer.GuildInviterCancel, command = self.__handleCancel)
        self.bCancel.reparentTo(self)
        self.bCancel.setPos(0.2, 0, 0.05)
        self.bCancel.hide()
        self.bYes = GuildInviterButton(text = OTPLocalizer.GuildInviterYes, command = self.__handleYes)
        self.bYes.reparentTo(self)
        self.bYes.setPos(0.1, 0, 0.05)
        self.bYes.hide()
        self.bNo = GuildInviterButton(text = OTPLocalizer.GuildInviterNo, command = self.__handleNo)
        self.bNo.reparentTo(self)
        self.bNo.setPos(0.3, 0, 0.05)
        self.bNo.hide()
        self.fsm.enterInitialState()
        if self.avId == None:
            self.fsm.request('getStarted')
        else:
            self.fsm.request('begin')

    def destroy(self):
        self.ignoreAll()
        if hasattr(self, 'destroyed'):
            return
        
        self.destroyed = 1
        self.fsm.request('cancel')
        del self.fsm
        GuiPanel.GuiPanel.destroy(self)

    def enterOff(self):
        pass

    def exitOff(self):
        pass
    
    def enterGetNewGuild(self):
        self.message['text'] = OTPLocalizer.GuildInviterClickToon
        self.bCancel.show()
        self.accept('clickedNametag', self.__handleClickedNametag)

    def exitGetNewGuild(self):
        self.bCancel.hide()
        self.ignore('clickedNametag')

    def __handleClickedNametag(self, avatar):
        self.avId = avatar.doId
        self.avName = avatar.getName()
        self.avDisableName = avatar.uniqueName('disable')
        self.fsm.request('begin')
    
    def enterBegin(self):
        myId = base.localAvatar.doId
        self.accept(self.avDisableName, self.__handleDisableAvatar)
        if self.avId == myId:
            self.fsm.request('self')
        
        handle = base.cr.identifyAvatar(self.avId)
        if not handle:
            self.fsm.request('wentAway')
            return
        
        self.fsm.request('notYet')
    
    def exitBegin(self):
        self.ignore(self.avDisableName)
    
    def enterTooMany(self):
        self.message['text'] = OTPLocalizer.GuildInviterTooMany % self.avName
        self['text_pos'] = (0.0, 0.2)
        self.bCancel.show()
        self.bCancel.setPos(0.0, 0.0, -0.16)

    def exitTooMany(self):
        self.bCancel.hide()
    
    def enterNotYet(self):
        self.accept(self.avDisableName, self.__handleDisableAvatar)
        self.message['text'] = OTPLocalizer.GuildInviterNotYet % self.avName
        self.bYes.show()
        self.bNo.show()

    def exitNotYet(self):
        self.ignore(self.avDisableName)
        self.bYes.hide()
        self.bNo.hide()
    
    def enterCheckAvailability(self):
        self.accept(self.avDisableName, self.__handleDisableAvatar)
        handle = base.cr.identifyAvatar(self.avId)
        if not handle:
            self.fsm.request('wentAway')
            return
        
        if isinstance(handle, DistributedBattleNPC):
            self.fsm.request('askingNPC')
            return
        
        self.fsm.request('asking')
        self.message['text'] = OTPLocalizer.GuildInviterCheckAvailability % self.avName
        base.cr.guildManager.sendRequestInvite(self.avId)
        self.bCancel.show()

    def __joinedGuild(self, avId, info):
        if self.avId == avId:
            self.fsm.request('yes')

    def exitCheckAvailability(self):
        self.ignore(self.avDisableName)
        self.bCancel.hide()

    def enterNotAvailable(self):
        self.message['text'] = OTPLocalizer.GuildInviterNotAvailable % self.avName
        self.context = None
        self.bOk.show()
    
    def exitNotAvailable(self):
        self.bOk.hide()

    def enterNotAcceptingGuilds(self):
        self.message['text'] = OTPLocalizer.GuildInviterGuildSaidNo % self.avName
        self.context = None
        self.bOk.show()
    
    def exitNotAcceptingGuilds(self):
        self.bOk.hide()

    def enterWentAway(self):
        self.message['text'] = OTPLocalizer.GuildInviterWentAway % self.avName
        if self.context != None:
            self.context = None
        
        self.bOk.show()
    
    def exitWentAway(self):
        self.bOk.hide()

    def enterGuildFull(self):
        self.message['text'] = OTPLocalizer.GuildInviterTooFull
        self['text_pos'] = (0.0, 0.2)
        self.context = None
        self.bCancel.show()
    
    def exitGuildFull(self):
        self.message['text'] = ''
        self['text_pos'] = (0.0, 0.13)
        self.bCancel.hide()

    def enterBusy(self):
        self.message['text'] = OTPLocalizer.GuildInviterBusy % self.avName
        self['text_pos'] = (0.0, 0.2)
        self.context = None
        self.bCancel.show()
    
    def exitBusy(self):
        self.message['text'] = ''
        self['text_pos'] = (0.0, 0.13)
        self.bCancel.hide()
    
    def enterAlreadyInGuild(self):
        self.message['text'] = OTPLocalizer.GuildInviterAlready % self.avName
        self['text_pos'] = (0.0, 0.2)
        self.context = None
        self.bCancel.show()
    
    def exitAlreadyInGuild(self):
        self.message['text'] = ''
        self['text_pos'] = (0.0, 0.13)
        self.bCancel.hide()
    
    def enterAlreadyInvited(self):
        self.message['text'] = OTPLocalizer.GuildInviterAlreadyInvited % self.avName
        self['text_pos'] = (0.0, 0.2)
        self.context = None
        self.bCancel.show()

    def exitAlreadyInvited(self):
        self.message['text'] = ''
        self['text_pos'] = (0.0, 0.13)
        self.bCancel.hide()

    def enterAskingNPC(self):
        self.message['text'] = PLocalizer.GuildInviterAskingNPC % self.avName
        taskMgr.doMethodLater(2.0, self.npcReplies, 'npcGuildship')
        self.bCancel.show()
    
    def exitAskingNPC(self):
        taskMgr.remove('npcGuildship')
        self.bCancel.hide()

    def npcReplies(self, task):
        self.fsm.request('no')
        return Task.done
    
    def enterEndGuildship(self):
        self.message['text'] = OTPLocalizer.GuildInviterEndGuildship % self.avName
        self.context = None
        self.bYes.show()
        self.bNo.show()

    def exitEndGuildship(self):
        self.bYes.hide()
        self.bNo.hide()
    
    def enterGuildsNoMore(self):
        base.cr.avatarGuildsManager.sendRequestRemove(self.avId)
        self.message['text'] = OTPLocalizer.GuildInviterGuildsNoMore % self.avName
        self.bOk.show()
        if not base.cr.identifyAvatar(self.avId):
            messenger.send(self.avDisableName)
    
    def exitGuildsNoMore(self):
        self.bOk.hide()
    
    def enterSelf(self):
        self.message['text'] = OTPLocalizer.GuildInviterSelf
        self.context = None
        self.bOk.show()

    def exitSelf(self):
        self.bOk.hide()
    
    def enterIgnored(self):
        self.message['text'] = OTPLocalizer.GuildInviterIgnored % self.avName
        self.context = None
        self.bOk.show()
    
    def exitIgnored(self):
        self.bOk.hide()

    def enterAsking(self):
        self.accept(self.avDisableName, self.__handleDisableAvatar)
        self.message['text'] = OTPLocalizer.GuildInviterAsking % self.avName
        self.accept(OTPGlobals.GuildAcceptInviteEvent, self.__handleGuildAcceptInvite)
        self.accept(OTPGlobals.GuildRejectInviteEvent, self.__handleGuildRejectInvite)
        self.bCancel.show()
    
    def exitAsking(self):
        self.ignore(self.avDisableName)
        self.ignore(OTPGlobals.GuildAcceptInviteEvent)
        self.ignore(OTPGlobals.GuildRejectInviteEvent)
        self.bCancel.hide()
    
    def enterYes(self):
        self.message['text'] = OTPLocalizer.GuildInviterGuildSaidYes % self.avName
        messenger.send('AvatarChange')
        self.context = None
        self.bOk.show()

    def exitYes(self):
        self.bOk.hide()
    
    def enterNo(self):
        self.message['text'] = OTPLocalizer.GuildInviterGuildSaidNo % self.avName
        self.context = None
        self.bCancel.hide()
        self.bOk.setPos(0.2, 0, 0.05)
        self.bOk.show()
    
    def exitNo(self):
        self.bOk.hide()
    
    def enterOtherTooMany(self):
        self.message['text'] = OTPLocalizer.GuildInviterTooMany % self.avName
        self.context = None
        self.bOk.show()

    def exitOtherTooMany(self):
        self.bOk.hide()
    
    def enterMaybe(self):
        self.message['text'] = OTPLocalizer.GuildInviterMaybe % self.avName
        self.context = None
        self.bOk.show()
    
    def exitMaybe(self):
        self.bOk.hide()

    def enterDown(self):
        self.message['text'] = OTPLocalizer.GuildInviterDown
        self.context = None
        self.bOk.show()

    def exitDown(self):
        self.bOk.hide()
    
    def enterCancel(self):
        if self.context != None:
            self.context = None
        
        self.fsm.request('off')

    def exitCancel(self):
        pass

    def __handleOk(self):
        self.destroy()

    def __handleCancel(self):
        self.destroy()

    def __handleYes(self):
        if self.fsm.getCurrentState().getName() == 'notYet':
            self.fsm.request('checkAvailability')
        elif self.fsm.getCurrentState().getName() == 'endGuildship':
            self.fsm.request('guildNoMore')
        else:
            self.destroy()
    
    def __handleNo(self):
        self.destroy()

    def __handleList(self):
        messenger.send('openGuildsList')

    def __guildConsidering(self, yesNoAlready, context):
        if yesNoAlready == 1:
            self.context = context
            self.fsm.request('asking')
        elif yesNoAlready == 0:
            self.fsm.request('notAvailable')
        elif yesNoAlready == 2:
            self.fsm.request('alreadyInGuild')
        elif yesNoAlready == 3:
            self.fsm.request('self')
        elif yesNoAlready == 4:
            self.fsm.request('ignored')
        elif yesNoAlready == 6:
            self.fsm.request('notAcceptingGuilds')
        elif yesNoAlready == 10:
            self.fsm.request('no')
        elif yesNoAlready == 13:
            self.fsm.request('otherTooMany')
        else:
            self.notify.warning('Got unexpected response to friendConsidering: %s' % yesNoAlready)
            self.fsm.request('maybe')

    def __handleGuildAcceptInvite(self, avId):
        print('Received accept invite event on inviter')
        self.fsm.request('yes')
    
    def __handleGuildRejectInvite(self, avId, reason):
        if reason == RejectCode.INVITEE_NOT_ONLINE:
            self.fsm.request('notAvailable')
        elif reason == RejectCode.BUSY:
            self.fsm.request('busy')
        elif reason == RejectCode.ALREADY_IN_GUILD:
            self.fsm.request('alreadyInGuild')
        elif reason == RejectCode.GUILD_FULL:
            self.fsm.request('guildFull')
        elif reason == RejectCode.NO_GUILD:
            self.fsm.request('no')
        else:
            self.notify.warning('guildRejectInvite: %s unknown reason: %s.' % (avId, reason))

    def __handleDisableAvatar(self):
        self.fsm.request('wentAway')


