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
    image_size = (35, 50)

    def __init__(self, x: int, y: int, player: int):
        self.controls = CONTROLS[player]
        image_path = 'assets/player1.png' if player == 1 else 'assets/player2.jpg'
        self.original_image = pygame.image.load(image_path)
        self.original_image = pygame.transform.scale(self.original_image, self.image_size)
        self.rect = self.original_image.get_rect(center=(x, y))
        self.facing_right = True if player == 1 else False

    def update(self, pressed_keys: dict):
        self.move(pressed_keys)

    def move(self, pressed_keys: dict):
        move_x, move_y = 0, 0
        if pressed_keys[self.controls['LEFT']]:
            move_x = -1
            self.facing_right = False
        if pressed_keys[self.controls['RIGHT']]:
            move_x = 1
            self.facing_right = True
        if pressed_keys[self.controls['UP']]:
            move_y = -1
        if pressed_keys[self.controls['DOWN']]:
            move_y = 1

        if move_x != 0 or move_y != 0:
            magnitude = (move_x ** 2 + move_y ** 2)**0.5
            move_x /= magnitude
            move_y /= magnitude

        self.rect.x += move_x * self.speed
        self.rect.y += move_y * self.speed

    def draw(self, surface):
        self.final_image = pygame.transform.flip(self.original_image, flip_x=not self.facing_right, flip_y=False)
        surface.blit(self.final_image, self.rect)