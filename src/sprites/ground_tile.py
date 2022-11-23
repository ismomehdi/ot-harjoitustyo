import pygame
ground_tile_size = 48

class GroundTile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('./src/assets/ground_tile.png')
        self.image = pygame.transform.scale(self.image, (ground_tile_size, ground_tile_size))
        self.rect = self.image.get_rect(topleft = pos)