from pandac.PandaModules import *
from direct.showbase import PythonUtil
import enum
TARGET_POS = {
    4: Vec3(0.85, 0, 0.0),
    3: Vec3(0.6, 0, 0.42),
    2: Vec3(0.27, 0, 0.6),
    1: Vec3(-0.08, 0, 0.63),
    0: Vec3(-0.59, 0, 0.29)}
class FACES(enum.Enum):
    DEALER = 1
    ONE = 2
    TWO = 3
    THREE = 4
    FOUR = 5
    FIVE = 6
    SIX = 7
    SEVEN = 8
FACE_SPOT_POS = {
    FACES.DEALER: (-1.0, 0, 0.6),
    FACES.ONE: (-1.15, 0, -0.3),
    FACES.TWO: (-0.96, 0, -0.61),
    FACES.THREE: (-0.65, 0, -0.8),
    FACES.FOUR: (0.65, 0, -0.8),
    FACES.FIVE: (0.96, 0, -0.61),
    FACES.SIX: (1.15, 0, -0.3)}
FINGER_RANGES = [
    [
        -26,
        -16],
    [
        -3,
        8],
    [
        23,
        32],
    [
        52,
        60]]
class PLAYER_ACTIONS(enum.Enum):
    JoinGame = 1
    UnjoinGame = 2
    RejoinGame = 3
    Resign = 4
    Leave = 5
    Continue_ = 6
    Progress = 7
class GAME_ACTIONS(enum.Enum):
    AskForContinue = 1
    NotifyOfWin = 2
    NotifyOfLoss = 3
class CONTINUE_OPTIONS(enum.Enum):
    Resign = 1
    Continue_ = 2
    Rejoin = 3
    Leave = 4
GameTimeDelay = 5
RoundTimeDelay = 5
RoundTimeLimit = 90
RoundContinueWait = 10
