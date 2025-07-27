from constants import WINDOW_WIDTH, WINDOW_HEIGHT, COLORS, BG_IMAGE, GROUND_IMAGE, GAME_OVER_BACKGROUND, BUTTON_HEIGHT, BUTTON_WIDTH, TITLE_IMAGE
from pipe import Pipe, PipeList
import config
from config import GameState
from utils import is_collided, save_to_file, get_high_score
from bird import Bird
import pygame
import sys

clock = pygame.time.Clock()
pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Flappy Bird Game")
font = pygame.font.Font(None, 50)

bird = Bird()

user_score = 0
loaded = False

score_button_idx    = 0
play_button_idx     = 0
exit_button_idx     = 0

normal_pipes = PipeList()
inverted_pipes = PipeList()

pipe_time = 0
pipe_interval = 1500

def game_over():
        screen.blit(BG_IMAGE, (0, 0))
        game_over_image = GAME_OVER_BACKGROUND.convert_alpha()
        screen.blit(game_over_image, (WINDOW_WIDTH // 2 - game_over_image.get_width() // 2, WINDOW_HEIGHT // 2 - game_over_image.get_height() // 2))
        high_score = get_high_score()

        user_score_text = font.render(f'{user_score}', True, COLORS['black'])
        high_score_text = font.render(f'{high_score}', True, COLORS['black'])

        screen.blit(user_score_text, (WINDOW_WIDTH // 2 + 80, WINDOW_HEIGHT // 2 + game_over_image.get_height() // 2 - 275))
        screen.blit(high_score_text, (WINDOW_WIDTH // 2 + 80, WINDOW_HEIGHT // 2 + game_over_image.get_height() // 2 - 180))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    config.GAME_STATE = GameState.MENU

        normal_pipes.pipes.clear()
        inverted_pipes.pipes.clear()


def draw_menu():
    global play_button_idx, score_button_idx, exit_button_idx, user_score
    user_score = 0
    screen.blit(BG_IMAGE, (0, 0))

    screen.blit(TITLE_IMAGE, (WINDOW_WIDTH // 2 - TITLE_IMAGE.get_width() // 2, 50))


    play_sprite_sheet = pygame.image.load('./assets/play_sprite.png').convert_alpha()
    score_sprite_sheet = pygame.image.load('./assets/high_score_sprite.png').convert_alpha()
    exit_sprite_sheet = pygame.image.load('./assets/exit_sprite.png').convert_alpha()


    play_button_state = []
    for i in range(3):
        x = i * BUTTON_WIDTH
        sub_image = play_sprite_sheet.subsurface(pygame.Rect(x, 0, BUTTON_WIDTH, BUTTON_HEIGHT)).copy()
        play_button_state.append(sub_image)



    score_button_state = []
    for i in range(3):
        x = i * BUTTON_WIDTH
        sub_image = score_sprite_sheet.subsurface(pygame.Rect(x, 0, BUTTON_WIDTH, BUTTON_HEIGHT)).copy()
        score_button_state.append(sub_image)


    exit_button_state = []
    for i in range(3):
        x = i * BUTTON_WIDTH
        sub_image = exit_sprite_sheet.subsurface(pygame.Rect(x, 0, BUTTON_WIDTH, BUTTON_HEIGHT)).copy()
        exit_button_state.append(sub_image)



    # Button rect
    play_button_pos = (480, 280)
    play_button_rect = pygame.Rect(play_button_pos, (BUTTON_WIDTH, BUTTON_HEIGHT))


    # Button rect
    score_button_pos = (480, 390)
    score_button_rect = pygame.Rect(score_button_pos, (BUTTON_WIDTH, BUTTON_HEIGHT))


    # Button rect
    exit_button_pos = (480, 500)
    exit_button_rect = pygame.Rect(exit_button_pos, (BUTTON_WIDTH, BUTTON_HEIGHT))


    # Draw the buttons
    screen.blit(play_button_state[play_button_idx], play_button_pos)
    screen.blit(score_button_state[score_button_idx], score_button_pos)
    screen.blit(exit_button_state[exit_button_idx], exit_button_pos)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        elif event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()

            if play_button_rect.collidepoint(pos):
                play_button_idx = 1

            elif score_button_rect.collidepoint(pos):
                score_button_idx = 1

            elif exit_button_rect.collidepoint(pos):
                exit_button_idx = 1
            else:
                play_button_idx = 0
                score_button_idx = 0
                exit_button_idx = 0

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if play_button_rect.collidepoint(pos):
                play_button_idx = 2
                bird.reset()
                config.GAME_STATE = GameState.PLAY
                print("yes")

            elif score_button_rect.collidepoint(pos):
                score_button_idx = 2

            elif exit_button_rect.collidepoint(pos):
                exit_button_idx = 2
                pygame.quit()
                sys.exit()


def play_game():
    global pipe_time, pipe_interval, user_score

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird.update_and_draw(screen, True)

    current_time = pygame.time.get_ticks()

    if current_time - pipe_time > pipe_interval:
        pipe_time = current_time

        # Add new pipes
        inverted_pipes.add_pipe(Pipe(True))
        normal_pipes.add_pipe(Pipe(False))

    screen.blit(BG_IMAGE, (0, 0))

    # Display pipes
    normal_pipes.update_and_draw(screen)
    inverted_pipes.update_and_draw(screen)

    is_crashed, score = is_collided(bird, normal_pipes, inverted_pipes)

    print(user_score)
    if is_crashed:
        config.GAME_STATE = GameState.GAME_OVER
        print("carshed")
        # write score to a file
        save_to_file(user_score)
    else:
        user_score += score


    # Display Base
    screen.blit(GROUND_IMAGE, (0, WINDOW_HEIGHT - GROUND_IMAGE.get_rect().height))
    bird.update_and_draw(screen)


    # Cleaning up the pipes
    inverted_pipes.remove_off_screen_pipes()
    normal_pipes.remove_off_screen_pipes()

    clock.tick(60)



def update_window():
    if pygame.display.get_init():
        pygame.display.flip()
