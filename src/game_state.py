import sys
import pygame
from build_world import BuildWorld
from menus.main_menu import MainMenu
from menus.pause_menu import PauseMenu
from services.finish_screen import FinishScreen
from level import level_map, LEVEL
from config.display import display, display_surface
from config.general import BG_COLOR


class GameState:
    def __init__(self):
        """The GameState class is used to control different game states."""
        self._clock = pygame.time.Clock()
        self._world = BuildWorld(level_map, display_surface)
        self._menu = MainMenu()
        self._pause = PauseMenu()
        self._finish = FinishScreen()

    def handle_user_input(self):
        """Handles the user keyboard input."""
        _score = self._world.player.score

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                _main_menu = self._menu.state['main_menu']
                if event.key == pygame.K_ESCAPE and not _main_menu:
                    self._pause.state['on_pause'] = True

                if self._finish.high_score:
                    self.handle_high_score_input(event, _score)

    def handle_high_score_input(self, event, score):
        """Handles the user keyboard input when the high score screen is active.

        Args:
            event: The pygame.event is used to determine the active keys.
            score: The score integer determines the score of the player.
        """
        if event.key == pygame.K_BACKSPACE:
            self._finish.user_input = self._finish.user_input[:-1]

        elif len(self._finish.user_input) < 10:
            self._finish.user_input += event.unicode

        if event.key == pygame.K_RETURN:
            if self._finish.user_input == '':
                self._finish.user_input = 'Player'

            self._finish.add_name_to_database(score)
            self._finish.high_score = False
            self._finish.high_scores_screen = True

    def restart(self):
        """Restarts the game."""
        self._world = BuildWorld(level_map, display_surface)
        self._menu = MainMenu()
        self._pause = PauseMenu()
        self._finish = FinishScreen()

    def goal(self):
        """Organizes the finish screen."""
        display.fill(BG_COLOR)
        _score = self._world.player.score

        if self._finish.win_screen:
            self._finish.draw_win_screen(_score)
        elif self._finish.high_score:
            self._finish.draw_enter_name_screen()
        elif self._finish.high_scores_screen:
            self._finish.draw_high_score_screen(LEVEL)
        else:
            self._pause.state['restart'] = True
            return

        self._world.run_world()
        pygame.display.update()

    def game_over(self):
        """Organizes the game over screen."""
        display.fill(BG_COLOR)

        if self._finish.game_over_screen:
            self._finish.draw_game_over_screen()
        else:
            self._pause.state['restart'] = True
            return

        self._world.run_world()
        pygame.display.update()

    def pause(self):
        """Organizes the pause menu."""
        self._pause.run_menu()
        pygame.display.update()

    def main_menu(self):
        """Organizes the main menu."""
        self._menu.run_menu()
        pygame.display.update()

    def play(self):
        """Starts the game."""
        display.fill(BG_COLOR)
        self._world.run_world()
        pygame.display.update()

    def run(self):
        """Runs the game based on the current game state."""
        _restart = self._pause.state['restart']
        _pause = self._pause.state['on_pause']
        _main_menu = self._menu.state['main_menu']
        _reached_goal = self._world.reached_goal
        _player = self._world.player

        if _restart:
            self.restart()

        elif _pause:
            self.pause()

        elif _main_menu:
            self.main_menu()

        elif _reached_goal:
            self.goal()

        elif _player.dead:
            self.game_over()

        else:
            self.play()

        self._clock.tick(60)
