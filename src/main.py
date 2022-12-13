import sys
import pygame
from config.general import BG_COLOR
from build_world import BuildWorld
from config.display import display, display_surface
from level import level_map
from menus.main_menu import MainMenu
from menus.pause_menu import PauseMenu

pygame.init()
clock = pygame.time.Clock()
world = BuildWorld(level_map, display_surface)
menu =  MainMenu()
pause = PauseMenu()
restart = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and not menu.game_menu:
                pause.on = True
    
    if pause.on:
        pause.run_menu()
        restart = pause.restart
        pygame.display.update()
        clock.tick(60)

    elif restart:
        world = BuildWorld(level_map, display_surface)
        menu =  MainMenu()
        pause = PauseMenu()
        restart = False

    elif menu.game_menu:
        menu.run_menu()
        game_menu = menu.game_menu
        pygame.display.update()
        clock.tick(60)

    else:
        display.fill(BG_COLOR)
        world.run_world()
        pygame.display.update()
        clock.tick(60)
