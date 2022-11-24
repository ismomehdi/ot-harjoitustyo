import pygame
from os import walk

def import_folder(path):
    image_list = []

    for dirpath, dirname, filenames in walk(path):
        for filename in sorted(filenames):
            full_path = path + '/' + filename
            image = pygame.image.load(full_path).convert_alpha()
            image_list.append(image)
    
    return image_list