import pygame
from assets.colors import tile_color

tile_size = 64

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.Surface((tile_size, tile_size))
        self.image.fill(tile_color)
        self.rect = self.image.get_rect(topleft = pos)