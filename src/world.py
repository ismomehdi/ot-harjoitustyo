import pygame
from maps import *
from sprites.tile import Tile, tile_size
from sprites.player import Player
from camera import Camera

class World:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        # Sprite configuration. Camera() is a custom sprite group
        # for controlling what's visible on the screen
        self.visible_sprites = Camera()
        self.active_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.setup_world()

    # Sets up the tiles and the initial position of the player
    def setup_world(self):
        for row_index, row in enumerate(level_1):
            for column_index, column in enumerate(row):
                x = column_index * tile_size
                y = row_index * tile_size

                if column == 'X':
                    Tile((x, y), [self.visible_sprites, self.collision_sprites])
                if column == 'P':
                    self.player = Player((x, y), 
                        [self.visible_sprites, self.active_sprites], 
                            self.collision_sprites)

    # Draws the world
    def run_world(self):
        self.active_sprites.update()
        self.visible_sprites.camera_draw(self.player)
