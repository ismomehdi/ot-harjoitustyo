import pygame
from sprites.ground_tile import GroundTile
from sprites.sky_tile import SkyTile
from sprites.player import Player
from sprites.coin import Coin
from sprites.enemy import Enemy
from services.camera import Camera
from services.draw_text import draw_text
from config.general import TILE_SIZE, ENEMY_SIZE_OFFSET


class BuildWorld:
    def __init__(self, level_map, display_surface):
        """The World class is used to set up the level and the sprites.

        Attributes:
            level_map: The level map contains the layout of the level.
            display_surface: The display surface is used to render the sprites.
        """

        self.active_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.coin_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.player_sprite = pygame.sprite.GroupSingle()

        self.visible_sprites = Camera(display_surface)

        self.level_map = level_map
        self.setup_world()

    def setup_world(self):
        """Sets up the tiles, player, coins and enemies in the level.
        """
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
                                             self.active_sprites,
                                          self.player_sprite],
                                         self.collision_sprites,
                                         self.coin_sprites,
                                         self.enemy_sprites)
                if column == 'o':
                    Coin((x_position, y_position),
                         [self.visible_sprites, self.active_sprites, self.coin_sprites])
                if column == 'e':
                    Enemy((x_position, y_position - ENEMY_SIZE_OFFSET),
                          [self.visible_sprites, self.active_sprites,
                              self.enemy_sprites],
                          self.collision_sprites, self.player_sprite)

    def draw_points(self):
        """Draws the points on the screen.
        """

        points = self.player.points
        
        text = f'POINTS: {points:04}'
        font = 'src/assets/fonts/Broken Console Bold.ttf'
        size = 30
        color = '#495F63'
        position = (1150, 30)

        draw_text(text, font, size, color, position)
        

    def run_world(self):
        """Runs the world by updating the sprites and drawing the visible sprites.
        """
        self.active_sprites.update()
        self.visible_sprites.camera_draw(self.player)
        self.draw_points()
