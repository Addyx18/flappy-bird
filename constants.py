import pygame
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600;

COLORS = {'blue': (0, 0, 255), 'black': (0, 0, 0), 'white': (255, 255, 255), 'red': (255, 0, 0), 'green': (0, 255, 0), 'yellow': (255, 255, 0)}
BG_IMAGE = pygame.transform.scale((pygame.image.load('./assets/background.jpg')), (WINDOW_WIDTH, WINDOW_HEIGHT))

GROUND_IMAGE = pygame.image.load('./assets/base.jfif')
GROUND_IMAGE = pygame.transform.scale(GROUND_IMAGE, (WINDOW_WIDTH, GROUND_IMAGE.get_rect().height))

BAR_IMAGE = pygame.image.load('./assets/pipe.png')
BIRD_IMAGE = pygame.image.load('./assets/bird.png')


MENU_BACKGROUND = pygame.transform.scale((pygame.image.load('./assets/bg-menu.jpg')), (WINDOW_WIDTH, WINDOW_HEIGHT))

GAME_OVER_BACKGROUND = pygame.image.load('./assets/game_over.png')

