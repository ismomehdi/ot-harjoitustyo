import sys
import pygame
from config.colors import BG_COLOR, MENU_COLOR
from world import World
from config.display import display, display_surface
from level import level_map
from menu import Menu

pygame.init()
clock = pygame.time.Clock()
world = World(level_map, display_surface)
menu = Menu()
game_menu = False

bg_image = pygame.image.load('./src/assets/images/menu/1.png')
bg_image = pygame.transform.scale(bg_image, (display.get_width(), display.get_height()))
bg_image_2 = pygame.image.load('./src/assets/images/menu/3.png')
bg_image_2 = pygame.transform.scale(bg_image_2, (display.get_width(), display.get_height()))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if game_menu:
        display.blit(bg_image, (0,0))
        menu.run_menu()
        display.blit(bg_image_2, (0,0))
        pygame.display.update()
        clock.tick(60)

    else:
        display.fill(BG_COLOR)
        world.run_world()
        pygame.display.update()
        clock.tick(60)
