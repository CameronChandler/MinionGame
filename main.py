import pygame
import sys
from player import Player
from turret import Turret
from game_object import HealthMixin

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

class ObjectManager:
        
    def __init__(self):
        self.objects = []

        self.players = {
            1: Player(WIDTH // 2      , HEIGHT // 2, player=1),
            2: Player(WIDTH // 2 + 100, HEIGHT // 2, player=2)
        }
        self.add_object(self.players[1])
        self.add_object(self.players[2])

        self.last_update_time = pygame.time.get_ticks()
        self.pressed_keys = set()

    def add_object(self, obj):
        self.objects.append(obj)

    def remove_object(self, obj):
        if obj in self.objects:
            self.objects.remove(obj)
            del obj

    def update(self, pressed_keys: dict):
        self.pressed_keys = pressed_keys
        current_time = pygame.time.get_ticks()
        self.delta = (current_time - self.last_update_time) / 1_000 # seconds

        for obj in self.objects:
            obj.update(self)
            if isinstance(obj, HealthMixin) and obj.health <= 0:
                self.handle_death(obj)

        self.last_update_time = current_time

    def draw(self, screen):
        for obj in self.objects:
            obj.draw(screen)

            if isinstance(obj, HealthMixin):
                obj.draw_health_bar(screen)

    def handle_death(self, obj):
        """Handle the death of an object, including removal and player rewards."""
        self.remove_object(obj)

    def build_turret(self, x: int, y: int, player: int):
        turret = Turret(x, y, player)
        self.add_object(turret)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Top-Down Character Movement")

background_image = pygame.image.load('assets/background.jpg')
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

object_manager = ObjectManager()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background_image, (0, 0))

    pressed_keys = pygame.key.get_pressed()

    object_manager.update(pressed_keys)
    object_manager.draw(screen)

    pygame.display.flip()
    pygame.time.Clock().tick(FPS)
