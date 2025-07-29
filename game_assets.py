from config import resource_path
from constants import WINDOW_WIDTH, WINDOW_HEIGHT

import pygame
pygame.init()

GROUND_IMAGE = pygame.image.load(resource_path('./assets/base.jfif'))
GROUND_IMAGE = pygame.transform.scale(GROUND_IMAGE, (WINDOW_WIDTH, GROUND_IMAGE.get_rect().height))
BG_IMAGE = pygame.transform.scale((pygame.image.load(resource_path('./assets/background.jpg'))), (WINDOW_WIDTH, WINDOW_HEIGHT))

BAR_IMAGE = pygame.image.load(resource_path('./assets/pipe.png'))
TITLE_IMAGE = pygame.image.load(resource_path('./assets/message.png'))
MENU_BACKGROUND = pygame.transform.scale((pygame.image.load(resource_path('./assets/bg-menu.jpg'))), (WINDOW_WIDTH, WINDOW_HEIGHT))
GAME_OVER_BACKGROUND = pygame.image.load(resource_path('./assets/game_over.png'))



BIRD_IMAGE = pygame.image.load(resource_path('./assets/bird.png'))
BIRD_FLAP_SOUND = pygame.mixer.Sound(resource_path('./assets/audio/wing.wav'))
BIRD_HIT_SOUND  = pygame.mixer.Sound(resource_path('./assets/audio/hit.wav'))
BIRD_POINT_SOUND = pygame.mixer.Sound(resource_path('./assets/audio/point.wav'))
BIRD_HIT_SOUND = pygame.mixer.Sound(resource_path('./assets/audio/hit.wav'))


PLAY_SPRITE_IMAGE = pygame.image.load(resource_path('./assets/play_sprite.png'))
SCORE_SPRITE_IMAGE = pygame.image.load(resource_path('./assets/high_score_sprite.png'))
EXIT_SPRITE_IMAGE = pygame.image.load(resource_path('./assets/exit_sprite.png'))

