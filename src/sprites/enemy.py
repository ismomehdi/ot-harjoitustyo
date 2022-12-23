import pygame
from config.paths import ENEMY_IMAGES_PATH
from config.general import ENEMY_AREA_SIZE, ENEMY_SPEED, ENEMY_CHASE_SPEED, ENEMY_GRAVITY
from services.collisions import Collisions
from services.animate_character import AnimateCharacter
from services.move_character import move_enemy


class Enemy(pygame.sprite.Sprite):
    def __init__(self, position, groups, collision_sprites, player_sprite):
        super().__init__(groups)

        # The AnimatedCharacter class is used to animate the enemy
        self.enemy = AnimateCharacter(ENEMY_IMAGES_PATH)
        self.image = self.enemy.image
        self.rect = self.image.get_rect(topleft=position)

        # Enemy starting position and area size for movement
        self.starting_pos_x = position[0]
        self.starting_pos_y = position[1]
        self.area_size = ENEMY_AREA_SIZE

        # Enemy movement
        self.direction = pygame.math.Vector2()
        self.direction.x = 1
        self.speed = ENEMY_SPEED
        self.chase_speed = ENEMY_CHASE_SPEED
        self.gravity = ENEMY_GRAVITY

        # For collisions
        self.collisions = Collisions(
            collision_sprites, self.direction, self.rect, self.gravity)

        # Player sprite group for tracking the player
        self.player = player_sprite

    def update(self):
        move_enemy(self.rect, self.direction, self.speed,
                   self.starting_pos_x, self.area_size,
                   self.chase_speed, self.player)

        self.collisions.apply_horizontal_collisions()
        self.collisions.apply_gravity()
        self.collisions.apply_vertical_collisions()
        self.image = self.enemy.animate(self.direction, self.collisions)
