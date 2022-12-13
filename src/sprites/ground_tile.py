import pygame
from config.general import TILE_SIZE
from config.paths import GROUND_TILE_IMAGE_PATH


class GroundTile(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(GROUND_TILE_IMAGE_PATH)
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=position)
