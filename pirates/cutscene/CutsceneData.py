from direct.showbase.PythonUtil import POD
from pirates.cutscene.CutsceneActor import *
from pirates.pirate.AvatarTypes import *
from pirates.ship import ShipGlobals
from pirates.piratesbase import PLocalizer
Cutscene1_1_1 = '1.1.1: Jail Break'
Cutscene1_1_2 = '1.1.2: Jail Break (continued)'
Cutscene1_1_5_a = '1.1.5.a: Doggerel Dan and Nell Intro'
Cutscene1_1_5_b = '1.1.5.b: Doggerel Dan and Nell Rush'
Cutscene1_1_5_c = '1.1.5.c: Doggerel Dan and Nell Bye'
Cutscene1_2 = "1.2: Beck's Boat"
Cutscene1_3 = '1.3: Jolly Roger'
Cutscene2_1 = '2.1: Will Turner Sword'
Cutscene2_1_b = '2.1.b: Sword Tut end'
Cutscene2_2 = '2.2: Tia Dalma Compass'
Cutscene2_3 = '2.3: Elizabeth Swan '
Cutscene2_4 = '2.4: Capt Barbossa Intro'
Cutscene2_4_b = '2.4.b: Capt Barbossa Pistol Finish'
Cutscene2_5 = '2.5: Jack Sparrow in Bar'
Cutscene3_1 = '3.1: Sneaking to BlackPearl'
Cutscene3_2 = '3.2: Jack and Joshamee'
Cutscene6_1 = '6.1: Tia Showing Voodoo Doll'
CutsceneNames = [
    Cutscene1_1_1,
    Cutscene1_1_2,
    Cutscene1_1_5_a,
    Cutscene1_1_5_b,
    Cutscene1_1_5_c,
    Cutscene1_2,
    Cutscene1_3,
    Cutscene2_1,
    Cutscene2_1_b,
    Cutscene2_2,
    Cutscene2_3,
    Cutscene2_4,
    Cutscene2_4_b,
    Cutscene2_5,
    Cutscene3_1,
    Cutscene3_2,
    Cutscene6_1]
CutsceneFilenames = {
    Cutscene1_1_1: 'tut_act_1_1_1_jail',
    Cutscene1_1_2: 'tut_act_1_1_2_jail',
    Cutscene1_1_5_a: 'tut_act_1_1_5_a_dan',
    Cutscene1_1_5_b: 'tut_act_1_1_5_b_dan',
    Cutscene1_1_5_c: 'tut_act_1_1_5_c_dan',
    Cutscene1_2: 'tut_act_1_2',
    Cutscene1_3: 'tut_act_1_3_jr',
    Cutscene2_1: 'tut_act_2_1_wt',
    Cutscene2_1_b: 'tut_act_2_1_b_wt',
    Cutscene2_2: 'tut_act_2_2_td',
    Cutscene2_3: 'tut_act_2_3_es',
    Cutscene2_4: 'tut_act_2_4_cb',
    Cutscene2_4_b: 'tut_act_2_4_cb',
    Cutscene2_5: 'tut_act_2_5_js',
    Cutscene3_1: 'tut_act_3_1_bp',
    Cutscene3_2: 'tut_act_3_2_js',
    Cutscene6_1: 'tut_act_6_1_td' }
