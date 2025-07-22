from constants import WINDOW_HEIGHT, WINDOW_WIDTH
import pygame

GRAVITY = 0.2
FLAP_STRENGTH = -4
MAX_FALL_SPEED = 10

class Bird:
    def __init__(self, x=WINDOW_WIDTH/2, y=WINDOW_HEIGHT/2):
        self.x = x
        self.y = y
        self.image = pygame.image.load('./assets/bird.png').convert_alpha()
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        scale_factor = 1.0
        self.bird = pygame.transform.scale(self.image, (int(self.width * scale_factor), int(self.height * scale_factor)))
        self.velocity = 0

    def update_and_draw(self, screen, keyUp=False):
        if keyUp:
            self.velocity = FLAP_STRENGTH

        self.velocity += GRAVITY

        if self.velocity > MAX_FALL_SPEED:
            self.velocity = MAX_FALL_SPEED

        self.y += self.velocity

        screen.blit(self.bird, (self.x, self.y))
