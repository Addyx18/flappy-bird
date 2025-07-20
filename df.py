import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 800))
clock = pygame.time.Clock()

# Game states
MENU = "menu"
GAME = "game"
SCORES = "scores"
state = MENU

# Load your button images here (from sprite sheet or separate files)
play_button = pygame.Rect(200, 250, 200, 60)
score_button = pygame.Rect(200, 350, 200, 60)
exit_button = pygame.Rect(200, 450, 200, 60)

def draw_menu():
    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (100, 200, 255), play_button)
    pygame.draw.rect(screen, (100, 255, 200), score_button)
    pygame.draw.rect(screen, (255, 100, 100), exit_button)

    font = pygame.font.SysFont(None, 40)
    screen.blit(font.render("Play", True, (0, 0, 0)), (play_button.x + 70, play_button.y + 15))
    screen.blit(font.render("Scores", True, (0, 0, 0)), (score_button.x + 55, score_button.y + 15))
    screen.blit(font.render("Exit", True, (0, 0, 0)), (exit_button.x + 70, exit_button.y + 15))

def run_game():
    # Replace with your actual Flappy Bird game logic
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont(None, 50)
    screen.blit(font.render("Flappy Bird Running...", True, (255, 255, 255)), (100, 350))

def draw_scores():
    screen.fill((50, 50, 50))
    font = pygame.font.SysFont(None, 50)
    screen.blit(font.render("High Scores Coming Soon!", True, (255, 255, 255)), (100, 350))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if state == MENU:
                if play_button.collidepoint(event.pos):
                    state = GAME
                elif score_button.collidepoint(event.pos):
                    state = SCORES
                elif exit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

    # State-based rendering
    if state == MENU:
        draw_menu()
    elif state == GAME:
        run_game()
    elif state == SCORES:
        draw_scores()

    pygame.display.flip()
    clock.tick(60)

