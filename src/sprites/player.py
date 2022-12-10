import pygame
from services.player_input import player_input
from services.move_character import move_player
from services.animate_character import AnimateCharacter
from services.collisions import Collisions


class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups, collision_sprites, coin_sprites, enemy_sprites):
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
        self.collisions = Collisions(collision_sprites, self.direction, self.rect, self.gravity)
        self.coin_sprites = coin_sprites
        self.enemy_sprites = enemy_sprites

        # Player health
        self.player_health = 5
        self.hurt = False
        self.hurt_time = 0
        self.hurt_delay = 500

    def decrease_health(self):
        if self.player_health == 1 and not self.hurt:
            print("Game Over")

        elif not self.hurt:
            self.player_health -= 1
            self.hurt = True
            self.hurt_time = pygame.time.get_ticks()
    
    def hurt_timer(self):
        if self.hurt:
            if pygame.time.get_ticks() - self.hurt_time >= self.hurt_delay:
                self.hurt = False

    def update(self):
        player_input(
            self.direction,
            self.jump_speed,
            self.collisions.ground())

        move_player(self.rect, self.direction, self.speed)
        self.collisions.apply_horizontal_collisions()
        self.collisions.apply_gravity()
        self.collisions.apply_vertical_collisions()
        self.collisions.apply_coin_collisions(self.coin_sprites)

        self.collisions.apply_enemy_collisions(self.enemy_sprites, self.direction, self.decrease_health)
        self.hurt_timer()

        self.image = self.player.animate(self.direction, self.collisions, self.hurt)