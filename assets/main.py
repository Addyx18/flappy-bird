import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

# Load the button image with transparency
button_img = pygame.image.load("start_button.png").convert_alpha()

# Draw it on the screen

running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))  # Fill the screen with black
    screen.blit(button_img, (100, 100))
    # Update the display
    pygame.display.update()
pygame.display.flip()

