import pygame
from db.high_score_repository import HighScoreRepository
from services.text import Text
from level import LEVEL


class FinishScreen:
    def __init__(self):
        """Handles the win and game over states."""
        self.win_screen = True
        self.game_over_screen = True
        self.ready_to_exit = False
        self.high_score = False
        self.high_scores_screen = False
        self.user_input = ''
        self.database = HighScoreRepository()

    def keys_released(self):
        """Checks if any keys are pressed. This is used
            to determine if the user has released all keys.

        Returns:
            boolean: True if NO keys are pressed,
                False otherwise.
        """
        keys = pygame.key.get_pressed()
        return not any(keys)

    def key_pressed(self):
        """Checks if any keys are pressed.

        Returns:
            boolean: True if any keys are pressed,
                False otherwise.
        """
        keys = pygame.key.get_pressed()
        return any(keys)

    def draw_game_over_screen(self):
        """Uses the Text class to draw the game over screen and
            handles the user input.
        """
        Text.game_over()

        if self.keys_released():
            self.ready_to_exit = True

        if self.ready_to_exit and self.key_pressed():
            self.ready_to_exit = False
            self.game_over_screen = False

    def draw_win_screen(self, score):
        """Uses the Text class to draw the win screen and
            handles the user input. Also checks if the score
            is a high score.

        Args:
            score: An integer representing the score.
        """
        Text.win(score)

        if self.keys_released():
            self.ready_to_exit = True

        if self.ready_to_exit and self.key_pressed():
            self.high_score = self.database.check_if_top_ten(score, LEVEL)
            self.win_screen = False

            if not self.high_score:
                self.high_scores_screen = True

            self.ready_to_exit = False

    def add_name_to_database(self, score):
        """Adds the user's name and score to the database.

        Args:
            score: An integer representing the score.
        """
        self.database.add(1, self.user_input, score)

    def draw_enter_name_screen(self):
        """Calls the Text class to draw the enter name screen."""
        Text.enter_name(self.user_input)

    def draw_high_score_screen(self, level):
        """Calls the Text class to draw the high score screen.
            and handles the user input.

        Args:
            level: An integer representing the level.
        """
        high_scores = self.database.get_top_ten(level)

        Text.high_score_titles()
        Text.high_score_stats(high_scores)

        if self.keys_released():
            self.ready_to_exit = True

        if self.ready_to_exit and self.key_pressed():
            self.high_scores_screen = False
