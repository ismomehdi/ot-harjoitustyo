import pygame
from maps import TILE_SIZE
from level import level_rect
from collisions.main_collisions import MainCollisions


class Enemy(pygame.sprite.Sprite):
    def __init__(self, position, groups, collision_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('./src/assets/sky_tile.png')
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=position)
        self.original_position = position

        # Enemy movement
        self.direction = pygame.math.Vector2()
        self.speed = 2

        self.collisions = MainCollisions(
            collision_sprites, self.direction, self.rect)

    def move_enemy(self):
        # self.rect.x += self.direction.x * self.speed
        self.rect.x += self.speed
        self.rect.clamp_ip(level_rect)

    def update(self):
        self.collisions.apply_horizontal_collisions()
        self.collisions.apply_vertical_collisions()
        self.move_enemy()