CutsceneSubtitles = {
  Cutscene1_1_1: [{
    'beginTime': 4,
    'text': PLocalizer.CutSubtitle1_1_1__1
  }],
  Cutscene1_1_2: [{
    'beginTime': 0.5,
    'text': PLocalizer.CutSubtitle1_1_2__1
  }, {
    'beginTime': 2.5,
    'text': PLocalizer.CutSubtitle1_1_2__2
  }, {
    'beginTime': 11.0,
    'text': PLocalizer.CutSubtitle1_1_2__3
  }, {
    'beginTime': 13.9,
    'text': PLocalizer.CutSubtitle1_1_2__4
  }, {
    'beginTime': 19.35,
    'text': PLocalizer.CutSubtitle1_1_2__5
  }, {
    'beginTime': 21.73,
    'text': PLocalizer.CutSubtitle1_1_2__6
  }, {
    'beginTime': 24.3,
    'text': PLocalizer.CutSubtitle1_1_2__7
  }],
  Cutscene1_1_5_a: [{
    'beginTime': 1.4,
    'text': PLocalizer.CutSubtitle1_1_5_a__1
  }, {
    'beginTime': 4.8,
    'text': PLocalizer.CutSubtitle1_1_5_a__2
  }, {
    'beginTime': 10.9,
    'text': PLocalizer.CutSubtitle1_1_5_a__3
  }, {
    'beginTime': 13.2,
    'text': PLocalizer.CutSubtitle1_1_5_a__4,
    'endTime': 17.78
  }, {
    'beginTime': 20.0,
    'text': PLocalizer.CutSubtitle1_1_5_a__5
  }, {
    'beginTime': 21.0,
    'text': PLocalizer.CutSubtitle1_1_5_a__6
  }, {
    'beginTime': 25.71,
    'text': PLocalizer.CutSubtitle1_1_5_a__7
  }],
  Cutscene1_1_5_b: [{
    'beginTime': 0.5,
    'text': PLocalizer.CutSubtitle1_1_5_b__1
  }],
  Cutscene1_1_5_c: [{
    'beginTime': 0.4,
    'text': PLocalizer.CutSubtitle1_1_5_c__1
  }, {
    'beginTime': 2.93,
    'text': PLocalizer.CutSubtitle1_1_5_c__2
  }, {
    'beginTime': 5.7,
    'text': PLocalizer.CutSubtitle1_1_5_c__3
  }, {
    'beginTime': 10.2,
    'text': PLocalizer.CutSubtitle1_1_5_c__4
  }, {
    'beginTime': 13.7,
    'text': PLocalizer.CutSubtitle1_1_5_c__5
  }, {
    'beginTime': 17.9,
    'text': PLocalizer.CutSubtitle1_1_5_c__6
  }, {
    'beginTime': 24.36,
    'text': PLocalizer.CutSubtitle1_1_5_c__7
  }, {
    'beginTime': 26.8,
    'text': PLocalizer.CutSubtitle1_1_5_c__8
  }, {
    'beginTime': 32.2,
    'text': PLocalizer.CutSubtitle1_1_5_c__9
  }, {
    'beginTime': 34.61,
    'text': PLocalizer.CutSubtitle1_1_5_c__10
  }],
  Cutscene1_2: [{
    'beginTime': 1.55,
    'text': PLocalizer.CutSubtitle1_2_a__1
  }, {
    'beginTime': 3.65,
    'text': PLocalizer.CutSubtitle1_2_a__2
  }, {
    'beginTime': 6.47,
    'text': PLocalizer.CutSubtitle1_2_a__3
  }, {
    'beginTime': 10.3,
    'text': PLocalizer.CutSubtitle1_2_b__1
  }, {
    'beginTime': 13.49,
    'text': PLocalizer.CutSubtitle1_2_b__2
  }, {
    'beginTime': 18.36,
    'text': PLocalizer.CutSubtitle1_2_b__3
  }],
  Cutscene1_3: [{
    'beginTime': 0.3,
    'text': PLocalizer.CutSubtitle1_3_a__1
  }, {
    'beginTime': 5.86,
    'text': PLocalizer.CutSubtitle1_3_a__2
  }, {
    'beginTime': 11.45,
    'text': PLocalizer.CutSubtitle1_3_a__3,
    'endTime': 14.22
  }, {
    'beginTime': 16.5,
    'text': PLocalizer.CutSubtitle1_3_a__4
  }, {
    'beginTime': 24.13,
    'text': PLocalizer.CutSubtitle1_3_a__5
  }, {
    'beginTime': 27.7,
    'text': PLocalizer.CutSubtitle1_3_a__6
  }, {
    'beginTime': 31.7,
    'text': PLocalizer.CutSubtitle1_3_a__7,
    'endTime': 35.0
  }, {
    'beginTime': 38.21,
    'text': PLocalizer.CutSubtitle1_3_a__8
  }, {
    'beginTime': 42.6,
    'text': PLocalizer.CutSubtitle1_3_a__9,
    'endTime': 47.65
  }, {
    'beginTime': 51.7,
    'text': PLocalizer.CutSubtitle1_3_a__10
  }, {
    'beginTime': 59.14,
    'text': PLocalizer.CutSubtitle1_3_a__11
  }, {
    'beginTime': 64.6,
    'text': PLocalizer.CutSubtitle1_3_a__12
  }, {
    'beginTime': 74.3,
    'text': PLocalizer.CutSubtitle1_3_a__13
  }],
  Cutscene2_1: [{
    'beginTime': 3.0,
    'text': PLocalizer.CutSubtitle2_1_a__1
  }, {
    'beginTime': 6.18,
    'text': PLocalizer.CutSubtitle2_1_a__2
  }, {
    'beginTime': 11.79,
    'text': PLocalizer.CutSubtitle2_1_a__3
  }, {
    'beginTime': 14.0,
    'text': PLocalizer.CutSubtitle2_1_a__4
  }, {
    'beginTime': 17.02,
    'text': PLocalizer.CutSubtitle2_1_a__5
  }, {
    'beginTime': 18.41,
    'text': PLocalizer.CutSubtitle2_1_a__6
  }, {
    'beginTime': 24.0,
    'text': PLocalizer.CutSubtitle2_1_a__7
  }, {
    'beginTime': 31.45,
    'text': PLocalizer.CutSubtitle2_1_a__8
  }, {
    'beginTime': 33.4,
    'text': PLocalizer.CutSubtitle2_1_a__9
  }],
  Cutscene2_1_b: [{
    'beginTime': 1.2,
    'text': PLocalizer.CutSubtitle2_1_b__1
  }, {
    'beginTime': 3.52,
    'text': PLocalizer.CutSubtitle2_1_b__2
  }, {
    'beginTime': 8.58,
    'text': PLocalizer.CutSubtitle2_1_b__3,
    'endTime': 11.52
  }, {
    'beginTime': 14.1,
    'text': PLocalizer.CutSubtitle2_1_b__4
  }, {
    'beginTime': 18.37,
    'text': PLocalizer.CutSubtitle2_1_b__5
  }, {
    'beginTime': 20.85,
    'text': PLocalizer.CutSubtitle2_1_b__6
  }],
  Cutscene2_2: [{
    'beginTime': 1.9,
    'text': PLocalizer.CutSubtitle2_2__1
  }, {
    'beginTime': 7.37,
    'text': PLocalizer.CutSubtitle2_2__2
  }, {
    'beginTime': 13.7,
    'text': PLocalizer.CutSubtitle2_2__3
  }, {
    'beginTime': 22.82,
    'text': PLocalizer.CutSubtitle2_2__4
  }, {
    'beginTime': 32.66,
    'text': PLocalizer.CutSubtitle2_2__5
  }, {
    'beginTime': 38.64,
    'text': PLocalizer.CutSubtitle2_2__6
  }, {
    'beginTime': 45.1,
    'text': PLocalizer.CutSubtitle2_2__7
  }, {
    'beginTime': 53.52,
    'text': PLocalizer.CutSubtitle2_2__8
  }, {
    'beginTime': 62.7,
    'text': PLocalizer.CutSubtitle2_2__9
  }, {
    'beginTime': 70.11,
    'text': PLocalizer.CutSubtitle2_2__10
  }, {
    'beginTime': 77.67,
    'text': PLocalizer.CutSubtitle2_2__11
  }, {
    'beginTime': 84.92,
    'text': PLocalizer.CutSubtitle2_2__12
  }],
  Cutscene2_3: [{
    'beginTime': 2.1,
    'text': PLocalizer.CutSubtitle2_3__1
  }, {
    'beginTime': 6.26,
    'text': PLocalizer.CutSubtitle2_3__2
  }, {
    'beginTime': 10.13,
    'text': PLocalizer.CutSubtitle2_3__3
  }, {
    'beginTime': 15.4,
    'text': PLocalizer.CutSubtitle2_3__4
  }, {
    'beginTime': 21.26,
    'text': PLocalizer.CutSubtitle2_3__5
  }, {
    'beginTime': 24.68,
    'text': PLocalizer.CutSubtitle2_3__6
  }, {
    'beginTime': 27.75,
    'text': PLocalizer.CutSubtitle2_3__7,
    'endTime': 31.34
  }, {
    'beginTime': 33.1,
    'text': PLocalizer.CutSubtitle2_3__8
  }, {
    'beginTime': 38.15,
    'text': PLocalizer.CutSubtitle2_3__9
  }, {
    'beginTime': 40.64,
    'text': PLocalizer.CutSubtitle2_3__10
  }, {
    'beginTime': 43.48,
    'text': PLocalizer.CutSubtitle2_3__11
  }, {
    'beginTime': 45.5,
    'text': PLocalizer.CutSubtitle2_3__12
  }, {
    'beginTime': 51.11,
    'text': PLocalizer.CutSubtitle2_3__13
  }],
  Cutscene2_4: [{
    'beginTime': 1.6,
    'text': PLocalizer.CutSubtitle2_4_a__1
  }, {
    'beginTime': 3.92,
    'text': PLocalizer.CutSubtitle2_4_a__2
  }, {
    'beginTime': 8.92,
    'text': PLocalizer.CutSubtitle2_4_a__3
  }, {
    'beginTime': 16.91,
    'text': PLocalizer.CutSubtitle2_4_a__4
  }],
  Cutscene2_4_b: [{
    'beginTime': 1.8,
    'text': PLocalizer.CutSubtitle2_4_b__1
  }, {
    'beginTime': 8.32,
    'text': PLocalizer.CutSubtitle2_4_b__2
  }, {
    'beginTime': 14.82,
    'text': PLocalizer.CutSubtitle2_4_b__3
  }, {
    'beginTime': 21.17,
    'text': PLocalizer.CutSubtitle2_4_b__4
  }, {
    'beginTime': 29.0,
    'text': PLocalizer.CutSubtitle2_4_b__5
  }, {
    'beginTime': 35.03,
    'text': PLocalizer.CutSubtitle2_4_b__6
  }, {
    'beginTime': 39.4,
    'text': PLocalizer.CutSubtitle2_4_b__7
  }, {
    'beginTime': 42.97,
    'text': PLocalizer.CutSubtitle2_4_b__8,
    'endTime': 50.23
  }, {
    'beginTime': 54.03,
    'text': PLocalizer.CutSubtitle2_4_b__9,
    'endTime': 58.45
  }, {
    'beginTime': 62.5,
    'text': PLocalizer.CutSubtitle2_4_b__10
  }],
  Cutscene2_5: [{
    'beginTime': 0,
    'text': PLocalizer.CutSubtitle2_5__1
  }, {
    'beginTime': 2.02,
    'text': PLocalizer.CutSubtitle2_5__2
  }, {
    'beginTime': 6.11,
    'text': PLocalizer.CutSubtitle2_5__3
  }, {
    'beginTime': 10.0,
    'text': PLocalizer.CutSubtitle2_5__4
  }, {
    'beginTime': 13.05,
    'text': PLocalizer.CutSubtitle2_5__5
  }, {
    'beginTime': 18.32,
    'text': PLocalizer.CutSubtitle2_5__6
  }, {
    'beginTime': 24.21,
    'text': PLocalizer.CutSubtitle2_5__7
  }, {
    'beginTime': 29.1,
    'text': PLocalizer.CutSubtitle2_5__8
  }, {
    'beginTime': 32.89,
    'text': PLocalizer.CutSubtitle2_5__9
  }, {
    'beginTime': 38.3,
    'text': PLocalizer.CutSubtitle2_5__10
  }, {
    'beginTime': 43.05,
    'text': PLocalizer.CutSubtitle2_5__11,
    'endTime': 46.68
  }, {
    'beginTime': 50.0,
    'text': PLocalizer.CutSubtitle2_5__12
  }, {
    'beginTime': 53.01,
    'text': PLocalizer.CutSubtitle2_5__13
  }, {
    'beginTime': 56.83,
    'text': PLocalizer.CutSubtitle2_5__14
  }],
  Cutscene3_1: [{
    'beginTime': 1.9,
    'text': PLocalizer.CutSubtitle3_1__1
  }, {
    'beginTime': 3.95,
    'text': PLocalizer.CutSubtitle3_1__2
  }, {
    'beginTime': 7.45,
    'text': PLocalizer.CutSubtitle3_1__3
  }, {
    'beginTime': 10.1,
    'text': PLocalizer.CutSubtitle3_1__4
  }, {
    'beginTime': 13.58,
    'text': PLocalizer.CutSubtitle3_1__5
  }, {
    'beginTime': 17.26,
    'text': PLocalizer.CutSubtitle3_1__6
  }, {
    'beginTime': 18.51,
    'text': PLocalizer.CutSubtitle3_1__7
  }, {
    'beginTime': 23.42,
    'text': PLocalizer.CutSubtitle3_1__8
  }, {
    'beginTime': 29.67,
    'text': PLocalizer.CutSubtitle3_1__9
  }, {
    'beginTime': 34.68,
    'text': PLocalizer.CutSubtitle3_1__10
  }, {
    'beginTime': 38.48,
    'text': PLocalizer.CutSubtitle3_1__11
  }, {
    'beginTime': 41.3,
    'text': PLocalizer.CutSubtitle3_1__12
  }, {
    'beginTime': 46.4,
    'text': PLocalizer.CutSubtitle3_1__13
  }, {
    'beginTime': 52.53,
    'text': PLocalizer.CutSubtitle3_1__14
  }, {
    'beginTime': 59.4,
    'text': PLocalizer.CutSubtitle3_1__15
  }, {
    'beginTime': 65.52,
    'text': PLocalizer.CutSubtitle3_1__16
  }, {
    'beginTime': 69.5,
    'text': PLocalizer.CutSubtitle3_1__17
  }],
  Cutscene3_2: [{
    'beginTime': 0,
    'text': PLocalizer.CutSubtitle3_2__1
  }, {
    'beginTime': 4.41,
    'text': PLocalizer.CutSubtitle3_2__2
  }, {
    'beginTime': 8.22,
    'text': PLocalizer.CutSubtitle3_2__3
  }, {
    'beginTime': 14.96,
    'text': PLocalizer.CutSubtitle3_2__4
  }, {
    'beginTime': 20.86,
    'text': PLocalizer.CutSubtitle3_2__5
  }, {
    'beginTime': 26.55,
    'text': PLocalizer.CutSubtitle3_2__6
  }, {
    'beginTime': 29.46,
    'text': PLocalizer.CutSubtitle3_2__7
  }, {
    'beginTime': 31.06,
    'text': PLocalizer.CutSubtitle3_2__8
  }, {
    'beginTime': 35.99,
    'text': PLocalizer.CutSubtitle3_2__9
  }, {
    'beginTime': 38.0,
    'text': PLocalizer.CutSubtitle3_2__10,
    'endTime': 41.6
  }, {
    'beginTime': 43.0,
    'text': PLocalizer.CutSubtitle3_2__11
  }, {
    'beginTime': 45.16,
    'text': PLocalizer.CutSubtitle3_2__12
  }, {
    'beginTime': 51.6,
    'text': PLocalizer.CutSubtitle3_2__13
  }, {
    'beginTime': 54.68,
    'text': PLocalizer.CutSubtitle3_2__14
  }, {
    'beginTime': 59.47,
    'text': PLocalizer.CutSubtitle3_2__15
  }, {
    'beginTime': 64.68,
    'text': PLocalizer.CutSubtitle3_2__16
  }, {
    'beginTime': 69.2,
    'text': PLocalizer.CutSubtitle3_2__17,
    'endTime': 74.6
  }, {
    'beginTime': 79,
    'text': PLocalizer.CutSubtitle3_2__18
  }, {
    'beginTime': 85.11,
    'text': PLocalizer.CutSubtitle3_2__19
  }, {
    'beginTime': 88.92,
    'text': PLocalizer.CutSubtitle3_2__20
  }, {
    'beginTime': 90.26,
    'text': PLocalizer.CutSubtitle3_2__21
  }, {
    'beginTime': 94.73,
    'text': PLocalizer.CutSubtitle3_2__22
  }, {
    'beginTime': 96.58,
    'text': PLocalizer.CutSubtitle3_2__23
  }, {
    'beginTime': 100.46,
    'text': PLocalizer.CutSubtitle3_2__24
  }],
  Cutscene3_2: [{
    'beginTime': 0,
    'text': PLocalizer.CutSubtitle3_2__1
  }, {
    'beginTime': 4.41,
    'text': PLocalizer.CutSubtitle3_2__2
  }],
  Cutscene6_1: [{
    'beginTime': 0,
    'text': PLocalizer.CutSubtitle6_1__1
  }, {
    'beginTime': 3.5,
    'text': PLocalizer.CutSubtitle6_1__2
  }, {
    'beginTime': 6.0,
    'text': PLocalizer.CutSubtitle6_1__3
  }, {
    'beginTime': 9.9,
    'text': PLocalizer.CutSubtitle6_1__4
  }, {
    'beginTime': 12.25,
    'text': PLocalizer.CutSubtitle6_1__5
  }, {
    'beginTime': 14.6,
    'text': PLocalizer.CutSubtitle6_1__6
  }, {
    'beginTime': 18.56,
    'text': PLocalizer.CutSubtitle6_1__7
  }, {
    'beginTime': 21.3,
    'text': PLocalizer.CutSubtitle6_1__8
  }]
}
CutsceneIds = list(CutsceneFilenames.keys())
CutsceneIds.sort()
PRELOADED_CUTSCENE_STAGE1 = [
    Cutscene1_1_2]
