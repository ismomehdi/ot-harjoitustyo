from os import walk
from fnmatch import fnmatch
import pygame


def import_folder(path):
    image_list = []

    for _, __, filenames in walk(path):
        for filename in sorted(filenames):
            full_path = path + '/' + filename

            # This ensures only .png files are imported
            if fnmatch(filename, '*.png'):
                image = pygame.image.load(full_path).convert_alpha()
                image_list.append(image)

    return image_list
