import pygame

CONTROLS = {
    1: {
        'UP': pygame.K_w,
        'DOWN': pygame.K_s,
        'LEFT': pygame.K_a,
        'RIGHT': pygame.K_d,
    },
    2: {
        'UP': pygame.K_UP,
        'DOWN': pygame.K_DOWN ,
        'LEFT': pygame.K_LEFT,
        'RIGHT': pygame.K_RIGHT,

    }
}

class Player:
    speed = 5

    def __init__(self, x: int, y: int, player: int):
        self.controls = CONTROLS[player]
        image_path = 'assets/player1.png' if player == 1 else 'assets/player2.png'
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=(x, y))

    def move(self, pressed_keys: dict):
        move_x, move_y = 0, 0
        if pressed_keys[pygame.K_LEFT]:
            move_x = -1
        if pressed_keys[pygame.K_RIGHT]:
            move_x = 1
        if pressed_keys[pygame.K_UP]:
            move_y = -1
        if pressed_keys[pygame.K_DOWN]:
            move_y = 1

        if move_x != 0 or move_y != 0:
            magnitude = (move_x ** 2 + move_y ** 2)**0.5
            move_x /= magnitude
            move_y /= magnitude

        self.rect.x += move_x * self.speed
        self.rect.y += move_y * self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)