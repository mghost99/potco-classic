from direct.showbase.DirectObject import DirectObject
from direct.directnotify import DirectNotifyGlobal
from direct.gui import DirectGuiGlobals
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.fsm import FSM
from direct.fsm import StateData
from direct.fsm.ClassicFSM import ClassicFSM
from direct.fsm.State import State
from direct.task import Task
from direct.interval.IntervalGlobal import *
from direct.distributed import PyDatagram
from otp.distributed import PotentialAvatar
from otp.otpgui import OTPDialog
from otp.otpbase import OTPGlobals
from pirates.piratesgui import PDialog
from pirates.pirate import Pirate
from pirates.pirate import LocalPirate
from pirates.pirate import Human
from pirates.pirate import HumanDNA
from pirates.npc import Skeleton
from pirates.piratesbase import PiratesGlobals
from pirates.piratesbase import PLocalizer
from pirates.piratesbase import UserFunnel
from pirates.pirate import DynamicHuman
from pirates.effects import DynamicLight
from .MakeAPirateGlobals import *
import random
from . import PirateMale
from . import PirateFemale
from . import GenderGUI
from . import BodyGUI
from . import HeadGUI
from . import ClothesGUI
from . import HairGUI
from . import TattooGUI
from . import JewelryGUI
from . import NameGUI
from . import NPCGUI
from .CharGuiBase import CharGuiSlider
MakeAPiratePageIcons = {
    'Body': 'chargui_body',
    'Head': 'chargui_head',
    'Mouth': 'chargui_mouth',
    'Eyes': 'chargui_eyes',
    'Nose': 'chargui_nose',
    'Ear': 'chargui_ears',
    'Hair': 'chargui_hair',
    'Clothes': 'chargui_cloth',
    'Name': 'chargui_name',
    'Tattoos': 'chargui_name',
    'Jewelry': 'chargui_head'}
heightBiasArray = {
  'm': [0.2, 0, 0, 0, -1.0],
  'f': [0, 0.7, 0.2, -.5, 0.2],
  'n': [0.2, 0, 0, 0, -1.0],
  's': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}
CamInitPosHprs = [
  [
    [
      Vec3(-2.2, 17.4, 8.5), Vec3(-2.0 + 180.0, -15.8, -1.2)
    ],
    [Vec3(-2.2, 17.4, 8.5), Vec3(-2.0 + 180.0, -15.8, -1.2)],
    [Vec3(-2.2, 17.4, 8.5), Vec3(-2.0 + 180.0, -15.8, -1.2)],
    [Vec3(-2.2, 17.4, 8.5), Vec3(-2.0 + 180.0, -15.8, -1.2)],
    [Vec3(-2.2, 17.4, 8.5), Vec3(-2.0 + 180.0, -15.8, -1.2)]
  ],
  [
    [Vec3(-2.2, 17.4, 8.5), Vec3(-2.0 + 180.0, -15.8, -1.2)],
    [Vec3(-2.2, 17.4, 8.5), Vec3(-2.0 + 180.0, -15.8, -1.2)],
    [Vec3(-2.2, 17.4, 8.5), Vec3(-2.0 + 180.0, -15.8, -1.2)],
    [Vec3(-2.2, 17.4, 8.5), Vec3(-2.0 + 180.0, -15.8, -1.2)],
    [Vec3(-2.2, 17.4, 8.5), Vec3(-2.0 + 180.0, -15.8, -1.2)]
  ]
]
CamZoomInPosHprs = [
  [
    [
      Vec3(0.0, 3.5, 5.4), Vec3(-6.2 + 180.0, -13.1, -2.4)
    ],
    [Vec3(0.03, 3, 6.3), Vec3(-5.0 + 180.0, -16.5, -2.1)],
    [Vec3(0, 4, 7), Vec3(-5.0 + 180.0, -16.5, -2.1)],
    [Vec3(-.15, 3.9, 6.3), Vec3(-3.3 + 180.0, -11.1, -1.9)],
    [Vec3(0.15, 4.7, 7.5), Vec3(-7.2 + 180.0, -14.9, -2.8)]
  ],
  [
    [Vec3(-0.5, 4, 5.3), Vec3(-6.2 + 180.0, -13.1, -2.4)],
    [Vec3(-0.4, 3.2, 6), Vec3(-6.2 + 180.0, -13.1, -2.4)],
    [Vec3(-0.5, 3.4, 6.1), Vec3(-3.8 + 180.0, -9.1, -2.6)],
    [Vec3(-0.6, 3.6, 6.5), Vec3(-3.3 + 180.0, -11.1, -1.9)],
    [Vec3(-0.5, 3.4, 6), Vec3(-3.8 + 180.0, -9.1, -2.6)]
  ]
]
CamZoomOutPosHprs = [
  [
    [
      Vec3(-3, 20.5, 9.2), Vec3(-0.3 + 180.0, -15.7, -0.8)
    ],
    [Vec3(-3, 20.5, 9.2), Vec3(-0.3 + 180.0, -15.7, -0.8)],
    [Vec3(-3, 20.5, 9.2), Vec3(-0.3 + 180.0, -15.7, -0.8)],
    [Vec3(-3, 20.5, 9.2), Vec3(-0.3 + 180.0, -15.7, -0.8)],
    [Vec3(-3, 20.5, 9.2), Vec3(-0.3 + 180.0, -15.7, -0.8)]
  ],
  [
    [Vec3(-3, 20.5, 9.2), Vec3(-0.3 + 180.0, -15.7, -0.8)],
    [Vec3(-3, 20.5, 9.2), Vec3(-0.3 + 180.0, -15.7, -0.8)],
    [Vec3(-3, 20.5, 9.2), Vec3(-0.3 + 180.0, -15.7, -0.8)],
    [Vec3(-3, 20.5, 9.2), Vec3(-0.3 + 180.0, -15.7, -0.8)],
    [Vec3(-3, 20.5, 9.2), Vec3(-0.3 + 180.0, -15.7, -0.8)]
  ]
]


