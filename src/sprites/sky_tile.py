import pygame
from config.general import TILE_SIZE
from config.paths import SKY_TILE_IMAGE_PATH


class SkyTile(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        """The SkyTile class is used to create the sky tile sprite.

        Args:
            position: Tuple containing the x and y position of the sky tile.
            groups: List containing the sprite groups the sky tile belongs to.
        """
        super().__init__(groups)
        self.image = pygame.image.load(SKY_TILE_IMAGE_PATH)
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=position)
