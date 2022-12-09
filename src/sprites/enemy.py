import pygame
from config.sprite_sizes import TILE_SIZE
from level import level_rect
from collisions.main_collisions import MainCollisions
from services.import_images import import_folder

class Enemy(pygame.sprite.Sprite):
    def __init__(self, position, groups, collision_sprites, player_sprite):
        super().__init__(groups)

        # Enemy config
        self.import_enemy_assets()
        self.frame_index = 0
        self.animation_speed = 0.14
        self.image = self.animations['run'][self.frame_index]
        self.rect = self.image.get_rect(topleft=position)
        self.gravity = 0.7

        # Enemy starting position and area size for movement
        self.starting_pos_x = position[0]
        self.starting_pos_y = position[1]
        self.area_size = TILE_SIZE * 20

        # Enemy movement
        self.direction = pygame.math.Vector2()
        self.speed = 2
        self.chase_speed = 100

        # Enemy status
        self.status = 'run'
        self.moving_forward = True

        # For collisions
        self.collisions = MainCollisions(
            collision_sprites, self.direction, self.rect)

        # Player sprite group for tracking the player
        self.player = player_sprite


    def move_enemy(self):
        # This defines the area the enemy can move in
        if self.rect.x < self.starting_pos_x:
            self.direction.x *= -1  
        elif self.rect.x > self.starting_pos_x + self.area_size:
            self.direction.x *= -1

        # This makes the enemy chase the player if they are in the enemy's area
        if self.starting_pos_x < self.player.sprite.rect.x \
            < self.starting_pos_x + self.area_size:
                if self.player.sprite.rect.x - self.chase_speed > self.rect.x:
                    self.direction.x = 1
                if self.player.sprite.rect.x + self.chase_speed < self.rect.x:
                    self.direction.x = -1
    
        self.rect.x += self.direction.x * self.speed
        self.rect.clamp_ip(level_rect)

    def import_enemy_assets(self):
        path = './src/assets/enemy_frames/'
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

    def get_enemy_status(self):
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
        self.move_enemy()
        self.collisions.apply_horizontal_collisions()
        self.apply_gravity()
        self.collisions.apply_vertical_collisions()
        self.get_enemy_status()
        self.animate()
