import pygame
from sprites.ground_tile import GroundTile
from sprites.sky_tile import SkyTile
from sprites.player import Player
from sprites.coin import Coin
from camera import Camera
from maps import TILE_SIZE


class World:
    def __init__(self, level_map, display_surface):
        # Sprite configuration. Camera() is a custom sprite group
        # for controlling what's visible on the screen
        self.visible_sprites = Camera(display_surface)
        self.active_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.coin_sprites = pygame.sprite.Group()
        self.level_map = level_map

        self.setup_world()

    # Sets up the tiles and the initial position of the player
    def setup_world(self):
        for row_index, row in enumerate(self.level_map):
            for column_index, column in enumerate(row):
                x_position = column_index * TILE_SIZE
                y_position = row_index * TILE_SIZE

                if column == 'X':
                    GroundTile(
                        (x_position, y_position), [self.visible_sprites, self.collision_sprites])
                if column == 'x':
                    SkyTile((x_position, y_position), [self.visible_sprites,
                            self.collision_sprites])
                if column == 'P':
                    self.player = Player((x_position, y_position),
                                         [self.visible_sprites,
                                             self.active_sprites],
                                         self.collision_sprites,
                                         self.coin_sprites)
                if column == 'o':
                    Coin((x_position, y_position),
                         [self.visible_sprites, self.active_sprites, self.coin_sprites])

    # Draws the world
    def run_world(self):
        self.active_sprites.update()
        self.visible_sprites.camera_draw(self.player)
