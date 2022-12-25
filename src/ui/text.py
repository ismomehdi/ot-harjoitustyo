import config.text_settings as ts
from services.draw_text import draw_text
from config.paths import BROKEN_CONSOLE_FONT


class Text:
    font = BROKEN_CONSOLE_FONT
    color_1 = ts.PURPLE
    color_2 = ts.PINK

    @classmethod
    def score(cls, score):
        """Draws the score on the screen.
        
        Args:
            score: The score integer determines the score of the player.
        """

        draw_text(f'SCORE: {score:04}', cls.font,
                  ts.SCORE_SIZE, cls.color_1, ts.SCORE_POSITION)

    @classmethod
    def high_score_titles(cls):
        """Draws the titles for the high score screen."""

        draw_text('HIGH SCORES', cls.font, ts.HS_TITLE_SIZE,
                  cls.color_1, ts.HS_TITLE_POS)
        draw_text('#', cls.font, ts.HS_COLUMN_NAME_SIZE,
                  cls.color_1, ts.HS_NUMBER_POS)
        draw_text('name', cls.font, ts.HS_COLUMN_NAME_SIZE,
                  cls.color_1, ts.HS_NAME_POS)
        draw_text('score', cls.font, ts.HS_COLUMN_NAME_SIZE,
                  cls.color_1, ts.HS_SCORE_POS)

    @classmethod
    def high_score_stats(cls, high_scores):
        """Draws the high score stats on the screen.

        Args:
            high_scores: A list of high score dictionaries.
        """
        row_position = 0
        spacing = ts.HS_BODY_SPACING

        for i in range(10):
            if len(high_scores) > i:
                row = high_scores[i]
                score = f"{row['score']:04}"
                name = row['name']
            else:
                score = '----'
                name = '----'

            number = i + 1

            draw_text(str(number), cls.font, ts.HS_BODY_SIZE, cls.color_2,
                      (ts.HS_BODY_NUMBER_POS_X, ts.HS_BODY_POS_Y + row_position))

            draw_text(str(name), cls.font, ts.HS_BODY_SIZE, cls.color_2,
                      (ts.HS_BODY_NAME_POS_X, ts.HS_BODY_POS_Y + row_position))

            draw_text(str(score), cls.font, ts.HS_BODY_SIZE, cls.color_2,
                      (ts.HS_BODY_SCORE_POS_X, ts.HS_BODY_POS_Y + row_position))

            row_position += spacing

        draw_text('press any key to proceed', cls.font,
                  ts.HS_PRESS_ANY_KEY_SIZE, cls.color_1, (ts.HS_PRESS_ANY_KEY_POS_X,
                  ts.HS_BODY_POS_Y + row_position))

    @classmethod
    def enter_name(cls, user_input):
        """Draws the enter name screen.

        Args:
            user_input: The user's input string.
        """
        draw_text('TOP 10 SCORE!', cls.font, ts.ENTER_NAME_TITLE_SIZE,
                  cls.color_2, ts.ENTER_NAME_TITLE_POS)

        draw_text('Enter name:', cls.font, ts.ENTER_NAME_BODY_SIZE,
                  cls.color_1, ts.ENTER_NAME_BODY_POS)

        draw_text(user_input, cls.font, ts.ENTER_NAME_INPUT_SIZE,
                  cls.color_2, ts.ENTER_NAME_INPUT_POS)

    @classmethod
    def win(cls, score):
        """Draws the win screen.

        Args:
            score: The player's score integer.
        """
        draw_text('YOU WIN!', cls.font, ts.YOU_WIN_TITLE_SIZE,
                  cls.color_2, ts.YOU_WIN_TITLE_POS)

        draw_text(f'SCORE: {score:04}', cls.font, ts.YOU_WIN_SCORE_SIZE, cls.color_2,
                  ts.YOU_WIN_SCORE_POS)

        draw_text('Press any key to proceed', cls.font, ts.YOU_WIN_PRESS_ANY_KEY_SIZE,
                  cls.color_2, ts.YOU_WIN_PRESS_ANY_KEY_POS)

    @classmethod
    def game_over(cls):
        """Draws the game over screen."""
        draw_text('GAME OVER', cls.font, ts.GAME_OVER_TITLE_SIZE,
                  cls.color_2, ts.GAME_OVER_TITLE_POS)

        draw_text('Press any key to restart', cls.font, ts.GAME_OVER_PRESS_ANY_KEY_SIZE,
                  cls.color_2, ts.GAME_OVER_PRESS_ANY_KEY_POS)
