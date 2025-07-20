from constants import WINDOW_HEIGHT, WINDOW_WIDTH
import pygame

class Bird():

    def __init__(self, x=WINDOW_WIDTH/2, y=WINDOW_HEIGHT/2):
        self.x = x
        self.y = y
        self.image = pygame.image.load('./assets/bird.png')
        self.bird = pygame.transform.scale(self.image, (self.image.get_rect().width + 5, self.image.get_rect().height + 5))
        self.score = 0



    def update_and_draw(self, screen, keyUp=False):
        if keyUp:
            self.y += -30 
        else: self.y-= -2
        screen.blit(self.bird, (self.x, self.y))