PRELOADED_CUTSCENE_STAGE2 = [
    Cutscene1_1_5_a,
    Cutscene1_1_5_c]
PRELOADED_CUTSCENE_STAGE3 = [
    Cutscene1_2,
    Cutscene1_3]
PRELOADED_CUTSCENE_STAGE4 = [
    Cutscene2_1_b]
PRELOADED_CUTSCENE_STAGE5 = [
    Cutscene2_4_b]

class CutsceneDesc(POD):
    DataSet = {
        'id': None,
        'components': tuple(''),
        'actorFunctors': None,
        'soundFile': None,
        'filmSizeHorizontal': 42.667,
        'focalLength': 30}
    
    def __init__(self, *args, **kwArgs):
        POD.__init__(self, *args, **kwArgs)
        self.filename = CutsceneFilenames[self.id]


CutsceneData = {
  Cutscene1_1_1: CutsceneDesc(id = Cutscene1_1_1, components = [''], actorFunctors = [CutJackSparrow, Functor(CutLocalPirate, False)], soundFile = ('audio/cs_tut_1_1_a_js.mp3', ), filmSizeHorizontal = 42.667, focalLength = 50),
  Cutscene1_1_2: CutsceneDesc(id = Cutscene1_1_2, components = [''], actorFunctors = [CutJackSparrow, Functor(CutLocalPirate, False)], soundFile = ('audio/cs_tut_1_1_b_js.mp3', ), filmSizeHorizontal = 42.667, focalLength = 50),
  Cutscene1_1_5_a: CutsceneDesc(id = Cutscene1_1_5_a, components = [''], actorFunctors = [Functor(CutLocalPirate, False), Functor(CutBartenderMmsDoggerel, 1), Functor(CutBartenderFmiNell, 1)], soundFile = ('audio/cs_tut_1_1_5_a_dan.mp3', ), filmSizeHorizontal = 42.667, focalLength = 50),
  Cutscene1_1_5_b: CutsceneDesc(id = Cutscene1_1_5_b, components = [''], actorFunctors = [Functor(CutLocalPirate, False), Functor(CutBartenderMmsDoggerel, 1), Functor(CutBartenderFmiNell, 1)], soundFile = ('audio/cs_tut_1_1_5_b_dan.mp3', ), filmSizeHorizontal = 42.667, focalLength = 50),
  Cutscene1_1_5_c: CutsceneDesc(id = Cutscene1_1_5_c, components = [''], actorFunctors = [Functor(CutLocalPirate, False), Functor(CutBartenderMmsDoggerel, 1), Functor(CutBartenderFmiNell, 1)], soundFile = ('audio/cs_tut_1_1_5_c_dan.mp3', ), filmSizeHorizontal = 42.667, focalLength = 50),
  Cutscene1_2: CutsceneDesc(id = Cutscene1_2, components = ['_dock', '_b_dock'], actorFunctors = [Functor(CutLocalPirate, False), Functor(CutCaptainBeckShort, 1), Functor(CutGenericActor, 'wheel', 'wheel_zero', 'models/props/'), Functor(CutBoat, ShipGlobals.STUMPY_SHIP, PiratesGlobals.PLAYER_TEAM, Vec3(0, 0, 0), 0)], soundFile = ('audio/cs_tut_1_2_dock.mp3', ), filmSizeHorizontal = 42.667, focalLength = 50),
  Cutscene1_3: CutsceneDesc(id = Cutscene1_3, components = ['_a', '_b'], actorFunctors = [CutJollyRoger, Functor(CutLocalPirate, False), Functor(CutGenericActor, 'wheel', 'wheel_zero', 'models/props/'), Functor(CutGenericActor, 'plank', 'plank_zero', 'models/props/'), Functor(CutCaptainBeckShort, 1), Functor(CutSkeleton, EarthUndead[0], 1), Functor(CutSkeleton, EarthUndead[4], 2), Functor(CutSkeleton, EarthUndead[2], 3), Functor(CutBoat, ShipGlobals.STUMPY_SHIP, PiratesGlobals.PLAYER_TEAM, Vec3(0, 0, 0), 1), Functor(CutBoat, ShipGlobals.SKEL_DEATH_OMEN, PiratesGlobals.UNDEAD_TEAM, Vec3(0, 0, 0), 0)], soundFile = ('audio/cs_tut_1_3_jr.mp3', ), filmSizeHorizontal = 42.667, focalLength = 50),
  Cutscene2_1: CutsceneDesc(id = Cutscene2_1, components = [''], actorFunctors = [Functor(CutWillTurner, '1152830677.95jubutler'), Functor(CutLocalPirate, False)], soundFile = ('audio/cs_tut_2_1_a_wt.mp3', ), filmSizeHorizontal = 42.667, focalLength = 72),
  Cutscene2_1_b: CutsceneDesc(id = Cutscene2_1_b, components = [''], actorFunctors = [Functor(CutWillTurner, '1152830677.95jubutler'), Functor(CutLocalPirate, False)], soundFile = ('audio/cs_tut_2_1_b_wt.mp3', ), filmSizeHorizontal = 42.667, focalLength = 35),
  Cutscene2_2: CutsceneDesc(id = Cutscene2_2, components = [''], actorFunctors = [Functor(CutTiaDalma, '1154497344.0jubutlerPR'), Functor(CutLocalPirate, False), Functor(CutBlackGuard1, 1), Functor(CutBlackGuard2, 2), Functor(CutBlackGuard3, 3), CutJollyRoger, Functor(CutSkeleton, EarthUndead[4], 4), Functor(CutSkeleton, EarthUndead[2], 5), Functor(CutGenericActor, 'lantern', 'lantern_zero', 'models/props/'), Functor(CutGenericActor, 'crablegs', 'crablegs_zero', 'models/props/')], soundFile = ('audio/cs_tut_2_2_td.mp3', ), filmSizeHorizontal = 42.667, focalLength = 72),
  Cutscene2_3: CutsceneDesc(id = Cutscene2_3, components = [''], actorFunctors = [Functor(CutElizabethSwan, '1171325040.86MAsaduzz'), Functor(CutLocalPirate, False), Functor(CutGenericActor, 'paper', 'paper_zero', 'models/props/')], soundFile = ('audio/cs_tut_2_3_es.mp3', ), filmSizeHorizontal = 42.667, focalLength = 32),
  Cutscene2_4: CutsceneDesc(id = Cutscene2_4, components = ['_a'], actorFunctors = [Functor(CutCaptBarbossa, '1172618710.78sdnaik'), Functor(CutLocalPirate, False), Functor(CutGenericActor, 'monkey', 'monkey_hi', 'models/char/')], soundFile = ('audio/cs_tut_2_4_a_cb.mp3', ), filmSizeHorizontal = 42.667, focalLength = 50),
  Cutscene2_4_b: CutsceneDesc(id = Cutscene2_4_b, components = ['_b', '_c'], actorFunctors = [Functor(CutCaptBarbossa, '1172618710.78sdnaik'), Functor(CutLocalPirate, True), Functor(CutGenericActor, 'monkey', 'monkey_hi', 'models/char/')], soundFile = ('audio/cs_tut_2_4_b_cb.mp3', ), filmSizeHorizontal = 42.667, focalLength = 50),
  Cutscene2_5: CutsceneDesc(id = Cutscene2_5, components = [''], actorFunctors = [CutJackSparrow, Functor(CutLocalPirate, False), Functor(CutGenericActor, 'mug', 'mug_zero', 'models/props/'), Functor(CutBartenderPear, 1)], soundFile = ('audio/cs_tut_2_5_js.mp3', ), filmSizeHorizontal = 42.667, focalLength = 30),
  Cutscene3_1: CutsceneDesc(id = Cutscene3_1, components = [''], actorFunctors = [Functor(CutLocalPirate, False), Functor(CutGenericActor, 'open_paper', 'open_paper_zero', 'models/props/'), Functor(CutNavyMtpPeter, 1), Functor(CutNavyMtpJeff, 2), Functor(CutCaptainBeckShort, 3), Functor(CutBartenderMmsDoggerel, 4), Functor(CutBoat, ShipGlobals.WARSHIPL3, PiratesGlobals.NAVY_TEAM, Vec3(0, 0, 0), 0, rootScale = 2.0), Functor(CutBoat, ShipGlobals.BLACK_PEARL, PiratesGlobals.PLAYER_TEAM, Vec3(0, 0, 0), 0)], soundFile = ('audio/cs_tut_3_1_bp.mp3', ), filmSizeHorizontal = 42.667, focalLength = 50),
  Cutscene3_2: CutsceneDesc(id = Cutscene3_2, components = [''], actorFunctors = [CutJackSparrow, Functor(CutLocalPirate, False), Functor(CutJoshGibbs, '1168022298.47Shochet')], soundFile = ('audio/cs_tut_3_2_js.mp3', ), filmSizeHorizontal = 42.667, focalLength = 50),
  Cutscene6_1: CutsceneDesc(id = Cutscene6_1, components = [''], actorFunctors = [Functor(CutTiaDalma, '1154497344.0jubutlerPR'), Functor(CutLocalPirate, False)], soundFile = ('audio/cs_tut_6_1_td.mp3', ), filmSizeHorizontal = 42.667, focalLength = 50)
}
