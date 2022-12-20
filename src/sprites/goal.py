import pygame
from config.paths import GOAL_IMAGES_PATH
from services.animate_object import AnimateObject

class Goal(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.goal = AnimateObject(GOAL_IMAGES_PATH)
        self.image = self.goal.image
        self.rect = self.image.get_rect(center=position)

    def update(self):
        self.image = self.goal.animate()

