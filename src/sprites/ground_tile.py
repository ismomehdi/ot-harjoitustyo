import pygame
from config.general import TILE_SIZE
from config.paths import GROUND_TILE_IMAGE_PATH


class GroundTile(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        """The GroundTile class is used to create the ground tile sprite.

        Args:
            position: Tuple containing the x and y position of the ground tile.
            groups: List containing the sprite groups the ground tile belongs to.
        """
        super().__init__(groups)
        self.image = pygame.image.load(GROUND_TILE_IMAGE_PATH)
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=position)
