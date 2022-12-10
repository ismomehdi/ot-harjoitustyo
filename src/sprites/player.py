import pygame
from services.player_input import player_input
from services.move_character import move_player
from services.animate_character import AnimateCharacter
from services.collisions import Collisions


class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups, collision_sprites, coin_sprites, enemy_sprites):
        """Player class is used to create the player sprite.

        Attributes:
            position: The position of the player.
            groups: The groups the player sprite belongs to.
            collision_sprites: The collision sprites are used to check for collisions.
            coin_sprites: The coin sprites are used to check for collisions.
            enemy_sprites: The enemy sprites are used to check for collisions.
        """

        super().__init__(groups)

        self.player = AnimateCharacter('./src/assets/player_frames/')
        self.image = self.player.image
        self.rect = self.image.get_rect(topleft=position)

        self.direction = pygame.math.Vector2()
        self.speed = 8
        self.gravity = 0.7
        self.jump_speed = 17

        self.collisions = Collisions(
            collision_sprites, self.direction, self.rect, self.gravity)
        self.coin_sprites = coin_sprites
        self.enemy_sprites = enemy_sprites

        self.player_health = 5
        self.invincible = False
        self.hurt_time = 0
        self.grace_period = 500

    def decrease_health(self):
        """Decreases the player health by 1.

        The self.invincible attribute is set to True for a short period of time 
        (self.grace_period) to prevent the player from losing all health too quickly.

        If the player health is 1 and this method is called, the game is over
        (unless the player is 'invincible').
        """
        if self.player_health == 1 and not self.invincible:
            print("Game Over")

        elif not self.invincible:
            self.player_health -= 1
            self.invincible = True
            self.hurt_time = pygame.time.get_ticks()

    def hurt_timer(self):
        """Sets the self.invincible attribute to False after the grace period.
        """
        if self.invincible:
            if pygame.time.get_ticks() - self.hurt_time >= self.grace_period:
                self.invincible = False

    def update(self):
        """Updates the player sprite.
        """
        player_input(
            self.direction,
            self.jump_speed,
            self.collisions.ground())

        move_player(self.rect, self.direction, self.speed)
        self.collisions.apply_horizontal_collisions()
        self.collisions.apply_gravity()
        self.collisions.apply_vertical_collisions()
        self.collisions.apply_coin_collisions(self.coin_sprites)

        self.collisions.apply_enemy_collisions(
            self.enemy_sprites, self.direction, self.decrease_health)
        self.hurt_timer()

        self.image = self.player.animate(
            self.direction, self.collisions, self.invincible)
