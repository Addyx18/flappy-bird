import pygame
import config
from config import GameState
from game_engine import draw_menu, game_over, play_game, update_window

pygame.init()

while True:

    match config.GAME_STATE:
        case GameState.MENU:
            draw_menu()

        case GameState.PLAY:
            play_game()

        case GameState.GAME_OVER:
            game_over()

    update_window()
