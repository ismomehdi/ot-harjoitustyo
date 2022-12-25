import pygame
from config.general import TILE_SIZE


class Camera(pygame.sprite.Group):
    def __init__(self, display_surface):
        """The Camera class is used to render the visible sprites on the display surface.

        The camera moves when the player gets close to the camera 'borders'. The camera
        borders are defined in the self.camera dictionary. For example, if the player's
        position is equal to self.camera[left], the camera moves left. If the player's
        position is equal to self.camera[right], the camera moves right. The same goes
        for the top and bottom borders.

        Attributes:
            display_surface: The display surface is used to render the sprites.
        """

        super().__init__()
        self.display_surface = display_surface
        self.offset = []

        self.camera = {
            'left': 150,
            'right': display_surface.get_size()[0] / 2,
            'top': 100,
            'bottom': TILE_SIZE
        }

        camera_width = display_surface.get_size()[0] - (
            self.camera['left'] + self.camera['right'])

        camera_height = display_surface.get_size()[1] - (
            self.camera['top'] + self.camera['bottom'])

        self.camera_rect = pygame.Rect(
            self.camera['left'], self.camera['top'], camera_width, camera_height)

    def camera_draw(self, player):
        """Draws the visible sprites on the display surface so that their position is
        manipulated by the offset value.

        1. Changes the camera rectangle coordinates if the player gets close to the 
        camera 'borders'. So in other words, moves the camera.

        2. Ensures the camera moves left only if the player is not in the starting 
        position (edge of the world).

        3. The offset vector calculates the distance from the camera borders to the 
        surface borders.

        4. The visible sprites are drawn on the surface so that their position is 
        manipulated by the offset value.

        Args:
            player: The player sprite.
        """

        # 1.
        if player.rect.right > self.camera_rect.right:
            self.camera_rect.right = player.rect.right
        if player.rect.top < self.camera_rect.top:
            self.camera_rect.top = player.rect.top
        if player.rect.bottom > self.camera_rect.bottom:
            self.camera_rect.bottom = player.rect.bottom

        # 2.
        if self.camera_rect.left > self.camera['left']:
            if player.rect.left < self.camera_rect.left:
                self.camera_rect.left = player.rect.left

        # 3.
        self.offset = pygame.math.Vector2(
            self.camera_rect.left - self.camera['left'],
            self.camera_rect.top - self.camera['top'])

        # 4.
        for sprite in self.sprites():
            offset_position = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_position)
