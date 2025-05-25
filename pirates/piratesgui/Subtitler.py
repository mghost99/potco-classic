from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.showbase import DirectObject
from direct.interval.IntervalGlobal import *
from pirates.piratesbase import PLocalizer
from pirates.piratesgui import PiratesGuiGlobals
from pirates.piratesbase import PiratesGlobals
from pirates.piratesgui.GuiButton import GuiButton
from pirates.piratesgui.DialogButton import DialogButton

class Subtitler(DirectObject.DirectObject):
    
    def __init__(self):
        DirectObject.DirectObject.__init__(self)
        self.event = None
        self.sfx = None
        self.text = DirectLabel(parent = render2d, relief = None, text = '', text_align = TextNode.ACenter, text_scale = 0.055, text_fg = PiratesGuiGlobals.TextFG2, text_shadow = PiratesGuiGlobals.TextShadow, textMayChange = 1, text_font = PiratesGlobals.getPirateFont(), pos = (0, 0, -0.9), sortOrder = 80)
        self.confirmButton = DialogButton(parent = base.a2dBottomRight, pos = (-0.15, 0, 0.095), text = PLocalizer.MakeAPirateNext, text_scale = 0.05, text_pos = (0.04, -0.018), text_fg = PiratesGuiGlobals.TextFG2, textMayChange = 1, command = self.advancePageNumber, sortOrder = 90, buttonStyle = DialogButton.YES)
        base.transitions.loadLetterbox()
        self.text.setScale(aspect2d, 1)
        self.accept('aspectRatioChanged', self.text.setScale, [
            aspect2d,
            1])
        self.text.hide()
        self.confirmButton.hide()
        self.fader = None
        self.subtitleParent = render2d.attachNewNode(PGTop('subtitleParent'))
        self.subtitleParent.node().setMouseWatcher(base.mouseWatcherNode)
        self.__chatPageNumber = None
        self.__chatPages = None
        self.__chatMessage = None
        self.__chatPages = []
        self.__optionButtons = []
        self.clearTextOverride = False
    
    def destroy(self):
        self.ignoreAll()
        if self.fader:
            self.fader.finish()
            self.fader = None
        
        if self.sfx:
            self.sfx.stop()
            self.sfx = None
        
        self.text.destroy()
        del self.text
        self.confirmButton.destroy()
        del self.confirmButton
        self.subtitleParent.removeNode()
        self.__destroyOptionButtons()
        taskMgr.remove('clearSubtitleTask')
    
    def clearText(self, resetOverride = False):
        if resetOverride:
            self.clearTextOverride = False
        
        if self.clearTextOverride:
            return
        
        taskMgr.remove('clearSubtitleTask')
        self.event = None
        self.text['text'] = ''
        self.text['text_fg'] = PiratesGuiGlobals.TextFG2
        self.text.hide()
        self.confirmButton.hide()
        if self.sfx:
            self.sfx.stop()
            self.sfx = None
        
        self.ignore('enter')
        self.ignore('mouse1')
        self.ignore('letterboxOff')
        self.__clearChatMessage()
        self.__destroyOptionButtons()
        self.__optionButtons = []
    
    def __processChatMessage(self, message):
        self.__chatPages = message.split('\x07')
        self.__chatMessage = message
        self.__chatSet = 0
        self.__chatPageNumber = 0

    def __clearChatMessage(self):
        self.__chatPageNumber = None
        self.__chatPages = None
        self.__chatMessage = None
        self.__chatPages = []
    
    def setPageChat(self, message, timeout = False, confirm = False, options = None, callback = None, extraArgs = []):
        if options != None:
            self.__loadOptionButtons(options, callback, extraArgs)
        
        self.__processChatMessage(message)
        self.__updatePageChat(timeout, confirm)

    def __loadOptionButtons(self, options, callback, extraArgs):
        
        def optionCallback(*args):
            self.advancePageNumber()
            callback(*args)

        for i in range(len(options)):
            optionButton = GuiButton(parent = base.a2dBottomRight,
                                     pos = (-0.15 - (len(options) - 1 - i) * 0.25, 0, 0.095),
                                     text = str(options[i]),
                                     text_pos = (0, -0.0125),
                                     text_scale = 0.05,
                                     text_fg = PiratesGuiGlobals.TextFG2,
                                     textMayChange = 1,
                                     command = optionCallback,
                                     extraArgs = [options[i]] + extraArgs,
                                     sortOrder = 90
                                     )
            optionButton.hide()
            self.__optionButtons.append(optionButton)

    def __destroyOptionButtons(self):
        for optionButton in self.__optionButtons:
            optionButton.destroy()
            del optionButton
        
        self.__optionButtons = None

    def __updatePageChat(self, timeout = False, confirm = False):
        if self.__chatPageNumber >= 0:
            message = self.__chatPages[self.__chatPageNumber]
            self.showText(message, timeout = timeout, confirm = confirm)

    def getNumChatPages(self):
        if self.__chatPageNumber != None:
            return len(self.__chatPages)
        
        return 0

    def advancePageNumber(self):
        if self.__chatPageNumber != None:
            if self.__chatPageNumber >= 0:
                self.__chatPageNumber += 1
                if self.__chatPageNumber >= len(self.__chatPages):
                    self.__chatPageNumber = -1
                
                self.__updatePageChat()
                if self.__chatPageNumber >= 0:
                    messenger.send('nextChatPage', [self.__chatPageNumber, 0])
                else:
                    messenger.send('doneChatPage', [0])
                    self.confirmCallback()

    def showText(self, text, color = None, sfx = None, timeout = 0, confirm = False):
        taskMgr.remove('clearSubtitleTask')
        self.text['text'] = text
        self.text.show()
        self.accept('letterboxOff', self.clearText)
        if self.getNumChatPages() > 1 or self.__optionButtons or confirm:
            self.confirmButton.show()
            if self.__chatPageNumber == len(self.__chatPages) - 1:
                messenger.send('lastSubtitlePage')
                if self.__optionButtons:
                    for optionButton in self.__optionButtons:
                        optionButton.show()
                    
                    self.confirmButton.hide()
                else:
                    self.confirmButton['text'] = PLocalizer.GenericConfirmOK
            else:
                self.confirmButton['text'] = PLocalizer.GenericConfirmNext
        else:
            self.confirmButton.hide()
        self.event = None
        if color:
            self.text['text_fg'] = color
        
        if sfx:
            if self.sfx:
                self.sfx.stop()
            
            self.sfx = sfx
            base.playSfx(sfx)
        
        if timeout:
            taskMgr.doMethodLater(timeout, self.clearText, 'clearSubtitleTask', extraArgs = [
                True])

    def fadeInText(self, text, color = None, sfx = None):
        self.text['text'] = text
        self.text.show()
        self.confirmButton.hide()
        self.event = None
        if sfx:
            if self.sfx:
                self.sfx.stop()
            
            self.sfx = sfx
            base.playSfx(sfx)
        
        if self.fader:
            self.fader.finish()
            self.fader = None
        
        if color:
            self.text['text_fg'] = color
        
        self.fader = LerpFunctionInterval(self.text.setAlphaScale, fromData = 0, toData = 1, duration = 1.0)
        self.fader.start()
    
    def fadeOutText(self):
        self.event = None
        self.confirmButton.hide()
        if self.sfx:
            self.sfx.stop()
            self.sfx = None
        
        self.ignore('enter')
        self.ignore('mouse1')
        if self.fader:
            self.fader.finish()
            self.fader = None
        
        fadeOut = LerpFunctionInterval(self.text.setAlphaScale, fromData = 1, toData = 0, duration = 1.0)
        
        def restoreColor():
            self.text['text_fg'] = PiratesGuiGlobals.TextFG2

        def resetPos():
            self.text.setPos(Vec3(0.0, 0.0, 0.0))

        self.fader = Sequence(fadeOut, Func(self.text.hide), Func(restoreColor), Func(resetPos))
        self.fader.start()

    def confirmText(self, text, event, color = None, sfx = None):
        self.text['text'] = text
        if color:
            self.text['text_fg'] = color
        
        self.text.show()
        self.confirmButton.show()
        self.event = event
        if sfx:
            if self.sfx:
                self.sfx.stop()
            
            self.sfx = sfx
            base.playSfx(sfx)
        
        self.confirmButton['command'] = self.confirmCallback

    def confirmCallback(self):
        if self.event:
            messenger.send(self.event)
            self.event = None
        
        self.clearText()
        self.confirmButton['command'] = self.advancePageNumber


