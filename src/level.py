import pygame
from services.import_maps import import_maps
from config.general import TILE_SIZE

# In the future, the level will be selected by the user
# and this module will be done differently

maps = import_maps()

level_map = maps['level_1']

LEVEL_X = len(level_map[0]) * TILE_SIZE
LEVEL_Y = len(level_map) * TILE_SIZE

level_rect = pygame.Rect(0, 0, LEVEL_X, LEVEL_Y)
