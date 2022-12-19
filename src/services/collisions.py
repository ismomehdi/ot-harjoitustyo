class Collisions:
    def __init__(self, collision_sprites, direction, rect, gravity):
        self.collision_sprites = collision_sprites
        self.direction = direction
        self.rect = rect
        self.on_ground = False
        self.gravity = gravity
        self.player_health = 3
        self.player_points = 0

    def apply_horizontal_collisions(self):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                # The character is moving left
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right
                # The character is moving right
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left

    def apply_vertical_collisions(self):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                # The character is moving up
                if self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0
                # The character is moving down
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.on_ground = True

        # The character is not on ground
        if self.on_ground and self.direction.y != 0:
            self.on_ground = False

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    # This method is used for player's collisions with coins
    def apply_coin_collisions(self, coin_sprites):
        for sprite in coin_sprites:
            if sprite.rect.colliderect(self.rect):
                self.player_points += 1
                sprite.kill()

    # This method is used for player's collisions with enemies
    def apply_enemy_collisions(self, enemy_sprites, direction, decrease_health):
        for enemy in enemy_sprites:
            if enemy.rect.colliderect(self.rect):

                # The enemy is destroyed if the player jumps on it
                if enemy.rect.top < self.rect.bottom < enemy.rect.centery \
                        and self.direction.y >= 0:
                    enemy.kill()
                    direction.y = -14
                    self.player_points += 10

                else:
                    decrease_health()
