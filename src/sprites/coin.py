import pygame
from config.general import TILE_SIZE
from config.paths import COIN_IMAGES_PATH
from services.animate_object import AnimateObject


class Coin(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        """The Coin class is used to create the coin sprite.

        Args:
            position: Tuple containing the x and y position of the coin.
            groups: List containing the sprite groups the coin belongs to.
        """
        super().__init__(groups)
        self.coin = AnimateObject(COIN_IMAGES_PATH)
        self.image = self.coin.image
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=position)

    def update(self):
        """Updates the coin animation."""
        self.image = self.coin.animate()
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
