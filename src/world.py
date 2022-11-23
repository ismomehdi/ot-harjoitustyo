import pygame
from sprites.ground_tile import GroundTile, ground_tile_size
from sprites.sky_tile import SkyTile
from sprites.player import Player
from camera import Camera

class World:
    def __init__(self, level_map, display_surface):
        # Sprite configuration. Camera() is a custom sprite group
        # for controlling what's visible on the screen
        self.visible_sprites = Camera(display_surface)
        self.active_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.setup_world(level_map)

    # Sets up the tiles and the initial position of the player
    def setup_world(self, level_map):
        for row_index, row in enumerate(level_map):
            for column_index, column in enumerate(row):
                x = column_index * ground_tile_size
                y = row_index * ground_tile_size

                if column == 'X':
                    GroundTile((x, y), [self.visible_sprites, self.collision_sprites])
                if column == 'x':
                    SkyTile((x, y), [self.visible_sprites, self.collision_sprites])
                if column == 'P':
                    self.player = Player((x, y), 
                        [self.visible_sprites, self.active_sprites], 
                            self.collision_sprites)

    # Draws the world
    def run_world(self):
        self.active_sprites.update()
        self.visible_sprites.camera_draw(self.player)

