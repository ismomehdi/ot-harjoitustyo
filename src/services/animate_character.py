import pygame
from services.import_images import import_folder


class AnimateCharacter:
    def __init__(self, path):
        self.import_assets(path)

        self.moving_forward = True
        self.status = 'idle'

        self.frame_index = 0
        self.animation_speed = 0.19

        self.image = self.animations['idle'][self.frame_index]

    def import_assets(self, path):
        self.animations = {'idle': [], 'run': [],
                           'jump': [], 'fall': [], 'hurt': [], 'death': []}

        for animation in self.animations:
            full_path = path + animation
            self.animations[animation] = import_folder(full_path)

    def get_status(self, direction, collisions, invincible, dead):

        # Check which way the player is moving
        if direction.x == 1:
            self.moving_forward = True
        elif direction.x == -1:
            self.moving_forward = False

        # Determine the player's status
        if invincible:
            self.status = 'hurt'
        elif dead:
            self.status = 'death'
            self.animation_speed = 0.1
        elif direction.y < 0:
            self.status = 'jump'
        elif direction.x != 0 and collisions.ground():
            self.status = 'run'
        elif collisions.ground():
            self.status = 'idle'

    def animate(self, direction, collisions, invincible=False, dead=False):
        self.get_status(direction, collisions, invincible, dead)
        animation_frames = self.animations[self.status]

        self.frame_index += self.animation_speed
        if dead and self.frame_index > len(animation_frames):
            return self.image
        elif self.frame_index > len(animation_frames):
            self.frame_index = 0

        image = animation_frames[int(self.frame_index)]
        if self.moving_forward:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image

        return self.image
