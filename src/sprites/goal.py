import pygame
from config.paths import GOAL_IMAGES_PATH
from services.animate_object import AnimateObject


class Goal(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        """The Goal class is used to create the goal sprite.

        Args:
            position: Tuple containing the x and y position of the goal.
            groups: List containing the sprite groups the goal belongs to.
        """
        super().__init__(groups)
        self.goal = AnimateObject(GOAL_IMAGES_PATH)
        self.image = self.goal.image
        self.rect = self.image.get_rect(center=position)

    def update(self):
        """Updates the goal animation."""
        self.image = self.goal.animate()
