import pygame, sys
from assets.colors import bg_color
from world import World
from maps import *
from display import display, display_surface

# Pygame configuration
pygame.init()

clock = pygame.time.Clock()
world = World(level_1, display_surface)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    display.fill(bg_color)
    world.run_world()
    pygame.display.update()
    clock.tick(60)