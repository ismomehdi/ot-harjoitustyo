import sys
import pygame
from build_world import BuildWorld
from menus.main_menu import MainMenu
from menus.pause_menu import PauseMenu
from level import level_map
from config.display import display, display_surface
from config.general import BG_COLOR


class GameState:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.world = BuildWorld(level_map, display_surface)
        self.menu = MainMenu()
        self.pause = PauseMenu()

    def handle_quit_and_pause_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                main_menu = self.menu.state['main_menu']
                if event.key == pygame.K_ESCAPE and not main_menu:
                    self.pause.state['on_pause'] = True

    def run(self):
        restart = self.pause.state['restart']
        pause = self.pause.state['on_pause']
        main_menu = self.menu.state['main_menu']

        if restart:
            self.world = BuildWorld(level_map, display_surface)
            self.menu = MainMenu()
            self.pause = PauseMenu()

        elif pause:
            self.pause.run_menu()
            pygame.display.update()

        elif main_menu:
            self.menu.run_menu()
            pygame.display.update()

        else:
            display.fill(BG_COLOR)
            self.world.run_world()
            pygame.display.update()

        self.clock.tick(60)
