import sys
import pygame
from assets.colors import BG_COLOR
from world import World
from display import display, display_surface
from level import level

# Pygame configuration
pygame.init()
clock = pygame.time.Clock()
world = World(level, display_surface)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    display.fill(BG_COLOR)
    world.run_world()
    pygame.display.update()
    clock.tick(60)
