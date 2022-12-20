import pygame
from config.general import TILE_SIZE
from config.paths import COIN_IMAGES_PATH
from services.import_images import import_folder
from services.animate_object import AnimateObject


class Coin(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.coin = AnimateObject(COIN_IMAGES_PATH)
        self.image = self.coin.image
        self.rect = self.image.get_rect(topleft=position)

    def update(self):
        self.image = self.coin.animate()
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
