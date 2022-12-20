from services.import_images import import_folder

class AnimateObject:
    def __init__(self, path):
        self.frame_index = 0
        self.animation_speed = 0.15
        self.animation_frames = import_folder(path)
        self.image = self.animation_frames[self.frame_index]

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index > len(self.animation_frames):
            self.frame_index = 0

        image = self.animation_frames[int(self.frame_index)]
        return image
