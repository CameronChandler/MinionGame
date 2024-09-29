import pygame

class Turret:
    image_size = (35, 35)

    def __init__(self, x: int, y: int, player: int):
        image_path = 'assets/player1.png' if player == 1 else 'assets/player2.jpg'
        self.original_image = pygame.image.load(image_path)
        self.original_image = pygame.transform.scale(self.original_image, self.image_size)
        self.rect = self.original_image.get_rect(center=(x, y))

    def update(self, object_manager):
        pass

    def draw(self, surface):
        self.final_image = self.original_image
        surface.blit(self.final_image, self.rect)