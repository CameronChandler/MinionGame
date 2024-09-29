import pygame

CONTROLS = {
    1: {
        'UP': pygame.K_w,
        'DOWN': pygame.K_s,
        'LEFT': pygame.K_a,
        'RIGHT': pygame.K_d,
        'ABILITY': pygame.K_1
    },
    2: {
        'UP': pygame.K_UP,
        'DOWN': pygame.K_DOWN ,
        'LEFT': pygame.K_LEFT,
        'RIGHT': pygame.K_RIGHT,
        'ABILITY': pygame.K_COMMA
    }
}

class Player:
    speed = 500
    image_size = (35, 50)
    ability_cooldown = 5 #seconds

    def __init__(self, x: int, y: int, player: int):
        self.player = player
        self.controls = CONTROLS[player]
        image_path = 'assets/player1.png' if player == 1 else 'assets/player2.jpg'
        self.original_image = pygame.image.load(image_path)
        self.original_image = pygame.transform.scale(self.original_image, self.image_size)
        self.rect = self.original_image.get_rect(center=(x, y))
        self.facing_right = True if player == 1 else False
        self.time_until_ability_ready = 0

    def update(self, object_manager):
        self.move(object_manager)

        # Handle turret building
        if object_manager.pressed_keys[self.controls['ABILITY']] and self.time_until_ability_ready <= 0:
            object_manager.build_turret(self.rect.x, self.rect.y, self.player)
            self.time_until_ability_ready = self.ability_cooldown

        self.time_until_ability_ready -= object_manager.delta

    def move(self, object_manager):
        move_x, move_y = 0, 0
        if object_manager.pressed_keys[self.controls['LEFT']]:
            move_x = -1
            self.facing_right = False
        if object_manager.pressed_keys[self.controls['RIGHT']]:
            move_x = 1
            self.facing_right = True
        if object_manager.pressed_keys[self.controls['UP']]:
            move_y = -1
        if object_manager.pressed_keys[self.controls['DOWN']]:
            move_y = 1

        if move_x != 0 or move_y != 0:
            magnitude = (move_x ** 2 + move_y ** 2)**0.5
            move_x /= magnitude
            move_y /= magnitude

        self.rect.x += move_x * self.speed * object_manager.delta
        self.rect.y += move_y * self.speed * object_manager.delta

    def draw(self, surface):
        self.final_image = pygame.transform.flip(self.original_image, flip_x=not self.facing_right, flip_y=False)
        surface.blit(self.final_image, self.rect)