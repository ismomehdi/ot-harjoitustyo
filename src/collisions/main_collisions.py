class MainCollisions:
    def __init__(self, collision_sprites, direction, rect, gravity):
        self.collision_sprites = collision_sprites
        self.direction = direction
        self.rect = rect
        self.on_ground = False
        self.gravity = gravity

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

    def ground(self):
        return self.on_ground

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
