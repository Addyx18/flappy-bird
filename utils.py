import pygame
import random
from constants import BAR_IMAGE


def random_bar():
    height = random.randint(20, 30)
    width = BAR_IMAGE.get_rect().width
    image = pygame.transform.scale(BAR_IMAGE, (width, height))
    return image


