import sys
import pygame
from build_world import BuildWorld
from menus.main_menu import MainMenu
from menus.pause_menu import PauseMenu
from services.finish_screen import FinishScreen
from level import level_map
from config.display import display, display_surface
from config.general import BG_COLOR


class GameState:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.world = BuildWorld(level_map, display_surface)
        self.menu = MainMenu()
        self.pause = PauseMenu()
        self.finish = FinishScreen()

    def handle_user_input(self):
        score = self.world.player.score

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                main_menu = self.menu.state['main_menu']
                if event.key == pygame.K_ESCAPE and not main_menu:
                    self.pause.state['on_pause'] = True
                
                if self.finish.high_score:
                    if event.key == pygame.K_BACKSPACE:
                        self.finish.user_input = self.finish.user_input[:-1]

                    elif len(self.finish.user_input) < 10:
                        self.finish.user_input += event.unicode

                    if event.key == pygame.K_RETURN:
                        if self.finish.user_input == '':
                            self.finish.user_input = 'Player'

                        self.finish.enter_name(score)
                        self.finish.high_score = False
                        self.finish.high_scores_screen = True

    def run(self):
        restart = self.pause.state['restart']
        pause = self.pause.state['on_pause']
        main_menu = self.menu.state['main_menu']
        reached_goal = self.world.reached_goal
        score = self.world.player.score 

        if restart:
            self.world = BuildWorld(level_map, display_surface)
            self.menu = MainMenu()
            self.pause = PauseMenu()
            self.finish = FinishScreen()

        elif pause:
            self.pause.run_menu()
            pygame.display.update()

        elif main_menu:
            self.menu.run_menu()
            pygame.display.update()
        
        elif reached_goal:
            display.fill(BG_COLOR)

            if self.finish.win_screen:
                self.finish.draw_win_screen(score)
            elif self.finish.high_score:
                self.finish.draw_enter_name_screen()
            elif self.finish.high_scores_screen:
                self.finish.draw_high_scores()
            else:
                self.pause.state['restart'] = True
                return

            self.world.run_world()
            pygame.display.update()

        else:
            display.fill(BG_COLOR)
            self.world.run_world()
            pygame.display.update()

        self.clock.tick(60)
