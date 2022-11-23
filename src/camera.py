import pygame

class Camera(pygame.sprite.Group):
    def __init__(self, display_surface):
        super().__init__()
        self.display_surface = display_surface

        # This controls when the camera moves. For example
        # if the player's position is 150px from left, the
        # camera moves. You can think of these as the camera
        # 'borders'
        self.camera = {
            'left': 150,
            'right': display_surface.get_size()[0] / 2,
            'top': 100,
            'bottom': 50
        }

        # This calculates the width and height of the camera area by
        # substracting the camera border values from the display size
        camera_width = display_surface.get_size()[0] - (
            self.camera['left'] + self.camera['right'])

        camera_height = display_surface.get_size()[1] - (
            self.camera['top'] + self.camera['bottom'])

        # These are the camera rectangle coordinates and size 
        self.camera_rect = pygame.Rect(
            self.camera['left'], self.camera['top'], camera_width, camera_height)

    def camera_draw(self, player):
        # This changes the camera rectangle coordinates if the player gets
        # close to the camera 'borders'. In other words, this moves the camera.
        if player.rect.left < self.camera_rect.left:
            self.camera_rect.left = player.rect.left
        if player.rect.right > self.camera_rect.right:
            self.camera_rect.right = player.rect.right
        if player.rect.top < self.camera_rect.top:
            self.camera_rect.top = player.rect.top
        if player.rect.bottom > self.camera_rect.bottom:
            self.camera_rect.bottom = player.rect.bottom

        # This vector calculates the distance from the camera
        # borders to the surface borders
        self.offset = pygame.math.Vector2(
            self.camera_rect.left - self.camera['left'], 
            self.camera_rect.top - self.camera['top'])

        # This draws the visible sprites on the surface so that their
        # position is manipulated by the offset value
        for sprite in self.sprites():
            offset_position = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_position)

