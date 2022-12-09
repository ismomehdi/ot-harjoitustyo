import pygame
from services.player_input import player_input
from services.move_character import move_player
from services.animate_character import AnimateCharacter
from collisions.main_collisions import MainCollisions
from collisions.coin_collisions import apply_coin_collisions


class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups, collision_sprites, coin_sprites):
        super().__init__(groups)

        # The AnimatedCharacter class is used to animate the player
        self.player = AnimateCharacter('./src/assets/player_frames/')
        self.image = self.player.image
        self.rect = self.image.get_rect(topleft=position)

        # Player movement
        self.direction = pygame.math.Vector2()
        self.speed = 8
        self.gravity = 0.7
        self.jump_speed = 17

        # For collisions
        self.collisions = MainCollisions(collision_sprites, self.direction, self.rect, self.gravity)
        self.coin_sprites = coin_sprites

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
        
        self.image = self.player.animate(self.direction, self.collisions)
