import pygame
from config.general import TILE_SIZE
from config.paths import COIN_IMAGES_PATH
from services.import_images import import_folder


class Coin(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.animation_frames = import_folder(COIN_IMAGES_PATH)
        self.image = self.animation_frames[self.frame_index]
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=position)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index > len(self.animation_frames):
            self.frame_index = 0

        self.image = self.animation_frames[int(self.frame_index)]
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))

    def update(self):
        self.animate()
