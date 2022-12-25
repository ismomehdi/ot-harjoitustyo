import pygame
from services.import_maps import import_maps
from config.general import TILE_SIZE

# In further development, a level selector could be added
# and this module would be done differently.

maps = import_maps()

LEVEL = 1
level_map = maps[str(LEVEL)]

LEVEL_X = len(level_map[0]) * TILE_SIZE
LEVEL_Y = len(level_map) * TILE_SIZE

level_rect = pygame.Rect(0, 0, LEVEL_X, LEVEL_Y)
