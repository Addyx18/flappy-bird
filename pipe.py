import pygame
import random
from constants import WINDOW_WIDTH, WINDOW_HEIGHT
from game_assets import BAR_IMAGE

class Pipe():
    def __init__(self, upside_down=True):
        self.height = random.randint(260, 280)                                                                # Height of the pipe
        self.speed = 2
        self.x = WINDOW_WIDTH + random.randint(100, 101)                                                      # Horizontal position of the pipe
        self.scored = False
        self.y = -5  if upside_down else WINDOW_HEIGHT - self.height                                          # Vertical position of the pipe
        self.image = BAR_IMAGE.convert_alpha()
        self.width = BAR_IMAGE.get_rect().width
        self.pipe = pygame.transform.rotate(pygame.transform.scale(self.image, (self.width, self.height)), 180) if upside_down else pygame.transform.scale(self.image, (self.width, self.height))

    def update_and_draw(self, screen):
        self.x -= self.speed
        screen.blit(self.pipe, (self.x, self.y))

    def off_screen(self):
        return self.x + self.width < 0


class PipeList():
    def __init__(self):
        self.pipes = []

    def add_pipe(self, pipe):
        self.pipes.append(pipe)

    def update_and_draw(self, screen):
        for pipe in self.pipes:
            pipe.update_and_draw(screen)

    def remove_off_screen_pipes(self):
        self.pipes = [pipe for pipe in self.pipes if not pipe.off_screen()]

    def __iter__(self):
        return iter(self.pipes)
