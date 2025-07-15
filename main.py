import pygame
import sys
import random
from pygame.locals import *
from utils import random_bar
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, COLORS, BG_IMAGE, BAR_IMAGE
from button import Button

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Flappy Bird Game")
font = pygame.font.Font(None, 20)
clock = pygame.time.Clock()

def on_button_press():
    print("Button pressed")

random_color = COLORS[1]
button = Button(10, 20, 150, 50, "Hello, world", on_button_press)

bg_x = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            random_color = random.choice(COLORS)
            if button.is_hovered(pygame.mouse.get_pos()):
                button.on_click()

    bg_x -= 1
    if bg_x <= -WINDOW_WIDTH:
        bg_x = 0

    screen.blit(BG_IMAGE, (bg_x, 0))
    screen.blit(BG_IMAGE, (bg_x + WINDOW_WIDTH, 0))

    button.process(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

