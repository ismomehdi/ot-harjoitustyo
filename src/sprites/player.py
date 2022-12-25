import pygame
from services.player_input import player_input
from services.move_character import move_player
from services.animate_character import AnimateCharacter
from services.collisions import Collisions
from config.paths import PLAYER_IMAGES_PATH
from config.general import PLAYER_SPEED, PLAYER_GRAVITY, \
    PLAYER_JUMP_SPEED, PLAYER_HEALTH, PLAYER_GRACE_PERIOD


class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups, collision_sprites, coin_sprites, enemy_sprites):
        """Player class is used to create the player sprite.

        Attributes:
            position: Tuple containing the x and y position of the player.
            groups: List containing the sprite groups the player belongs to.
            collision_sprites: The collision sprites are used to check for collisions.
            coin_sprites: The coin sprites are used to check for collisions.
            enemy_sprites: The enemy sprites are used to check for collisions.
        """

        super().__init__(groups)

        self.player = AnimateCharacter(PLAYER_IMAGES_PATH)
        self.image = self.player.image
        self.rect = self.image.get_rect(topleft=position)

        self.direction = pygame.math.Vector2()

        self.get_player_constants()

        self.collisions = Collisions(
            collision_sprites, self.direction, self.rect, self._gravity)
        self.coin_sprites = coin_sprites
        self.enemy_sprites = enemy_sprites

        self.score = 0
        self.invincible = False
        self.dead = False
        self.hurt_time = 0
        self.reached_goal = False

    def get_player_constants(self):
        """Sets the player constants."""
        self._speed = PLAYER_SPEED
        self._gravity = PLAYER_GRAVITY
        self._jump_speed = PLAYER_JUMP_SPEED
        self._player_health = PLAYER_HEALTH
        self._grace_period = PLAYER_GRACE_PERIOD

    def decrease_health(self):
        """Decreases the player health by 1.

        The self.invincible attribute is set to True for a short period of time
        (self.grace_period) to prevent the player from losing all health too quickly.

        If the player health is 1 and this method is called, the game is over
        (unless the player is 'invincible').
        """
        if self._player_health == 1 and not self.invincible:
            self.dead = True
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)
        elif not self.invincible:
            self._player_health -= 1
            self.invincible = True
            self.hurt_time = pygame.time.get_ticks()

    def hurt_timer(self):
        """Sets the self.invincible attribute to False after the grace period.
        """
        if self.invincible:
            if pygame.time.get_ticks() - self.hurt_time >= self._grace_period:
                self.invincible = False

    def get_score(self):
        """Gets the player score from the collisions class.

        Returns:
            integer: The player score.
        """
        self.score = self.collisions.player_score
        return self.score

    def update(self):
        """Updates the player sprite and the player score.
        """
        if self.reached_goal:
            self.direction.x = 0

        elif not self.dead and not self.reached_goal:
            player_input(
                self.direction,
                self._jump_speed,
                self.collisions.on_ground,
                pygame.key.get_pressed())

            move_player(self.rect, self.direction, self._speed)

        self.collisions.apply_horizontal_collisions()
        self.collisions.apply_gravity()
        self.collisions.apply_vertical_collisions()
        self.collisions.apply_coin_collisions(self.coin_sprites)

        self.collisions.apply_enemy_collisions(
            self.enemy_sprites, self.direction, self.decrease_health)
        self.hurt_timer()

        self.image = self.player.animate(
            self.direction, self.collisions, self.invincible, self.dead)

        self.score = self.get_score()
