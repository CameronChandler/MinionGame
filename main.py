import pygame
import sys
from player import Player

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Top-Down Character Movement")

background_image = pygame.image.load('assets/background.jpg')
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

player1 = Player(WIDTH // 2      , HEIGHT // 2, player=1)
player2 = Player(WIDTH // 2 + 100, HEIGHT // 2, player=2)

game_objects: list = [player1, player2]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background_image, (0, 0))

    pressed_keys = pygame.key.get_pressed()

    for obj in game_objects:
        obj.update(pressed_keys)
        obj.draw(screen)

    pygame.display.flip()
    pygame.time.Clock().tick(FPS)
