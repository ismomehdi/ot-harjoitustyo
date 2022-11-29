import pygame
from maps import TILE_SIZE
from level import level_rect
from services.player_input import player_input


class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups, collision_sprites, coin_sprites):
        super().__init__(groups)

        # Player configuration
        player_size_x = (TILE_SIZE * 2)
        player_size_y = (TILE_SIZE * 2) * 0.9347826086956522

        self. image = pygame.image.load('./src/assets/player.png')
        self.image = pygame.transform.scale(
            self.image, (player_size_x, player_size_y))
        self.rect = self.image.get_rect(topleft=position)

        self.direction = pygame.math.Vector2()
        self.speed = 8
        self.gravity = 0.7
        self.jump_speed = 17
        self.player_on_ground = False

        # These are the sprites player can collide with
        self.collision_sprites = collision_sprites
        self.coin_sprites = coin_sprites

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
