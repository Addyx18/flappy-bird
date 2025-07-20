import pygame
import random
from itertools import zip_longest


def exit_game():
    pygame.quit()
    sys.exit()


def is_collided(bird, normal_pipes, inverted_pipes):
    score = 0
    bird_mask = pygame.mask.from_surface(bird.bird)
    bird_rect = bird.bird.get_rect(topleft=(bird.x, bird.y))
    
    for pipe1, pipe2 in zip_longest(normal_pipes, inverted_pipes):
        if pipe1 and pipe2:
            mask1 = pygame.mask.from_surface(pipe1.pipe)
            mask2 = pygame.mask.from_surface(pipe2.pipe)

            rect1 = pipe1.pipe.get_rect(topleft=(pipe1.x, pipe1.y))
            rect2 = pipe2.pipe.get_rect(topleft=(pipe2.x, pipe2.y))

            offset1 = (bird_rect.left - rect1.left, bird_rect.top - rect1.top)
            offset2 = (bird_rect.left - rect2.left, bird_rect.top - rect2.top)
            if mask1.overlap(bird_mask, offset1) or mask2.overlap(bird_mask, offset2):
                return True, score

            if bird.x > pipe1.x + pipe1.width and bird.x > pipe2.x + pipe2.width:
                score+=1
    return False, score

# Functions for managing scores

def save_to_file(score):
    with open('score.txt', 'a') as file:
        file.write(f'{score}\n')

def load_scores_from_file():
    try:
        with open('score.txt', 'r') as file:
            scores = [int(line.strip()) for line in file if line.strip().isdigit()]
        return scores
    except FileNotFoundError:
        return []
    except ValueError:
        return []

def get_high_score():
    scores = load_scores_from_file()
    if scores:
        return max(scores)
    return 0
