from enum import Enum

class GameState(Enum):
    MENU      = 1
    PLAY      = 2
    PAUSE     = 3
    GAME_OVER = 4

GAME_STATE = GameState.MENU

loaded = False
