import pygame, sys
from assets.colors import bg_color
from world import World

# Pygame configuration
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("The Adventures of Yakuzi")

clock = pygame.time.Clock()
world = World()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(bg_color)
    world.run_world()

    pygame.display.update()
    clock.tick(60)