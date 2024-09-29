import pygame
import sys
from player import Player

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Top-Down Character Movement")

player = Player(WIDTH // 2, HEIGHT // 2, player=1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pressed_keys = pygame.key.get_pressed()

    player.move(pressed_keys)

    screen.fill(WHITE)

    player.draw(screen)

    # Update the display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(FPS)
