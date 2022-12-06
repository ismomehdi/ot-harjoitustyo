import pygame
from maps import TILE_SIZE
from level import level_rect
from services.player_input import player_input
from services.import_images import import_folder


class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups, collision_sprites, coin_sprites):
        super().__init__(groups)

        self.import_player_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['idle'][self.frame_index]
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=position)

        self.direction = pygame.math.Vector2()
        self.speed = 8
        self.gravity = 0.7
        self.jump_speed = 17
        self.player_on_ground = False

        # These are the sprites player can collide with
        self.collision_sprites = collision_sprites
        self.coin_sprites = coin_sprites
    
    def import_player_assets(self):
        path = './src/assets/player_frames/'
        self.animations = {'idle': [], 'run': [], 'jump': []}

        for animation in self.animations.keys():
            full_path = path + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        animation_frames = self.animations['idle']

        self.frame_index += self.animation_speed
        if self.frame_index > len(animation_frames):
            self.frame_index = 0
        
        self.image = animation_frames[int(self.frame_index)]
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))

    def horizontal_collisions(self):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                # The player is moving left
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right
                # The player is moving right
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left

    def vertical_collisions(self):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                # The player is moving up
                if self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0
                # The player is moving down
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.player_on_ground = True

        # The player is not on ground
        if self.player_on_ground and self.direction.y != 0:
            self.player_on_ground = False

    def coin_collisions(self):
        for sprite in self.coin_sprites:
            if sprite.rect.colliderect(self.rect):
                sprite.kill()

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def move_player(self):
        self.rect.x += self.direction.x * self.speed
        self.rect.clamp_ip(level_rect)

    def update(self):
        player_input(
            self.direction,
            self.jump_speed,
            self.player_on_ground)

        self.move_player()
        self.horizontal_collisions()
        self.apply_gravity()
        self.vertical_collisions()
        self.coin_collisions()
        self.animate()
