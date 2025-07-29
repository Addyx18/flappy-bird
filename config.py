from enum import Enum
import os
import sys

class GameState(Enum):
    MENU      = 1
    PLAY      = 2
    PAUSE     = 3
    GAME_OVER = 4

GAME_STATE = GameState.MENU

loaded = False



def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller """
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

