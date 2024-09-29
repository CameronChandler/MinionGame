import pygame
import sys
from player import Player

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
FPS = 60

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Top-Down Character Movement")


player = Player(WIDTH // 2, HEIGHT // 2, 'assets/player1.png')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    player.move()

    screen.fill(WHITE)

    player.draw(screen)

    # Update the display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(FPS)
