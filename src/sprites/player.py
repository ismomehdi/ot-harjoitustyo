import pygame
from services.player_input import player_input
from services.import_images import import_folder
from services.move_character import move_player
from collisions.main_collisions import MainCollisions
from collisions.coin_collisions import apply_coin_collisions


class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups, collision_sprites, coin_sprites):
        super().__init__(groups)

        # Player config
        self.import_player_assets()
        self.frame_index = 0
        self.animation_speed = 0.14
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft=position)

        # Player movement
        self.direction = pygame.math.Vector2()
        self.speed = 8
        self.gravity = 0.7
        self.jump_speed = 17

        # Player status
        self.status = 'idle'
        self.moving_forward = True

        # For collisions
        self.collisions = MainCollisions(collision_sprites, self.direction, self.rect, self.gravity)
        self.coin_sprites = coin_sprites

    def import_player_assets(self):
        path = './src/assets/player_frames/'
        self.animations = {'idle': [], 'run': [], 'jump': [], 'fall': []}

        for animation in self.animations:
            full_path = path + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        animation_frames = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index > len(animation_frames):
            self.frame_index = 0

        image = animation_frames[int(self.frame_index)]
        if self.moving_forward:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image

    def get_player_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
            if self.direction.x == 1:
                self.moving_forward = True
            elif self.direction.x == -1:
                self.moving_forward = False

        elif self.direction.x == 1 and self.collisions.ground():
            self.status = 'run'
            self.moving_forward = True

        elif self.direction.x == -1 and self.collisions.ground():
            self.status = 'run'
            self.moving_forward = False

        elif self.collisions.ground():
            self.status = 'idle'

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self):
        player_input(
            self.direction,
            self.jump_speed,
            self.collisions.ground())

        move_player(self.rect, self.direction, self.speed)
        self.collisions.apply_horizontal_collisions()
        self.collisions.apply_gravity()
        self.collisions.apply_vertical_collisions()
        apply_coin_collisions(self.rect, self.coin_sprites)
        self.get_player_status()
        self.animate()
