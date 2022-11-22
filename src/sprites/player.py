import pygame
from assets.colors import player_color
from sprites.tile import tile_size

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)

        # Player configuration
        player_size_x = tile_size / 2
        player_size_y = tile_size

        self.image = pygame.Surface((player_size_x, player_size_y))
        self.image.fill(player_color)
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2()
        self.speed = 10
        self.gravity = 1.1
        self.jump_speed = 20
        self.player_on_ground = False

        # These are the sprites player can collide with
        self.collision_sprites = collision_sprites

    def input(self):
        self.keys = pygame.key.get_pressed()

        # This controls the player left and right movement
        if self.keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif self.keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        # This controls the player jump
        if self.keys[pygame.K_UP] and self.player_on_ground:
            self.direction.y = -self.jump_speed
    
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

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    
    def update(self):
        self.input()
        self.rect.x += self.direction.x * self.speed
        self.horizontal_collisions()
        self.apply_gravity()
        self.vertical_collisions()
        
        

        