class MakeAPirate(DirectObject, StateData.StateData, FSM.FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory('MakeAPirate')

    def __init__(self,
                 avList,
                 doneEvent,
                 subId=0,
                 index=0,
                 isPaid=0,
                 isNPCEditor=False,
                 piratesEditor=None
                 ):

        AnimList.extend(AnimListA_B)
        AnimList.extend(AnimListC_G)
        AnimList.extend(AnimListI_Si)
        AnimList.extend(AnimListSl_Sz)
        AnimList.extend(AnimListT_Z)
        self.undoList = {'m': [HumanDNA.HumanDNA()], 'f': [HumanDNA.HumanDNA('f')], 'n': [HumanDNA.HumanDNA('n')]}
        self.guiIdStates = {}
        self.compositeAction = 0
        self.undoLevel = {'m': 0, 'f': 0, 'n': 0}
        FSM.FSM.__init__(self, 'MakeAPirate')
        self.avList = avList
        self.index = index
        self.subId = subId
        self.wantNPCViewer = base.config.GetBool('want-npc-viewer', 0)
        self.wantPicButtons = base.config.GetBool('want-gen-pics-buttons', 0)
        if self.wantPicButtons and not self.wantNPCViewer:
            self.wantNPCViewer = True
            self.notify.warning('Warning! want-gen-pics-buttons needs want-npc-viewer. wantNPCViewer overridden and set to TRUE')

        self.wantMarketingViewer = base.config.GetBool('want-marketing-viewer', 0)
        if isNPCEditor:
            self.wantNPCViewer = 1
        self.loadJackDialogs()
        self.skipTutorial = base.config.GetBool('skip-tutorial', 0)
        self.chooseFemale = base.config.GetBool('choose-female', 0)
        self.noJailLight = base.config.GetBool('no-jail-light', 0)
        if hasattr(base, 'pe') and base.pe:
            self.noJailLight = True
        if self.skipTutorial or isNPCEditor or self.avList[self.index] == None or self.avList[self.index] == OTPGlobals.AvatarSlotAvailable:
            self.isTutorial = 0
        else:
            self.isTutorial = 1
        self.isPaid = isPaid
        self.lowestPage = 0
        StateData.StateData.__init__(self, doneEvent)
        self.phase = 3
        self.isNPCEditor = isNPCEditor
        for key in PiratesGlobals.ScreenshotHotkeyList:
            self.accept(key, self.takeScreenShot)

        self.accept('f12', self.toggleGUI)
        self.accept('exitPlayPirates', self.handleCancel)
        self.newPotAv = None
        self.pirate = None
        self.skeleton = None
        self.confirmTempName = None
        self.pageNames = []
        self.pageTabs = []
        self.currPageTabIndex = None
        self.currPageIndex = None
        self.names = [
         '', '', '', '']
        self.dnastring = None
        self.entered = 0
        if not self.isTutorial and not self.isNPCEditor:
            self.initH = 180
        else:
            self.initH = 0
        self.lastRot = self.initH
        self.pirateHpr = Point3(self.initH, 0, 0)
        self.piratePos = Point3(0, 0, 0)
        self.leftTime = 1.6
        self.rightTime = 1
        self.slide = 0
        self.lastLOD = 0
        self.npcViewerLOD = -1
        self.lastAnim = 0
        self.aPos = None
        self.avatarType = 0
        if self.isNPCEditor:
            self.editorAvatar = self.avList[self.index]
            self.piratesEditor = piratesEditor
            self.loadNPC = True
            self.camAdjusted = False
            self.avatarDummyNode = render.attachNewNode('Avatar Dummy Node')
            self.avatarDummyNode.setPos(self.avList[self.index].getPos(render))
            rot = self.avList[self.index].getHpr()
            self.avatarDummyNode.setScale(self.avList[self.index].getScale())
            self.avatarDummyNode.setHpr(rot[0], rot[1], rot[2])
            camera.wrtReparentTo(self.avatarDummyNode)
        self.nameList = []
        self.shop = BODYSHOP
        self.shopsVisited = []
        self.music = None
        self.soundBack = None
        if not hasattr(base, 'wantJewelry'):
            self.wantJewelry = base.config.GetBool('want-jewelry', 0)
        else:
            self.wantJewelry = base.wantJewelry
        if self.wantNPCViewer:
            self.numShops = len(ShopNames)
        else:
            self.numShops = ShopNames.index('NameShop') + 1
        self.inRandomAll = False
        self.idleFSM = ClassicFSM('idleFSM', [
            State('default', self.enterIdleFSMDefault, self.exitIdleFSMDefault,
                  ['alt1', 'alt2']),
            State('alt1', self.enterIdleFSMAlt1, self.exitIdleFSMAlt1,
                  ['alt2', 'default']),
            State('alt2', self.enterIdleFSMAlt2, self.exitIdleFSMAlt2,
                  ['alt1', 'default'])
        ], 'default', 'default')
        self.idleFSM.enterInitialState()
    
    def getPirate(self):
        return self.pirate
    
    def enter(self):
        self.entered = 1
        if base.config.GetBool('want-alt-idles', 0):
            taskMgr.add(self.altIdleTask, 'avCreate-AltIdleTask')
        
        taskMgr.add(self.zoomTask, 'avCreate-ZoomTask')
        self._waitForServerDlg = None
        self.bookModel.show()
        self.lowBookModel.show()
        self.guiBottomBar.show()
        if self.skipTutorial and not self.isNPCEditor:
            self.jail = loader.loadModel('models/buildings/navy_jail_interior')
            self.jail.flattenMedium()
            self.jail.reparentTo(render)
            self.jail.setLightOff()
        
        if not self.noJailLight:
            self.pirate.setH(self.initH)
            self.pirate.setZ(-1.5)
            light = DynamicLight.DynamicLight(type=DynamicLight.DYN_LIGHT_AMBIENT, parent=render, pos=VBase3(37.912, 12.061, 0.944), hpr=VBase3(176.273, 5.678, -0.212))
            self.ambientLight = light
            newPos = light.getPos(self.pirate)
            newHpr = light.getHpr(self.pirate)
            light.setPos(newPos)
            light.setHpr(newHpr)
            light.turnOff()
            light.setIntensity(0.3182)
            light.setConeAngle(60.0)
            light.setDropOff(9.5455)
            light.turnOn()
            light = DynamicLight.DynamicLight(type=DynamicLight.DYN_LIGHT_SPOT, parent=render, pos=VBase3(12.358, 7.072, 12.536), hpr=VBase3(117.392, -35.256, -7.489))
            self.spotLight1 = light
            newPos = light.getPos(self.pirate)
            newHpr = light.getHpr(self.pirate)
            light.setPos(newPos)
            light.setHpr(newHpr)
            light.turnOff()
            light.setIntensity(0.4545)
            light.setConeAngle(77.0455)
            light.setDropOff(84.5455)
            light.turnOn()
            light = DynamicLight.DynamicLight(type=DynamicLight.DYN_LIGHT_SPOT, parent=render, pos=VBase3(-9.914, 10.93, 14.172), hpr=VBase3(-137.877, -34.676, -4.026))
            self.spotLight2 = light
            newPos = light.getPos(self.pirate)
            newHpr = light.getHpr(self.pirate)
            light.setPos(newPos)
            light.setHpr(newHpr)
            light.turnOff()
            light.setIntensity(1.0606)
            light.setConeAngle(78.6364)
            light.setDropOff(87.2727)
            light.turnOn()
            light = DynamicLight.DynamicLight(type=DynamicLight.DYN_LIGHT_SPOT, parent=render, pos=VBase3(7.156, -15.566, 9.971), hpr=VBase3(27.413, -20.551, -68.33))
            self.spotLight3 = light
            newPos = light.getPos(self.pirate)
            newHpr = light.getHpr(self.pirate)
            light.setPos(newPos)
            light.setHpr(newHpr)
            light.turnOff()
            light.setIntensity(0.2727)
            light.setConeAngle(56.3636)
            light.setDropOff(90.0)
            light.turnOn()
            self.pirate.setP(0)
            self.pirate.setZ(0)
        
        self.setupJackDialogs()
        base.camLens.setMinFov(PiratesGlobals.MakeAPirateCameraFov)
        self.placePirate()
        self.pirate.setNameVisible(0)
        self.guiCancelButton.show()
        if self.isNPCEditor or self.wantNPCViewer:
            self.guiTopBar.show()
            self.guiCancelButton.hide()
        
        self.guiBottomBar.show()
        self.request('BodyShop')
        if hasattr(base, 'musicMgr'):
            base.musicMgr.request('make-a-pirate', volume = 0.4)
        
        self.accept('mouse1', self._startMouseReadTask)
        self.accept('mouse1-up', self._stopMouseReadTask)
        self.accept('mouse3', self._startMouseReadTask)
        self.accept('mouse3-up', self._stopMouseReadTask)
        self.accept('wheel_up', self._handleWheelUp)
        self.accept('wheel_down', self._handleWheelDown)
        if self.isTutorial:
            self.offsetZoomPos = Vec3(-0.6, 4, 1.2)
        elif self.isNPCEditor:
            self.offsetZoomPos = Vec3(-0.6, 4, 1.2)
        else:
            self.offsetZoomPos = Vec3(0.6, -4, 1.2)
        if self.isNPCEditor:
            self.offsetZoomHpr = camera.getHpr(self.avatarDummyNode)
        else:
            self.offsetZoomHpr = camera.getHpr(render)
        base.transitions.fadeIn()
    
    def exit(self):
        taskMgr.remove('avCreate-ZoomTask')
        taskMgr.remove('avCreate-AltIdleTask')
        taskMgr.remove('avCreate-restoreIdle')
        taskMgr.remove('avCreate-altIdle')
        base.camLens.setMinFov(PiratesGlobals.DefaultCameraFov)
        if self._waitForServerDlg:
            self._waitForServerDlg.destroy()
            self._waitForServerDlg = None
        
        if self.confirmTempName:
            self.confirmTempName.destroy()
            self.confirmTempName = None
        
        self.bookModel.hide()
        self.lowBookModel.hide()
        if self.isNPCEditor or self.wantNPCViewer:
            self.guiTopBar.hide()
        
        self.guiBottomBar.hide()
        if self.skipTutorial:
            self.pirate.detachNode()
        
        self.pirate.setNameVisible(1)
        if self.skipTutorial and not self.isNPCEditor:
            if hasattr(self, 'jail'):
                self.jail.hide()
        
        if self.entered and not self.noJailLight:
            self.ambientLight.turnOff()
            self.spotLight1.turnOff()
            self.spotLight2.turnOff()
            self.spotLight3.turnOff()
        
        if hasattr(base, 'musicMgr'):
            base.musicMgr.requestFadeOut('make-a-pirate')
        
        self.ignore('mouse1')
        self.ignore('mouse1-up')
        self.ignore('mouse3')
        self.ignore('mouse3-up')
        self._stopMouseReadTask()
        self.ignore('wheel_up')
        self.ignore('wheel_down')
        self.entered = 0
        UserFunnel.logSubmit(1, 'CREATE_PIRATE_EXITS')
        UserFunnel.logSubmit(0, 'CREATE_PIRATE_EXITS')
        if not self.isNPCEditor:
            base.cr.centralLogger.writeClientEvent('CREATE_PIRATE_EXITS')
        
        UserFunnel.logSubmit(1, 'CUTSCENE_ONE_START')
        UserFunnel.logSubmit(0, 'CUTSCENE_ONE_START')
        if not self.isNPCEditor:
            base.cr.centralLogger.writeClientEvent('CUTSCENE_ONE_START')

    def loadJackDialogs(self):
        self.jsd_anytime_1 = base.loader.loadSfx('audio/jsd_anytime_1.mp3')
        self.jsd_anytime_2 = base.loader.loadSfx('audio/jsd_anytime_2.mp3')
        self.jsd_anytime_3 = base.loader.loadSfx('audio/jsd_anytime_3.mp3')
        self.jsd_anytime_4 = base.loader.loadSfx('audio/jsd_anytime_4.mp3')
        self.jsd_body_ms_1 = base.loader.loadSfx('audio/jsd_body_ms_1.mp3')
        self.jsd_body_ms_2 = base.loader.loadSfx('audio/jsd_body_ms_2.mp3')
        self.jsd_body_sf_1 = base.loader.loadSfx('audio/jsd_body_sf_1.mp3')
        self.jsd_body_sf_2 = base.loader.loadSfx('audio/jsd_body_sf_2.mp3')
        self.jsd_body_tm_1 = base.loader.loadSfx('audio/jsd_body_tm_1.mp3')
        self.jsd_body_tm_2 = base.loader.loadSfx('audio/jsd_body_tm_2.mp3')
        self.jsd_clothes_1 = base.loader.loadSfx('audio/jsd_clothes_1.mp3')
        self.jsd_clothes_5 = base.loader.loadSfx('audio/jsd_clothes_5.mp3')
        self.jsd_clothes_finish_1 = base.loader.loadSfx('audio/jsd_clothes_finish_1.mp3')
        self.jsd_clothes_finish_2 = base.loader.loadSfx('audio/jsd_clothes_finish_2.mp3')
        self.jsd_coat_good = base.loader.loadSfx('audio/jsd_coat_good.mp3')
        self.jsd_face_long = base.loader.loadSfx('audio/jsd_face_long.mp3')
        self.jsd_face_pretty = base.loader.loadSfx('audio/jsd_face_pretty.mp3')
        self.jsd_face_rogue = base.loader.loadSfx('audio/jsd_face_rogue.mp3')
        self.jsd_face_ugly = base.loader.loadSfx('audio/jsd_face_ugly.mp3')
        self.jsd_hair_lot = base.loader.loadSfx('audio/jsd_hair_lot.mp3')
        self.jsd_hair_mop = base.loader.loadSfx('audio/jsd_hair_mop.mp3')
        self.jsd_hat_good = base.loader.loadSfx('audio/jsd_hat_good.mp3')
        self.jsd_pant_good = base.loader.loadSfx('audio/jsd_pant_good.mp3')
        self.jsd_shoe_barbossa = base.loader.loadSfx('audio/jsd_shoe_barbossa.mp3')
        self.jsd_shoe_good = base.loader.loadSfx('audio/jsd_shoe_good.mp3')
        self.lastDialog = None
    
    def setupJackDialogs(self):
        self.JSD_ANYTIME = [
            [
                self.jsd_anytime_1,
                self.jsd_anytime_2,
                self.jsd_anytime_3,
                self.jsd_anytime_4,
                self.jsd_clothes_finish_2],
            [
                self.jsd_anytime_1,
                self.jsd_anytime_2,
                self.jsd_anytime_3,
                self.jsd_anytime_4,
                self.jsd_clothes_finish_2]]
        self.JSD_BODY = [
            [
                self.jsd_body_sf_1,
                self.jsd_body_sf_2],
            [
                self.jsd_body_ms_1,
                self.jsd_body_ms_2],
            [
                self.jsd_body_tm_1,
                self.jsd_body_tm_2],
            [
                self.jsd_body_tm_1,
                self.jsd_body_tm_2],
            [
                self.jsd_body_tm_1,
                self.jsd_body_tm_2]]
        self.JSD_FACE = [
            [
                self.jsd_face_long,
                self.jsd_face_ugly],
            [
                self.jsd_face_pretty,
                self.jsd_face_rogue]]
        self.JSD_HAIR = [
            [
                self.jsd_hair_lot,
                self.jsd_hair_mop],
            [
                self.jsd_hair_lot,
                self.jsd_hair_mop]]
        self.JSD_CLOTHING_INTRO = [
            [
                self.jsd_clothes_1,
                self.jsd_clothes_5,
                self.jsd_clothes_finish_1,
                self.jsd_clothes_finish_2],
            [
                self.jsd_clothes_1,
                self.jsd_clothes_5,
                self.jsd_clothes_finish_1,
                self.jsd_clothes_finish_2]]
        self.JSD_CLOTHING = {
            'm': {
                'HAT': [
                    self.jsd_hat_good],
                'SHIRT': [
                    None],
                'VEST': [
                    None],
                'COAT': [
                    self.jsd_coat_good],
                'PANT': [
                    self.jsd_pant_good],
                'BELT': [
                    None],
                'SHOE': [
                    self.jsd_shoe_barbossa,
                    self.jsd_shoe_good]},
            'f': {
                'HAT': [
                    self.jsd_hat_good],
                'SHIRT': [
                    None],
                'VEST': [
                    None],
                'COAT': [
                    self.jsd_coat_good],
                'PANT': [
                    self.jsd_pant_good],
                'BELT': [
                    None],
                'SHOE': [
                    self.jsd_shoe_barbossa,
                    self.jsd_shoe_good]}}

    def setupCamera(self, character):
        
        try:
            id = character.style.getBodyShape()
        except:
            if self.skeletonType > 4:
                id = 2
            else:
                id = 0

        lastRot = self.lastRot
        self.lastRot = self.initH
        self.rotatePirate()
        if self.isNPCEditor:
            self.camParent = self.avatarDummyNode
        else:
            self.camParent = render
        camera.wrtReparentTo(character)
        camera.setPos(CamInitPosHprs[self.genderIdx][id][0])
        self.camInitPos = camera.getPos(self.camParent)
        camera.setHpr(CamInitPosHprs[self.genderIdx][id][1])
        self.camInitHpr = camera.getHpr(self.camParent)
        camera.setPos(CamZoomOutPosHprs[self.genderIdx][id][0])
        self.camZoomOutPos = camera.getPos(self.camParent)
        camera.setHpr(CamZoomOutPosHprs[self.genderIdx][id][1])
        self.camZoomOutHpr = camera.getHpr(self.camParent)
        camera.wrtReparentTo(self.camParent)
        camera.setHpr(self.camInitHpr)
        camera.setPos(self.camInitPos)
        self.lastRot = lastRot
        self.rotatePirate()

    def placePirate(self):
        if self.pirate.style.gender == 'f':
            self.genderIdx = 1
        else:
            self.genderIdx = 0
        self.pirate.setHpr(self.initH, 0, 0)
        if hasattr(self, 'lastAnim') == False:
            self.lastAnim = 0
        
        if self.isNPCEditor:
            self.pirate.reparentTo(self.avatarDummyNode)
        else:
            self.pirate.reparentTo(render)
        self.aPos = self.pirate.getPos()
        self.pirate.loop(AnimList[self.lastAnim])
        if not self.isNPCEditor:
            self.setupCamera(self.pirate)
        else:
            
            try:
                id = self.pirate.style.getBodyShape()
            except:
                if self.skeletonType > 4:
                    id = 2
                else:
                    id = 0

            self.camInitPos = CamInitPosHprs[self.genderIdx][id][0]
            self.camInitHpr = CamInitPosHprs[self.genderIdx][id][1]
            self.camZoomInPos = CamZoomInPosHprs[self.genderIdx][id][0]
            self.camZoomInHpr = CamZoomInPosHprs[self.genderIdx][id][1]
            self.camZoomOutPos = CamZoomOutPosHprs[self.genderIdx][id][0]
            self.camZoomOutHpr = CamZoomOutPosHprs[self.genderIdx][id][1]
        if not self.isNPCEditor and not self.wantNPCViewer:
            self.pirate.enableBlend()
            self.pirate.loop('idle')
            self.pirate.loop('idle_centered')
        
        self.assignPirateToGui()

    def assignPirateToGui(self):
        self.genderGui.assignAvatar(self.pirate.model)
        self.bodyGui.assignAvatar(self.pirate.model)
        self.headGui.assignAvatar(self.pirate.model)
        self.clothesGui.assignAvatar(self.pirate.model)
        self.hairGui.assignAvatar(self.pirate.model)
        self.nameGui.assignAvatar(self.pirate.model)
        if self.wantNPCViewer:
            self.tattooGui.assignAvatar(self.pirate.model)
            self.jewelryGui.assignAvatar(self.pirate.model)
    
    def takeScreenShot(self):
        self.notify.info('Beginning screenshot capture')
        base.screenshot()
        self.notify.info('Screenshot captured')
    
    def assignSkeletonToGui(self):
        self.NPCGui.assignAvatar(self.skeleton.model)

    def placeSkeleton(self, type):
        self.skeleton.reparentTo(render)
        self.skeleton.setHpr(self.initH, 0, 0)
        if hasattr(self, 'lastAnim') == False:
            self.lastAnim = 0
        
        self.skeleton.loop(AnimList[self.lastAnim])
        self.pgsZoom['value'] = 0.0
        self.pgsRotate['value'] = 0.0
        self.aPos = self.skeleton.getPos()
        self.skeleton.setPos(0, 0, 0)
        if not self.isNPCEditor:
            self.setupCamera(self.skeleton)
        else:
            
            try:
                id = self.pirate.style.getBodyShape()
            except:
                if self.skeletonType > 4:
                    id = 2
                else:
                    id = 0

            self.camInitPos = CamInitPosHprs[self.genderIdx][id][0]
            self.camInitHpr = CamInitPosHprs[self.genderIdx][id][1]
            self.camZoomInPos = CamZoomInPosHprs[self.genderIdx][id][0]
            self.camZoomInHpr = CamZoomInPosHprs[self.genderIdx][id][1]
            self.camZoomOutPos = CamZoomOutPosHprs[self.genderIdx][id][0]
            self.camZoomOutHpr = CamZoomOutPosHprs[self.genderIdx][id][1]
        self.assignSkeletonToGui()

    def loadNPCButton(self):
        self.PirateButton = DirectButton(parent = self.guiTopBar, relief = DGG.SUNKEN, pos = (-0.7, 0.0, 0.0), scale = 0.6, command = self.handlePirate, frameSize = (-0.25, 0.25, -0.1, 0.1), borderWidth = (0.02, 0.02), text = PLocalizer.PirateButton, text_pos = (0, -0.05), text_scale = 0.2, text_align = TextNode.ACenter)
        self.NPCButton = DirectButton(parent = self.guiTopBar, relief = DGG.RAISED, pos = (-0.3, 0.0, 0.0), scale = 0.6, command = self.handleNPC, frameSize = (-0.25, 0.25, -0.1, 0.1), borderWidth = (0.02, 0.02), text = PLocalizer.NPCButton, text_pos = (0, -0.05), text_scale = 0.2, text_align = TextNode.ACenter)
        self.NavyButton = DirectButton(parent = self.guiTopBar, relief = DGG.RAISED, pos = (0.1, 0.0, 0.0), scale = 0.6, command = self.handleNavy, frameSize = (-0.25, 0.25, -0.1, 0.1), borderWidth = (0.02, 0.02), text = PLocalizer.NavyButton, text_pos = (0, -0.05), text_scale = 0.2, text_align = TextNode.ACenter)
    
    def load(self):
        self.charGui = loader.loadModelOnce('models/gui/char_gui')
        self.triangleGui = loader.loadModelOnce('models/gui/triangle')
        self.bookModel = DirectFrame(parent = base.a2dTopRight, image = self.charGui.find('**/chargui_base'), image_pos = (-0.13, 0, 0), relief = None, pos = (-0.65, 0, -0.8), scale = 0.42)
        self.bookModel.hide()
        self.lowBookModel = DirectFrame(parent = base.a2dBottomLeft, relief = None, frameSize = (-1, 1, -0.12, 0.12), frameColor = (0.5, 0.5, 0.5, 0.3), borderWidth = (0.025, 0.025), pos = (0.45, 0, 0.12), scale = (0.6, 1, 0.75))
        self.lowBookModel.hide()
        self.guiRandomAllButton = DirectButton(parent = self.bookModel, relief = None, image = (self.charGui.find('**/chargui_text_block_large'), self.charGui.find('**/chargui_text_block_large_down'), self.charGui.find('**/chargui_text_block_large_over')), image_scale = 1.5, scale = 0.7, pos = (-0.7, 0, -2.5), command = self.handleRandomAll, text = PLocalizer.ShuffleButton, text_font = PiratesGlobals.getInterfaceFont(), text_scale = 0.18, text_pos = (0, -0.025), text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1))
        self.prevShuffleButton = DirectButton(parent = self.bookModel, relief = None, image = (self.triangleGui.find('**/triangle'), self.triangleGui.find('**/triangle_down'), self.triangleGui.find('**/triangle_over')), scale = -0.2, pos = (-1.15, 0, -2.5), command = self.undo)
        self.prevShuffleButton['state'] = DGG.DISABLED
        self.nextShuffleButton = DirectButton(parent = self.bookModel, relief = None, image = (self.triangleGui.find('**/triangle'), self.triangleGui.find('**/triangle_down'), self.triangleGui.find('**/triangle_over')), scale = 0.2, pos = (-0.25, 0, -2.5), command = self.redo)
        self.nextShuffleButton['state'] = DGG.DISABLED
        self.guiRandomButton = DirectButton(parent = self.bookModel, relief = None, image = (self.charGui.find('**/chargui_text_block_large'), self.charGui.find('**/chargui_text_block_large_down'), self.charGui.find('**/chargui_text_block_large_over')), image_scale = 1.5, scale = 0.6, pos = (0, 0, -2.05), command = self.handleRandom, text = PLocalizer.RandomButton, text_font = PiratesGlobals.getInterfaceFont(), text_scale = 0.18, text_pos = (0, -0.025), text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1))
        self.guiNextButton = DirectButton(parent = self.bookModel, relief = None, image = (self.charGui.find('**/chargui_text_block_large'), self.charGui.find('**/chargui_text_block_large_down'), self.charGui.find('**/chargui_text_block_large_over')), image_scale = 1.5, scale = 0.7, pos = (0.7, 0, -2.5), command = self.handleNext, text = PLocalizer.MakeAPirateNext, text_scale = 0.18, text_pos = (0, -0.025), text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1))
        self.guiBottomBar = DirectFrame(parent = base.a2dBottomLeft, relief = None, frameSize = (-0.6, 0.6, -0.05, 0.05), frameColor = (0.5, 0.5, 0.5, 0.3), pos = (0.5, 0, 0.9))
        self.guiBottomBar.hide()
        self.guiCancelButton = DirectButton(parent = self.guiBottomBar, relief = None, image = (self.charGui.find('**/chargui_frame02'), self.charGui.find('**/chargui_frame02_down'), self.charGui.find('**/chargui_frame02_over')), scale = 0.3, pos = (-0.39, 0, 1.04), command = self.handleCancel, text = PLocalizer.MakeAPirateCancel, text_font = PiratesGlobals.getInterfaceFont(), text_scale = 0.18, text_pos = (0, -0.025), text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1))
        self.guiCancelButton.hide()
        self.guiSaveUndoButton = DirectButton(parent = self.guiBottomBar, relief = None, image = (self.charGui.find('**/chargui_frame02'), self.charGui.find('**/chargui_frame02_down'), self.charGui.find('**/chargui_frame02_over')), scale = 0.3, pos = (-0.1, 0, 1.04), command = self.storeUndo, text = 'save state', text_font = PiratesGlobals.getInterfaceFont(), text_scale = 0.18, text_pos = (0, -0.025), text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1))
        self.guiSaveUndoButton.hide()
        self.guiUndoButton = DirectButton(parent = self.bookModel, relief = None, image = (self.charGui.find('**/chargui_frame02'), self.charGui.find('**/chargui_frame02_down'), self.charGui.find('**/chargui_frame02_over')), scale = 0.7, pos = (-1.5, 0, -2.5), command = self.undo, text = PLocalizer.ShufflePrevButton, text_font = PiratesGlobals.getInterfaceFont(), text_scale = 0.18, text_pos = (0, -0.025), text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1))
        self.guiUndoButton.hide()
        self.guiDoneButton = DirectButton(parent = self.bookModel, relief = None, image = (self.charGui.find('**/chargui_frame02'), self.charGui.find('**/chargui_frame02_down'), self.charGui.find('**/chargui_frame02_over')), scale = 0.7, pos = (0.7, 0, -2.5), image_scale = (1.5, 1.0, 1.0), command = self.handleDone, text = PLocalizer.DoneButton, text_scale = 0.18, text_pos = (0, -0.025), text_fg = (0.6, 1, 0.6, 1), text_shadow = (0, 0, 0, 1))
        self.guiDoneButton.hide()
        self.pgsZoom = CharGuiSlider(self, parent = self.lowBookModel, text = PLocalizer.ZoomSlider, command = self.handleZoomSlider, range = (-1, 1))
        self.pgsZoom.setPos(-0.1, 0, 0.07)
        self.pgsZoom.setScale(0.5)
        self.pgsZoom['extraArgs'] = [self.pgsZoom]
        self.pgsRotate = CharGuiSlider(self, parent = self.lowBookModel, text = PLocalizer.RotateSlider, command = self.handleRotateSlider, range = (-1, 1))
        self.pgsRotate.setPos(-0.1, 0, -0.07)
        self.pgsRotate.setScale(0.5)
        self.pgsRotate['extraArgs'] = [self.pgsRotate]
        if self.isNPCEditor or self.wantNPCViewer or self.wantMarketingViewer:
            self.guiTopBar = DirectFrame(parent = base.a2dTopLeft, relief = DGG.FLAT, frameSize = (-1.0, 1.0, -0.1, 0.1), frameColor = (0.5, 0.5, 0.5, 0.3), pos = (0.6, 0, -0.1), scale = 0.5)
            self.guiTopBar.hide()
            self.toggleLODFrame = DirectFrame(parent = self.guiTopBar, relief = DGG.FLAT, frameSize = (-0.45, 0.45, -0.18, 0.1), frameColor = (0.9, 0.9, 0.9, 0.3), text = PLocalizer.LODFrame, text_scale = 0.1, text_pos = (0, -0.15), text_align = TextNode.ACenter, text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1), scale = 1, pos = (1.5, 0, 0.05))
            self.guiHiToggleLOD = DirectButton(parent = self.toggleLODFrame, relief = DGG.RAISED, pos = (0.3, 0.0, 0.0), command = self.handleHiLOD, frameSize = (-0.09, 0.09, -0.05, 0.05), borderWidth = (0.008, 0.008), text = PLocalizer.LODHi, text_pos = (0, -0.015), text_scale = 0.08)
            self.guiMedToggleLOD = DirectButton(parent = self.toggleLODFrame, relief = DGG.RAISED, pos = (0.0, 0.0, 0.0), command = self.handleMedLOD, frameSize = (-0.09, 0.09, -0.05, 0.05), borderWidth = (0.008, 0.008), text = PLocalizer.LODMed, text_pos = (0, -0.015), text_scale = 0.08)
            self.guiLowToggleLOD = DirectButton(parent = self.toggleLODFrame, relief = DGG.RAISED, pos = (-0.3, 0.0, 0.0), command = self.handleLowLOD, frameSize = (-0.09, 0.09, -0.05, 0.05), borderWidth = (0.008, 0.008), text = PLocalizer.LODLow, text_pos = (0, -0.015), text_scale = 0.08)
            self.guiTextureInfoBox = DirectFrame(parent = self.guiTopBar, text_fg = (1, 1, 1, 1), scale = 0.08, pos = (2.5, 0, -0.5))
            self.guiTextureInfoBox.setBin('gui-popup', 0)
            self.guiTextureInfo = {}
            self.guiTextureInfo['HAT'] = DirectLabel(parent = self.guiTextureInfoBox, text_fg = (1, 1, 1, 1), pos = (0, 0, 7.5))
            self.guiTextureInfo['SHIRT'] = DirectLabel(parent = self.guiTextureInfoBox, text_fg = (1, 1, 1, 1), pos = (0, 0, 6.5))
            self.guiTextureInfo['VEST'] = DirectLabel(parent = self.guiTextureInfoBox, pos = (0, 0, 5.5))
            self.guiTextureInfo['COAT'] = DirectLabel(parent = self.guiTextureInfoBox, pos = (0, 0, 4.5))
            self.guiTextureInfo['PANT'] = DirectLabel(parent = self.guiTextureInfoBox, pos = (0, 0, 3.5))
            self.guiTextureInfo['BELT'] = DirectLabel(parent = self.guiTextureInfoBox, pos = (0, 0, 2.5))
            self.guiTextureInfo['SOCK'] = DirectLabel(parent = self.guiTextureInfoBox, pos = (0, 0, 1.5))
            self.guiTextureInfo['SHOE'] = DirectLabel(parent = self.guiTextureInfoBox, pos = (0, 0, 1.5))
            self.guiResetButton = DirectButton(parent = self.guiTopBar, relief = DGG.RAISED, pos = (0.7, 0.0, 0.0), scale = 0.6, command = self.handleReset, frameColor = (1, 0, 0, 0.5), frameSize = (-0.25, 0.25, -0.1, 0.1), borderWidth = (0.02, 0.02), text = PLocalizer.ResetButton, text_pos = (0, -0.05), text_scale = 0.2, text_align = TextNode.ACenter)
            self.toggleAnimFrame = DirectFrame(parent = self.guiTopBar, relief = DGG.FLAT, frameSize = (-0.25, 0.25, -0.05, 0.05), frameColor = (0.8, 0.8, 0.8, 0), text = PLocalizer.AnimateFrame, text_scale = 0.1, text_pos = (-0.15, -0.025), text_align = TextNode.ACenter, text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1), scale = 1.2, pos = (-0.6, 0, -0.2))
            self.guiNextToggleAnim = DirectButton(parent = self.toggleAnimFrame, relief = DGG.RAISED, pos = (0.3, 0.0, 0.0), command = self.handleNextAnim, frameSize = (-0.09, 0.09, -0.05, 0.05), borderWidth = (0.008, 0.008), text = PLocalizer.MakeAPirateNextAnim, text_pos = (0, -0.015), text_scale = 0.1)
            self.guiNextToggleAnim.hide()
            self.guiLastToggleAnim = DirectButton(parent = self.toggleAnimFrame, relief = DGG.RAISED, pos = (-0.3, 0.0, 0.0), command = self.handleLastAnim, frameSize = (-0.09, 0.09, -0.05, 0.05), borderWidth = (0.008, 0.008), text = PLocalizer.MakeAPirateLastAnim, text_pos = (0, -0.015), text_scale = 0.1)
            self.guiLastToggleAnim.hide()
            self.pgsAnimSpeed = DirectSlider(parent = self.toggleAnimFrame, text = PLocalizer.AnimSpeedSlider, text_scale = 0.6, text_pos = (-4.8, -0.14), text_align = TextNode.ALeft, text_fg = (1, 1, 1, 1), pos = (0.23, 0, -0.1), value = 1, borderWidth = (0.04, 0.04), frameSize = (-3.0, 3.0, -0.3, 0.3), frameColor = (0.5, 0.5, 0.5, 0.3), scale = 0.11, range = (0, 1), command = self.handleAnimSpeedSlider)
            self.pgsAnimSpeed['extraArgs'] = [self.pgsAnimSpeed]
            self.pgsAnimPos = DirectSlider(parent = self.toggleAnimFrame, pos = (0.23, 0, -0.4), thumb_relief = DGG.FLAT, value = 1, thumb_text = '1', thumb_text_scale = 0.15, scale = 0.5, range = (1, 96), command = self.handleAnimPosSlider)
            self.pgsAnimPos['extraArgs'] = [self.pgsAnimPos]
            self.pgsAnimPos.hide()
            self.pgsAvHPos = DirectSlider(parent = self.toggleAnimFrame, text = PLocalizer.AvHPosSlider, text_scale = 0.6, text_pos = (-4.8, -0.14), text_align = TextNode.ALeft, text_fg = (1, 1, 1, 1), pos = (0.23, 0, -0.2), value = 0, borderWidth = (0.04, 0.04), frameSize = (-3.0, 3.0, -0.3, 0.3), frameColor = (0.5, 0.5, 0.5, 0.3), scale = 0.11, range = (-1, 6), command = self.handleAvHPosSlider)
            self.pgsAvHPos['extraArgs'] = [self.pgsAvHPos]
            self.pgsAvVPos = DirectSlider(parent = self.toggleAnimFrame, text = PLocalizer.AvVPosSlider, text_scale = 0.6, text_pos = (-4.8, -0.14), text_align = TextNode.ALeft, text_fg = (1, 1, 1, 1), pos = (0.23, 0, -0.3), value = 0, borderWidth = (0.04, 0.04), frameSize = (-3.0, 3.0, -0.3, 0.3), frameColor = (0.5, 0.5, 0.5, 0.3), scale = 0.11, range = (-1, 6), command = self.handleAvVPosSlider)
            self.pgsAvVPos['extraArgs'] = [self.pgsAvVPos]
            self.guiAnimListA_B = DirectOptionMenu(parent = self.toggleAnimFrame, frameSize = (-1, 13, -0.5, 1), scale = 0.04, pos = (0.1, 0, 0), textMayChange = 1, initialitem = 0, items = AnimListA_B, command = self.handleSetAnim)
            self.guiAnimListC_G = DirectOptionMenu(parent = self.toggleAnimFrame, frameSize = (-1, 13, -0.5, 1), scale = 0.04, pos = (0.7, 0, 0), textMayChange = 1, initialitem = 0, items = AnimListC_G, command = self.handleSetAnim)
            self.guiAnimListI_Si = DirectOptionMenu(parent = self.toggleAnimFrame, frameSize = (-1, 13, -0.5, 1), scale = 0.04, pos = (1.3, 0, 0), textMayChange = 1, initialitem = 0, items = AnimListI_Si, command = self.handleSetAnim)
            self.guiAnimListSl_Sz = DirectOptionMenu(parent = self.toggleAnimFrame, frameSize = (-1, 13, -0.5, 1), scale = 0.04, pos = (1.9, 0, 0), textMayChange = 1, initialitem = 0, items = AnimListSl_Sz, command = self.handleSetAnim)
            self.guiAnimListT_Z = DirectOptionMenu(parent = self.toggleAnimFrame, frameSize = (-1, 13, -0.5, 1), scale = 0.04, pos = (2.51, 0, 0), textMayChange = 1, initialitem = 0, items = AnimListT_Z, command = self.handleSetAnim)
            self.loadNPCButton()
            self.NPCGui = NPCGUI.NPCGUI(self)
        
        self.pirate = DynamicHuman.DynamicHuman()
        if self.avList[self.index] and self.avList[self.index] != OTPGlobals.AvatarSlotAvailable:
            self.pirate.style = self.avList[self.index].style
        elif self.chooseFemale:
            self.pirate.style = HumanDNA.HumanDNA('f')
        else:
            self.pirate.style = HumanDNA.HumanDNA()
        self.navyDNA = HumanDNA
        self.loadPirate()
        self.genderGui = GenderGUI.GenderGUI(self)
        self.bodyGui = BodyGUI.BodyGUI(self)
        self.headGui = HeadGUI.HeadGUI(self)
        self.clothesGui = ClothesGUI.ClothesGUI(self)
        self.hairGui = HairGUI.HairGUI(self)
        self.nameGui = NameGUI.NameGUI(self)
        if self.wantNPCViewer:
            self.tattooGui = TattooGUI.TattooGUI(self)
            self.jewelryGui = JewelryGUI.JewelryGUI(self)
        
        self.headGui.restore()
        self.addPage(PLocalizer.MakeAPiratePageNames[0])
        self.addPage(PLocalizer.MakeAPiratePageNames[1])
        self.addPage(PLocalizer.MakeAPiratePageNames[2])
        self.addPage(PLocalizer.MakeAPiratePageNames[3])
        self.addPage(PLocalizer.MakeAPiratePageNames[4])
        self.addPage(PLocalizer.MakeAPiratePageNames[5])
        self.addPage(PLocalizer.MakeAPiratePageNames[6])
        self.addPage(PLocalizer.MakeAPiratePageNames[7])
        self.addPage(PLocalizer.MakeAPiratePageNames[8])
        if self.wantNPCViewer:
            self.addPage(PLocalizer.MakeAPiratePageNames[9])
            self.addPage(PLocalizer.MakeAPiratePageNames[10])
        
        self.setPage(PLocalizer.MakeAPiratePageNames[0])
        self.setPage(PLocalizer.MakeAPiratePageNames[1])
        self.setPage(PLocalizer.MakeAPiratePageNames[2])
        self.setPage(PLocalizer.MakeAPiratePageNames[3])
        self.setPage(PLocalizer.MakeAPiratePageNames[4])
        self.setPage(PLocalizer.MakeAPiratePageNames[5])
        self.setPage(PLocalizer.MakeAPiratePageNames[6])
        self.setPage(PLocalizer.MakeAPiratePageNames[7])
        self.setPage(PLocalizer.MakeAPiratePageNames[8])
        self.setPage(PLocalizer.MakeAPiratePageNames[0])
        self.pageTabs[1].hide()
        self.pageTabs[2].hide()
        self.pageTabs[3].hide()
        self.pageTabs[4].hide()
        self.pageTabs[5].hide()
        self.pageTabs[6].hide()
        self.pageTabs[7].hide()
        self.pageTabs[8].hide()
        if self.wantNPCViewer:
            self.pageTabs[9].hide()
            self.pageTabs[10].hide()

    def randomMe(self):
        self.genderGui.randomPick()
    
    def loadPirate(self):
        self.unloadPirate()
        self.pirate.setDNAString(self.pirate.style)
        self.pirate.generateHuman(self.pirate.style.gender)
        if self.isNPCEditor or self.wantNPCViewer:
            self.pirate.disableBlend()
            self.pirate.model.setupSelectionChoices('NPC')
        else:
            self.pirate.model.setupSelectionChoices('DEFAULT')
            self.pirate.mixingEnabled = False
            self.pirate.enableBlend()
            self.pirate.loop('idle_centered')
            self.pirate.loop('idle')
            self.pirate.setControlEffect('idle_centered', 0)
            self.pirate.setControlEffect('idle', 1)
        self.avatar = self.pirate.model
        self.pirate.useLOD(2000)
        if self.npcViewerLOD > -1:
            if self.npcViewerLOD == 1:
                self.pirate.useLOD(1000)
            elif self.npcViewerLOD == 2:
                self.pirate.useLOD(500)

        self.pirate.show()

    def unloadPirate(self):
        if self.pirate and self.pirate.loaded:
            self.pirate.hide()

    def loadSkeleton(self, type):
        self.unloadSkeleton()
        self.skeletonType = type
        self.skeleton = Skeleton.Skeleton()
        self.skeleton.style = SkeletonBodyTypes[type]
        self.skeleton.generateSkeleton()
        if self.isNPCEditor or self.wantNPCViewer:
            self.skeleton.disableBlend()
        
        self.avatar = self.skeleton.model

    def unloadSkeleton(self):
        if self.skeleton:
            self.skeleton.hide()
            self.skeleton.delete()
            self.skeleton = None

    def unload(self):
        self.charGui.removeNode()
        self.charGui = None
        self.pirate.detachNode()
        self.pirate.cleanupHuman()
        self.pirate.delete()
        if self.isNPCEditor:
            camera.reparentTo(render)
            self.avatarDummyNode.removeNode()
            del self.avatarDummyNode
        
        self.genderGui.unload()
        self.bodyGui.unload()
        self.headGui.unload()
        self.clothesGui.unload()
        self.hairGui.unload()
        self.nameGui.unload()
        self.nameGui.destroy()
        if self.wantNPCViewer:
            self.tattooGui.unload()
            self.jewelryGui.unload()
        
        self.pirate.stopBlink()
        if hasattr(self, 'jail'):
            self.jail.removeNode()
            del self.jail
        
        if self.entered and not self.noJailLight:
            self.ambientLight.unload()
            self.spotLight1.unload()
            self.spotLight2.unload()
            self.spotLight3.unload()
            del self.ambientLight
            del self.spotLight1
            del self.spotLight2
            del self.spotLight3
        
        if self.isNPCEditor or self.wantNPCViewer or self.wantMarketingViewer:
            self.guiTopBar.destroy()
            del self.guiTopBar
            del self.guiNextToggleAnim
            del self.guiLastToggleAnim
            del self.toggleAnimFrame
            del self.guiResetButton
        
        self.guiBottomBar.destroy()
        del self.guiBottomBar
        del self.guiCancelButton
        del self.guiRandomButton
        del self.guiDoneButton
        del self.guiNextButton
        self.bookModel.destroy()
        del self.bookModel
        self.lowBookModel.destroy()
        del self.lowBookModel
        del self.names
        del self.dnastring
        del self.nameList
        del self.music
        del self.soundBack
        if hasattr(self, 'fsm'):
            del self.fsm
        
        del self.avatar
        del self.newPotAv
        if self.isNPCEditor:
            self.pirate.delete()
        
        del self.pirate
        self.ignoreAll()
    
    def getDNA(self):
        return self.dnastring

    def handleCancel(self):
        self.doneStatus = 'cancel'
        self.shopsVisited = []
        if self.isNPCEditor:
            self.piratesEditor.updateNPC('Cancel')
        
        base.transitions.fadeOut(finishIval = EventInterval(self.doneEvent))

    def handleDone(self):
        self.doneStatus = 'created'
        if hasattr(self, 'confirmInvalidName'):
            self.confirmInvalidName.destroy()
            del self.confirmInvalidName
        
        self.nameGui._checkTypeANameAsPickAName()
        if hasattr(base, 'pe') and base.pe or self.nameGui.cr is None:
            self._handleNameOK()
        elif self.nameGui.hasCustomName():
            if self._waitForServerDlg:
                self._waitForServerDlg.destroy()
                self._waitForServerDlg = None
            
            self._waitForServerDlg = PDialog.PDialog(text = PLocalizer.MakeAPirateWait, style = OTPDialog.NoButtons)
            self.nameGui.getTypeANameProblem(self._handleNameProblem)
        else:
            self._handleNameOK()
    
    def _handleNameProblem(self, problemStr):
        if self._waitForServerDlg:
            self._waitForServerDlg.destroy()
            self._waitForServerDlg = None
        
        if problemStr:
            
            def confirmInvalidName(value):
                self.confirmInvalidName.destroy()
                del self.confirmInvalidName

            self.confirmInvalidName = PDialog.PDialog(text = problemStr, style = OTPDialog.Acknowledge, command = confirmInvalidName)
        else:
            self._handleNameOK()
    
    def _handleNameOK(self):
        self.bookModel.stash()
        self.guiDoneButton.hide()
        self.genderGui.save()
        self.bodyGui.save()
        self.headGui.save()
        self.clothesGui.save()
        self.hairGui.save()
        self.nameGui.save()
        if self.wantNPCViewer:
            self.tattooGui.save()
            self.jewelryGui.save()
        
        if self.skipTutorial:
            newPotAv = PotentialAvatar.PotentialAvatar(0, [
                'dbp',
                '',
                '',
                ''], self.pirate.style, self.index, 0)
            self.newPotAv = newPotAv
        
        if self.isNPCEditor:
            self.editorAvatar.setDNAString(self.pirate.style)
            self.piratesEditor.updateNPC('Save')
            self.exit()
            self.unload()
        
        def sendDone(value = 1):
            messenger.send(self.doneEvent)
            base.transitions.fadeIn(1.0)

        def chooseAv(avId):
            if not avId:
                self.notify.error('An error occured when trying to create avatar!')

            self.avId = avId
            sendDone()

        def createAv():
            self.acceptOnce('createdNewAvatar', chooseAv)
            base.cr.csm.sendCreateAvatar(self.pirate.style, '', self.index, self.pirate.style.name)

        def acknowledgeTempName(value):
            self.confirmTempName.destroy()
            self.confirmTempName = None
            if self.isTutorial or self.isNPCEditor or self.wantNPCViewer:
                base.transitions.fadeOut(finishIval = Func(sendDone))
            else:
                base.transitions.fadeOut(finishIval = Func(createAv))

        if self.nameGui.customName and not self.isNPCEditor and not self.confirmTempName:
            self.confirmTempName = PDialog.PDialog(text = PLocalizer.TempNameIssued, style = OTPDialog.Acknowledge, command = acknowledgeTempName)
        elif self.isTutorial or self.isNPCEditor or self.wantNPCViewer:
            base.transitions.fadeOut(finishIval = Func(sendDone))
        else:
            base.transitions.fadeOut(finishIval = Func(createAv))
    
    def toggleSlide(self):
        self.slide = 1 - self.slide
    
    def enterNameShop(self):
        self.pgsZoom['value'] = 0.0
        self.nameGui.enter()
        self.shop = NAMESHOP
        if NAMESHOP not in self.shopsVisited:
            self.shopsVisited.append(NAMESHOP)

    def exitNameShop(self):
        self.nameGui.exit()

    def resetName(self):
        self.nameGui.reset()
    
    def makeRandomName(self):
        self.nameGui.makeRandomName()

    def resetGender(self, index):
        self.genderGui.reset(index)

    def makeRandomGender(self):
        self.genderGui.randomPick()
    
    def enterBodyShop(self):
        self.shop = BODYSHOP
        self.pgsZoom['value'] = 0.0
        self.genderGui.enter()
        self.bodyGui.enter()
        self.accept('BodyShop-done', self.handleBodyShopDone)
        base.disableMouse()
        if BODYSHOP not in self.shopsVisited:
            self.shopsVisited.append(BODYSHOP)
    
    def exitBodyShop(self):
        self.ignore('BodyShop-done')
        self.genderGui.exit()
        self.bodyGui.exit()
    
    def handleBodyShopDone(self):
        pass

    def resetBody(self):
        self.bodyGui.reset()
    
    def makeRandomBody(self):
        self.bodyGui.randomPick()
    
    def enterHeadShop(self):
        self.shop = HEADSHOP
        self.pgsZoom.node().setValue(1)
        self.headGui.shape.enter()
        self.accept('HeadShop-done', self.handleHeadShopDone)
        base.disableMouse()
        if HEADSHOP not in self.shopsVisited:
            self.shopsVisited.append(HEADSHOP)
    
    def exitHeadShop(self):
        self.ignore('HeadShop-done')
        self.headGui.shape.exit()
    
    def handleHeadShopDone(self):
        pass
    
    def resetHead(self):
        self.headGui.shape.reset()
    
    def makeRandomHead(self):
        self.headGui.shape.randomPick()
    
    def enterMouthShop(self):
        self.shop = MOUTHSHOP
        self.pgsZoom.node().setValue(1)
        self.headGui.mouth.enter()
        self.accept('MouthShop-done', self.handleMouthShopDone)
        base.disableMouse()
        if MOUTHSHOP not in self.shopsVisited:
            self.shopsVisited.append(MOUTHSHOP)

    def exitMouthShop(self):
        self.ignore('MouthShop-done')
        self.headGui.mouth.exit()

    def handleMouthShopDone(self):
        pass

    def resetMouth(self):
        self.headGui.mouth.reset()

    def makeRandomMouth(self):
        self.headGui.mouth.randomPick()
    
    def enterEyesShop(self):
        self.shop = EYESSHOP
        self.pgsZoom.node().setValue(1)
        self.headGui.eyes.enter()
        self.accept('EyesShop-done', self.handleEyesShopDone)
        base.disableMouse()
        if EYESSHOP not in self.shopsVisited:
            self.shopsVisited.append(EYESSHOP)

    def exitEyesShop(self):
        self.ignore('EyesShop-done')
        self.headGui.eyes.exit()

    def handleEyesShopDone(self):
        pass
    
    def resetEyes(self):
        self.headGui.eyes.reset()
    
    def makeRandomEyes(self):
        self.headGui.eyes.randomPick()
    
    def enterNoseShop(self):
        self.shop = NOSESHOP
        self.pgsZoom.node().setValue(1)
        self.headGui.nose.enter()
        self.accept('NoseShop-done', self.handleNoseShopDone)
        base.disableMouse()
        if NOSESHOP not in self.shopsVisited:
            self.shopsVisited.append(NOSESHOP)

    def exitNoseShop(self):
        self.ignore('NoseShop-done')
        self.headGui.nose.exit()
    
    def handleNoseShopDone(self):
        pass
    
    def resetNose(self):
        self.headGui.nose.reset()
    
    def makeRandomNose(self):
        self.headGui.nose.randomPick()

    def enterEarShop(self):
        self.shop = EARSHOP
        self.pgsZoom.node().setValue(1)
        self.headGui.ear.enter()
        self.accept('EarShop-done', self.handleEarShopDone)
        base.disableMouse()
        if EARSHOP not in self.shopsVisited:
            self.shopsVisited.append(EARSHOP)
    
    def exitEarShop(self):
        self.ignore('EarShop-done')
        self.headGui.ear.exit()

    def handleEarShopDone(self):
        pass
    
    def resetEar(self):
        self.headGui.ear.reset()

    def makeRandomEar(self):
        self.headGui.ear.randomPick()

    def enterHairShop(self):
        self.shop = HAIRSHOP
        self.pgsZoom.node().setValue(0.9)
        self.hairGui.enter()
        self.accept('HairShop-done', self.handleHairShopDone)
        base.disableMouse()
        if HAIRSHOP not in self.shopsVisited:
            self.shopsVisited.append(HAIRSHOP)

    def exitHairShop(self):
        self.ignore('HairShop-done')
        self.hairGui.exit()
    
    def handleHairShopDone(self):
        pass
    
    def resetHair(self):
        self.hairGui.reset()
    
    def makeRandomHair(self):
        self.hairGui.randomPick()
    
    def enterClothesShop(self):
        self.shop = CLOTHESSHOP
        self.pgsZoom.node().setValue(0.0)
        self.clothesGui.enter()
        self.accept('ClothesShop-done', self.handleClothesShopDone)
        base.disableMouse()
        if CLOTHESSHOP not in self.shopsVisited:
            self.shopsVisited.append(CLOTHESSHOP)

    def exitClothesShop(self):
        self.ignore('ClothesShop-done')
        self.clothesGui.exit()

    def handleClothesShopDone(self):
        pass
    
    def resetClothing(self):
        self.clothesGui.reset()
    
    def makeRandomClothing(self):
        self.clothesGui.randomPick()
    
    def enterTattooShop(self):
        self.shop = TATTOOSHOP
        self.pgsZoom.node().setValue(0.0)
        self.tattooGui.enter()
        self.accept('TattooShop-done', self.handleTattooShopDone)
        base.disableMouse()
        if TATTOOSHOP not in self.shopsVisited:
            self.shopsVisited.append(TATTOOSHOP)

    def exitTattooShop(self):
        self.ignore('TattooShop-done')
        self.tattooGui.exit()
    
    def handleTattooShopDone(self):
        pass

    def resetTattoo(self):
        self.tattooGui.reset()

    def makeRandomTattoo(self):
        self.tattooGui.randomPick()

    def enterJewelryShop(self):
        self.shop = JEWELRYSHOP
        self.pgsZoom.node().setValue(0.0)
        self.jewelryGui.enter()
        self.accept('JewelryShop-done', self.handleJewelryShopDone)
        base.disableMouse()
        if JEWELRYSHOP not in self.shopsVisited:
            self.shopsVisited.append(JEWELRYSHOP)

    def exitJewelryShop(self):
        self.ignore('JewelryShop-done')
        self.jewelryGui.exit()

    def handleJewelryShopDone(self):
        pass

    def resetJewelry(self):
        self.jewelryGui.reset()

    def makeRandomJewelry(self):
        self.jewelryGui.randomPick()

    def handlePirate(self):
        self.avatarType = AVATAR_PIRATE
        self.unloadSkeleton()
        self.genderGui.enter()
        self.genderGui.handleMale()
        self.bodyGui.enter()
        self.loadPirate()
        self.placePirate()
        self.PirateButton['relief'] = DGG.SUNKEN
        self.NPCButton['relief'] = DGG.RAISED
        self.NavyButton['relief'] = DGG.RAISED
        self.showPageTabs()
        self.setPage(PLocalizer.MakeAPiratePageNames[0])
        self.NPCGui.exit()
    
    def handleNPC(self):
        self.avatarType = AVATAR_SKELETON
        self.unloadPirate()
        self.loadSkeleton(4)
        self.placeSkeleton(4)
        self.PirateButton['relief'] = DGG.RAISED
        self.NPCButton['relief'] = DGG.SUNKEN
        self.NavyButton['relief'] = DGG.RAISED
        self.hidePageTabs()
        self.NPCGui.enter()
    
    def handleNavy(self):
        self.avatarType = AVATAR_NAVY
        self.unloadSkeleton()
        self.genderGui.enter()
        self.genderGui.handleNavy()
        self.bodyGui.enter()
        self.loadPirate()
        self.placePirate()
        self.PirateButton['relief'] = DGG.RAISED
        self.NPCButton['relief'] = DGG.RAISED
        self.NavyButton['relief'] = DGG.SUNKEN
        self.showPageTabs()
        self.setPage(PLocalizer.MakeAPiratePageNames[0])
        self.NPCGui.exit()

    def handleNextAnim(self):
        self.lastAnim = (self.lastAnim + 1) % len(AnimList)
        self.pirate.loop(AnimList[self.lastAnim])
        if self.skeleton:
            self.skeleton.loop(AnimList[self.lastAnim])

    def handleLastAnim(self):
        self.lastAnim = (self.lastAnim + len(AnimList) - 1) % len(AnimList)
        self.pirate.loop(AnimList[self.lastAnim])
        if self.skeleton:
            self.skeleton.loop(AnimList[self.lastAnim])

    def handleHiLOD(self):
        self.npcViewerLOD = 0
        self.pirate.useLOD(2000)

    def handleMedLOD(self):
        self.npcViewerLOD = 1
        self.pirate.useLOD(1000)

    def handleLowLOD(self):
        self.npcViewerLOD = 2
        self.pirate.useLOD(500)

    def handleNext(self):
        idx = self.currPageIndex + 1
        if idx > self.numShops - 1:
            return

        if idx == self.numShops - 1:
            self.guiNextButton.hide()
            self.guiDoneButton.show()

        if idx >= self.lowestPage:
            self.lowestPage = idx
            self.pageTabs[idx].show()

        self.setPage(PLocalizer.MakeAPiratePageNames[idx])

    def handleZoomSlider(self, pgs):
        pass

    def restoreIdle(self, task):
        if self.pirate:
            self.pirate.loop('idle')
            self.idleFSM.request('default')
        
        return Task.done
    
    def handleAltIdle(self, task):
        if self.pirate:
            r = self.pirate.randGen.random() * 10
            if r < 4:
                if self.genderIdx == 1:
                    anim = 'emote_wave'
                else:
                    anim = 'idle_arm_scratch'
            elif r < 7:
                anim = 'emote_wink'
            elif r < 9:
                anim = 'emote_wave'
            elif self.genderIdx == 1:
                anim = 'primp_idle'
            else:
                anim = 'idle_flex'
        
        self.pirate.play(anim)
        dur = self.pirate.getDuration(anim)
        
        try:
            taskMgr.doMethodLater(dur, self.restoreIdle, 'avCreate-restoreIdle')
        except:
            self.notify.warning("task to restore idle didn't work")
            self.restoreIdle

        return Task.done
    
    def altIdleTask(self, task):
        if self.pirate:
            if self.idleFSM.getCurrentState().getName() == 'default':
                r = self.pirate.randGen.random()
                taskMgr.doMethodLater(r * 10 + 20, self.handleAltIdle, 'avCreate-altIdle')
                self.idleFSM.request('alt1')

        return Task.cont

    def enterIdleFSMDefault(self):
        pass

    def exitIdleFSMDefault(self):
        pass

    def enterIdleFSMAlt1(self):
        pass

    def exitIdleFSMAlt1(self):
        pass

    def enterIdleFSMAlt2(self):
        pass

    def exitIdleFSMAlt2(self):
        pass

    def zoomTask(self, task):
        value = self.pgsZoom.getValue()
        iPos = self.camInitPos
        iHpr = self.camInitHpr
        deltaPos = deltaHpr = None
        distancePercent = (value + 1) / 2.0
        if self.isNPCEditor:
            headPos = self.pirate.headNode.getPos(self.avatarDummyNode)
        else:
            headPos = self.pirate.headNode.getPos(render)
        if value > 0.0:
            deltaPos = (headPos + self.offsetZoomPos - self.camInitPos) * value
            if self.isNPCEditor:
                deltaHpr = (self.camZoomOutHpr - self.camInitHpr) * value
            else:
                deltaHpr = (self.offsetZoomHpr - self.camInitHpr) * value
            if not self.isNPCEditor and not self.wantNPCViewer:
                subValue = (value - 0.5) * 2.0
                if subValue >= 0:
                    self.pirate.setControlEffect('idle_centered', subValue)
                    self.pirate.setControlEffect('idle', 1 - subValue)
                else:
                    self.pirate.setControlEffect('idle_centered', 0)
                    self.pirate.setControlEffect('idle', 1)
        else:
            if not self.isNPCEditor and not self.wantNPCViewer:
                self.pirate.setControlEffect('idle_centered', 0)
                self.pirate.setControlEffect('idle', 1)
            value = -value
            deltaPos = (self.camZoomOutPos - self.camInitPos) * value
            deltaHpr = (self.camZoomOutHpr - self.camInitHpr) * value
        nPos = Vec3(iPos[0] + deltaPos[0], iPos[1] + deltaPos[1], iPos[2] + deltaPos[2])
        nHpr = Vec3(iHpr[0] + deltaHpr[0], iHpr[1] + deltaHpr[1], iHpr[2] + deltaHpr[2])
        if self.avatar.dna:
            bias = heightBiasArray[self.avatar.dna.getGender()][self.avatar.dna.getBodyShape()]
            camera.setPos(nPos)
            camera.setHpr(nHpr)
        else:
            bias = heightBiasArray['s'][self.skeletonType]
            camera.setPos(nPos)
            camera.setHpr(nHpr)
        return Task.cont

    def handleRotateSlider(self, pgs):
        value = pgs['value']
        if self.isNPCEditor:
            self.lastRot = value * 180
        else:
            self.lastRot = value * 180 + self.initH
        self.rotatePirate()
    
    def rotatePirate(self):
        hpr = self.pirate.getHpr()
        self.pirate.setHpr(self.lastRot, hpr[1], hpr[2])
        if self.skeleton:
            self.skeleton.setHpr(self.lastRot, hpr[1], hpr[2])

    def _stopMouseReadTask(self):
        taskMgr.remove('MakeAPirate-MouseRead')

    def _startMouseReadTask(self):
        self._stopMouseReadTask()
        mouseData = base.win.getPointer(0)
        self.lastMousePos = (mouseData.getX(), mouseData.getY())
        taskMgr.add(self._mouseReadTask, 'MakeAPirate-MouseRead')

    def _mouseReadTask(self, task):
        if not base.mouseWatcherNode.hasMouse():
            pass
        else:
            winSize = (base.win.getXSize(), base.win.getYSize())
            mouseData = base.win.getPointer(0)
            if mouseData.getX() > winSize[0] or mouseData.getY() > winSize[1]:
                pass
            else:
                dx = mouseData.getX() - self.lastMousePos[0]
                mouseData = base.win.getPointer(0)
                self.lastMousePos = (mouseData.getX(), mouseData.getY())
                value = self.pgsRotate['value']
                value = max(-1, min(1, value + dx * 0.004))
                self.pgsRotate['value'] = value
        return Task.cont
    
    def _handleWheelUp(self):
        value = self.pgsZoom['value']
        value = min(1, max(-1, value + 0.1))
        self.pgsZoom['value'] = value
    
    def _handleWheelDown(self):
        value = self.pgsZoom['value']
        value = min(1, max(-1, value - 0.1))
        self.pgsZoom['value'] = value

    def handleSpin(self, value):
        if not hasattr(self, 'oldSpinValue'):
            self.oldSpinValue = 0
        
        if value > self.oldSpinValue:
            if self.pirate.getCurrentAnim() != 'spin_right':
                self.pirate.loop('spin_right')
            
        elif value < self.oldSpinValue:
            if self.pirate.getCurrentAnim() != 'spin_left':
                self.pirate.loop('spin_left')
            
        elif self.pirate.getCurrentAnim() != 'idle':
            self.pirate.loop('idle')
        
        self.oldSpinValue = value
    
    def handleAnimSpeedSlider(self, pgs):
        value = pgs['value']
        if self.skeleton:
            avatar = self.skeleton
        else:
            avatar = self.pirate
        avatar.setPlayRate(rate = value, animName = AnimList[self.lastAnim])
    
    def handleAnimPosSlider(self, pgs):
        pass
    
    def handleAvHPosSlider(self, pgs):
        if self.aPos == None:
            return
        
        value = pgs['value'] + self.aPos.getX()
        self.pirate.setX(value)
        if self.skeleton:
            self.skeleton.setX(value)
    
    def handleAvVPosSlider(self, pgs):
        if self.aPos == None:
            return
        
        value = pgs['value'] + self.aPos.getZ()
        self.pirate.setZ(value)
        if self.skeleton:
            self.skeleton.setZ(value)

    def handleSetAnim(self, pgs):
        self.lastAnim = AnimList.index(pgs)
        if self.skeleton:
            self.skeleton.loop(AnimList[0])
            self.skeleton.loop(AnimList[self.lastAnim])
        else:
            self.pirate.loop(AnimList[0])
            self.pirate.loop(AnimList[self.lastAnim])
        self.pgsAnimPos['range'] = (1, 30)
        self.pgsAnimPos['thumb_text'] = '30'

    def handleRandom(self):
        if self.avatarType == AVATAR_PIRATE:
            if self.shop == BODYSHOP:
                self.makeRandomBody()
            elif self.shop == HEADSHOP:
                self.makeRandomHead()
            elif self.shop == MOUTHSHOP:
                self.makeRandomMouth()
            elif self.shop == EYESSHOP:
                self.makeRandomEyes()
            elif self.shop == NOSESHOP:
                self.makeRandomNose()
            elif self.shop == EARSHOP:
                self.makeRandomEar()
            elif self.shop == HAIRSHOP:
                self.makeRandomHair()
            elif self.shop == CLOTHESSHOP:
                self.makeRandomClothing()
            elif self.shop == NAMESHOP:
                self.makeRandomName()
            
        elif self.avatarType == AVATAR_SKELETON:
            self.NPCGui.randomPick()
        elif self.avatarType == AVATAR_NAVY:
            if self.shop == BODYSHOP:
                self.makeRandomBody()
                self.makeRandomHead()
                self.makeRandomHair()
            elif self.shop == HEADSHOP:
                self.makeRandomHead()
            elif self.shop == HAIRSHOP:
                self.makeRandomHair()

    def handleReset(self):
        if self.avatarType == AVATAR_PIRATE:
            if self.shop == BODYSHOP:
                if self.pirate.style.gender == 'm':
                    self.resetGender(0)
                else:
                    self.resetGender(1)
                self.resetBody()
            elif self.shop == HEADSHOP:
                self.resetHead()
            elif self.shop == MOUTHSHOP:
                self.resetMouth()
            elif self.shop == EYESSHOP:
                self.resetEyes()
            elif self.shop == NOSESHOP:
                self.resetNose()
            elif self.shop == EARSHOP:
                self.resetEar()
            elif self.shop == HAIRSHOP:
                self.resetHair()
            elif self.shop == CLOTHESSHOP:
                self.resetClothing()
            elif self.shop == NAMESHOP:
                self.resetName()
            elif self.shop == TATTOOSHOP:
                self.resetTattoo()
            elif self.shop == JEWELRYSHOP:
                self.resetJewelry()
            
        elif self.avatarType == AVATAR_SKELETON:
            self.NPCGui.reset()
        elif self.avatarType == AVATAR_NAVY:
            if self.shop == BODYSHOP:
                self.resetBody()
                self.resetHead()
                self.resetHair()
            elif self.shop == HEADSHOP:
                self.resetHead()
            elif self.shop == HAIRSHOP:
                self.resetHair()

    def addPage(self, pageName = 'Page'):
        self.addPageTab(pageName)

    def addPageTab(self, pageName = 'Page'):
        tabIndex = len(self.pageTabs)
        
        def goToPage():
            self.setPage(pageName)

        yOffset = 0.695 - 0.325 * len(self.pageTabs)
        tabText = pageName
        icon = '**/' + MakeAPiratePageIcons[pageName]
        icon_down = '**/' + MakeAPiratePageIcons[pageName] + '_over'
        icon_over = '**/' + MakeAPiratePageIcons[pageName] + '_over'
        pageTab = DirectButton(parent = self.bookModel,
                               relief = None,
                               image = (self.charGui.find('**/chargui_frame02'),
                                        self.charGui.find('**/chargui_frame02_down'),
                                        self.charGui.find('**/chargui_frame02_over')),
                               geom = (self.charGui.find(icon),
                                       self.charGui.find(icon_down),
                                       self.charGui.find(icon_over)),
                               pos = (-1.475, 0, yOffset),
                               scale = 0.87,
                               command = goToPage)
        self.pageNames.append(pageName)
        self.pageTabs.append(pageTab)

    def setPage(self, pageName):
        nextPageIndex = self.pageNames.index(pageName)
        if self.currPageIndex is not None:
            if self.currPageIndex == nextPageIndex:
                return
            
            messenger.send(ShopNames[self.currPageIndex] + '-done')
        
        self.pgsRotate.setValue(0)
        self.currPageIndex = self.pageNames.index(pageName)
        self.setPageTabIndex(self.currPageIndex)
        self.request(ShopNames[self.currPageIndex])

    def setPageTabIndex(self, pageTabIndex):
        if self.currPageTabIndex is not None and pageTabIndex != self.currPageTabIndex:
            self.pageTabs[self.currPageTabIndex].clearColorScale()
        
        self.currPageTabIndex = pageTabIndex
        self.pageTabs[self.currPageTabIndex].setColorScale(1, 1, 0.5, 1)

    def showPageTabs(self):
        for i in range(0, len(self.pageTabs)):
            self.pageTabs[i].show()
    
    def hidePageTabs(self):
        if self.currPageTabIndex == BODYSHOP:
            self.exitBodyShop()
        elif self.currPageTabIndex == HEADSHOP:
            self.exitHeadShop()
        elif self.currPageTabIndex == MOUTHSHOP:
            self.exitMouthShop()
        elif self.currPageTabIndex == EYESSHOP:
            self.exitEyesShop()
        elif self.currPageTabIndex == NOSESHOP:
            self.exitNoseShop()
        elif self.currPageTabIndex == EARSHOP:
            self.exitEarShop()
        elif self.currPageTabIndex == HAIRSHOP:
            self.exitHairShop()
        elif self.currPageTabIndex == CLOTHESSHOP:
            self.exitClothesShop()
        elif self.currPageTabIndex == NAMESHOP:
            self.exitNameShop()
        elif self.currPageTabIndex == TATTOOSHOP:
            self.exitTattoosShop()
        elif self.currPageTabIndex == JEWELRYSHOP:
            self.exitJewelryShop()
        
        for i in range(0, len(self.pageTabs)):
            self.pageTabs[i].hide()

    def handleRandomAll(self):
        self.overwriteCurrentUndo()
        self.inRandomAll = True
        if self.avatarType == AVATAR_PIRATE:
            count = self.currPageIndex + 1
            page = self.currPageIndex
            self.setPage(PLocalizer.MakeAPiratePageNames[0])
            self.makeRandomBody()
            self.setPage(PLocalizer.MakeAPiratePageNames[1])
            self.makeRandomHead()
            self.setPage(PLocalizer.MakeAPiratePageNames[2])
            self.makeRandomMouth()
            self.setPage(PLocalizer.MakeAPiratePageNames[3])
            self.makeRandomEyes()
            self.setPage(PLocalizer.MakeAPiratePageNames[4])
            self.makeRandomNose()
            self.setPage(PLocalizer.MakeAPiratePageNames[5])
            self.makeRandomEar()
            self.setPage(PLocalizer.MakeAPiratePageNames[6])
            self.makeRandomHair()
            self.setPage(PLocalizer.MakeAPiratePageNames[7])
            self.makeRandomClothing()
            self.setPage(PLocalizer.MakeAPiratePageNames[8])
            self.makeRandomName()
            self.setPage(PLocalizer.MakeAPiratePageNames[page])
            idx = 0
            if self.pirate.gender == 'f':
                idx = 1
            
            optionsLeft = len(self.JSD_ANYTIME[idx])
            if optionsLeft and random.choice([0, 1, 2, 3]) == 1:
                if self.lastDialog:
                    self.lastDialog.stop()
                
                choice = random.choice(list(range(0, optionsLeft)))
                dialog = self.JSD_ANYTIME[idx][choice]
                base.playSfx(dialog)
                self.lastDialog = dialog
                self.JSD_ANYTIME[idx].remove(dialog)
            
        elif self.avatarType == AVATAR_SKELETON:
            self.NPCGui.randomPick()
        elif self.avatarType == AVATAR_NAVY:
            if self.shop == BODYSHOP:
                self.makeRandomBody()
                self.makeRandomHead()
                self.makeRandomHair()
            elif self.shop == HEADSHOP:
                self.makeRandomHead()
            elif self.shop == HAIRSHOP:
                self.makeRandomHair()

        self.inRandomAll = False
        self.appendUndo()
        self.undoLevel[self.pirate.style.gender] = len(self.undoList[self.pirate.style.gender]) - 1
    
    def handleQuarterView(self, extraArgs):
        hpr = self.pirate.getHpr()
        if extraArgs != None:
            hCam = self.pirate.getH(camera)
            rotX = hpr[0]
            fudge = self.initH
            if self.isNPCEditor:
                fudge = 0
            
            if hCam < 0:
                if hCam >= -180:
                    rotX = fudge + 45
                
            elif hCam <= 180:
                rotX = fudge - 45
            
            self.pirate.setHpr(rotX, hpr[1], hpr[2])
        else:
            self.pirate.setHpr(self.lastRot, hpr[1], hpr[2])

    def enableRandom(self):
        self.guiRandomButton['state'] = 'normal'
        self.guiRandomButton.setColorScale(Vec4(1, 1, 1, 1))
    
    def disableRandom(self):
        self.guiRandomButton['state'] = 'disabled'
        self.guiRandomButton.setColorScale(Vec4(0.3, 0.3, 0.3, 1))
    
    def storeUndo(self):
        gender = self.pirate.style.gender
        self.bodyGui.save()
        self.headGui.save()
        self.clothesGui.save()
        self.hairGui.save()
        self.undoList[gender] = self.undoList[gender][:self.undoLevel[gender] + 1]
        self.undoLevel[gender] += 1
        h = HumanDNA.HumanDNA()
        h.copy(self.pirate.style)
        self.undoList[gender].append(h)

    def undo(self):
        self.boundUndo()
    
    def redo(self):
        self.boundRedo()

    def overwriteCurrentUndo(self):
        gender = self.pirate.style.gender
        self.bodyGui.save()
        self.headGui.save()
        self.clothesGui.save()
        self.hairGui.save()
        h = HumanDNA.HumanDNA()
        h.copy(self.pirate.style)
        self.undoList[gender][self.undoLevel[gender]] = h

    def appendUndo(self):
        gender = self.pirate.style.gender
        self.bodyGui.save()
        self.headGui.save()
        self.clothesGui.save()
        self.hairGui.save()
        h = HumanDNA.HumanDNA()
        h.copy(self.pirate.style)
        self.undoList[gender].append(h)
        self.prevShuffleButton['state'] = DGG.NORMAL
        if self.undoLevel[gender] == len(self.undoList[gender]) - 1:
            self.nextShuffleButton['state'] = DGG.DISABLED

    def boundUndo(self):
        gender = self.pirate.style.gender
        listLen = len(self.undoList[gender])
        self.overwriteCurrentUndo()
        self.pirate.style.copy(self.undoList[gender][self.undoLevel[gender] - 1])
        self.undoLevel[gender] -= 1
        self.refresh()
        if self.undoLevel[gender] == 0:
            self.prevShuffleButton['state'] = DGG.DISABLED
        
        if self.undoLevel[gender] < len(self.undoList[gender]) - 1:
            self.nextShuffleButton['state'] = DGG.NORMAL

    def boundRedo(self):
        gender = self.pirate.style.gender
        listLen = len(self.undoList[gender])
        self.overwriteCurrentUndo()
        if self.undoLevel[gender] < listLen - 1:
            self.pirate.style = HumanDNA.HumanDNA()
            self.pirate.style.copy(self.undoList[gender][self.undoLevel[gender] + 1])
            self.pirate.style = self.pirate.style
            self.undoLevel[gender] += 1
            self.refresh()
        
        if self.undoLevel[gender] == len(self.undoList[gender]) - 1:
            self.nextShuffleButton['state'] = DGG.DISABLED
        
        if self.undoLevel[gender] > 0:
            self.prevShuffleButton['state'] = DGG.NORMAL

    def refreshShuffleButtons(self):
        gender = self.pirate.style.gender
        listLen = len(self.undoList[gender])
        self.prevShuffleButton['state'] = DGG.DISABLED
        self.nextShuffleButton['state'] = DGG.DISABLED
        if self.undoLevel[gender] < listLen - 1:
            self.nextShuffleButton['state'] = DGG.NORMAL
        
        if self.undoLevel[gender] > 0:
            self.prevShuffleButton['state'] = DGG.NORMAL

    def receivedRelease(self, pgs, extraStuff):
        if self.guiIdStates[pgs.guiId] != pgs['value']:
            self.guiIdStates[pgs.guiId] = pgs['value']
            if not self.compositeAction:
                self.storeUndo()

    def receivedAdjust(self, pgs):
        self.guiIdStates[pgs.guiId] = 1

    def trackSliderElement(self, element):
        guiId = element.guiId
        thumbId = element.thumb.guiId
        self.guiIdStates[guiId] = element['value']
        self.accept('release-mouse1-%s' % guiId, self.receivedRelease, extraArgs=[element])
        self.accept('release-mouse1-%s' % thumbId, self.receivedRelease, extraArgs=[element])
    
    def startCompositeAction(self):
        self.compositeAction = 1
    
    def endCompositeAction(self):
        self.compositeAction = 0
        self.storeUndo()
    
    def refresh(self):
        self.pirate.setDNA(self.pirate.style)
        self.pirate.generateHuman(self.pirate.style.gender)
        if self.isNPCEditor or self.wantNPCViewer:
            self.pirate.disableBlend()
            self.pirate.model.setupSelectionChoices('NPC')
        else:
            self.pirate.model.setupSelectionChoices('DEFAULT')
        self.placePirate()
        self.bodyGui.restore()
        self.headGui.restore()
        self.clothesGui.restore()
    
    def playJackDialogOnClothes(self, clothesType):
        if self.inRandomAll:
            return
        
        choice = random.choice(list(range(12)))
        if choice != 0:
            return
        
        optionsLeft = len(self.JSD_CLOTHING[self.pirate.gender][clothesType])
        if optionsLeft:
            if self.lastDialog:
                if self.lastDialog.status() == AudioSound.PLAYING:
                    return

            choice = random.choice(list(range(0, optionsLeft)))
            dialog = self.JSD_CLOTHING[self.pirate.gender][clothesType][choice]
            base.playSfx(dialog)
            self.lastDialog = dialog
            self.JSD_CLOTHING[self.pirate.gender][clothesType].remove(dialog)
    
    def refreshAnim(self):
        self.pirate.loop(AnimList[self.lastAnim])

    def marketingOn(self):
        if self.entered and self.wantMarketingViewer:
            self.guiTopBar.show()
            self.PirateButton.hide()
            self.NPCButton.hide()
            self.NavyButton.hide()
    
    def marketingOff(self):
        if self.entered and self.wantMarketingViewer:
            self.guiTopBar.hide()

    def toggleGUI(self):
        render2d.toggleVis()
        self.pirate.findAllMatches('**/drop*').getPath(1).toggleVis()

