import pygame
from sprites.ground_tile import ground_tile_size

sky_tile_size = ground_tile_size

class SkyTile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('./src/assets/sky_tile.png')
        self.image = pygame.transform.scale(self.image, (sky_tile_size, sky_tile_size))
        self.rect = self.image.get_rect(topleft = pos)