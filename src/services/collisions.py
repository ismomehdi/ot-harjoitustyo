from config.general import COIN_POINTS, ENEMY_POINTS, PLAYER_HEALTH, PLAYER_COLLISION_JUMP_SPEED


class Collisions:
    def __init__(self, collision_sprites, direction, rect, gravity):
        """The Collisions class is used to handle the collisions of the sprites.

        Args:
            collision_sprites: The collision sprite group.
            direction: A direction vector.
            rect: The rect of the sprite.
            gravity: An integer representing the gravity.
        """
        self.collision_sprites = collision_sprites
        self.direction = direction
        self.rect = rect
        self.on_ground = False
        self.gravity = gravity
        self.player_health = PLAYER_HEALTH
        self.player_score = 0

    def apply_horizontal_collisions(self):
        """Applies horizontal collisions."""
        for sprite in self.collision_sprites:

            if sprite.rect.colliderect(self.rect):
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right

                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left

    def apply_vertical_collisions(self):
        """Applies vertical collisions."""
        for sprite in self.collision_sprites:

            if sprite.rect.colliderect(self.rect):
                if self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0

                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.on_ground = True

        if self.on_ground and self.direction.y != 0:
            self.on_ground = False

    def apply_gravity(self):
        """Applies gravity by increasing the y direction
        by the gravity value."""
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def apply_coin_collisions(self, coin_sprites):
        """Applies player's collisions with coins.

        Args:
            coin_sprites: The coin sprite group.
        """
        for coin in coin_sprites:
            if coin.rect.colliderect(self.rect):
                self.player_score += COIN_POINTS
                coin.kill()

    def apply_enemy_collisions(self, enemy_sprites, direction, decrease_health):
        """Applies player's collisions with enemies.

        Args:
            enemy_sprites: The enemy sprite group.
            direction: A direction vector. 
            decrease_health: A function that decreases the player's health. 
        """

        for enemy in enemy_sprites:
            if enemy.rect.colliderect(self.rect):

                # The enemy is destroyed if the player jumps on it
                if enemy.rect.top < self.rect.bottom < enemy.rect.centery \
                        and self.direction.y >= 0:
                    enemy.kill()
                    direction.y = -PLAYER_COLLISION_JUMP_SPEED
                    self.player_score += ENEMY_POINTS

                else:
                    decrease_health()
