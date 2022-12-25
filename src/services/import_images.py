from os import walk
from fnmatch import fnmatch
import pygame


def import_folder(path):
    """Imports all images from a folder.

    Args:
        path: A string containing the path to the folder.

    Returns:
        list: A list containing all images from the folder.
    """
    image_list = []

    for _, __, filenames in walk(path):
        for filename in sorted(filenames):
            full_path = path + '/' + filename

            # This ensures only .png files are imported
            if fnmatch(filename, '*.png'):
                image = pygame.image.load(full_path).convert_alpha()
                image_list.append(image)

    return image_list
