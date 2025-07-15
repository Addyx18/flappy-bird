import pygame
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600;
COLORS = ['blue', 'purple', 'red', 'tomato', 'yellow', 'green', 'white', 'black', 'cyan']
BG_IMAGE = pygame.transform.scale((pygame.image.load('./assets/background.jpg')), (WINDOW_WIDTH, WINDOW_HEIGHT))
BAR_IMAGE = pygame.image.load('./assets/pipe.png')
