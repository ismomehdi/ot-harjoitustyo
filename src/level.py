# This can be used in future development for choosing the level

import pygame
from maps import maps, TILE_SIZE

level_map = maps['level_1']
LEVEL_X = len(level_map[0]) * TILE_SIZE
LEVEL_Y = len(level_map) * TILE_SIZE

level_rect = pygame.Rect(0, 0, LEVEL_X, LEVEL_Y)
