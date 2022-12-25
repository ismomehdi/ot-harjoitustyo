from services.draw_text import draw_text
from config.paths import BROKEN_CONSOLE_FONT
from config.text_settings import *

class Text:
    font = BROKEN_CONSOLE_FONT
    color_1 = PURPLE
    color_2 = PINK

    @classmethod
    def score(cls, score):
        """Draws the score on the screen."""

        draw_text(f'SCORE: {score:04}', cls.font, SCORE_SIZE, cls.color_1, SCORE_POSITION)

    @classmethod
    def high_score_titles(cls):
        """Draws the titles for the high score screen."""

        draw_text('HIGH SCORES', cls.font, HS_TITLE_SIZE, cls.color_1, HS_TITLE_POS)
        draw_text('#', cls.font, HS_COLUMN_NAME_SIZE, cls.color_1, HS_NUMBER_POS)
        draw_text('name', cls.font, HS_COLUMN_NAME_SIZE, cls.color_1, HS_NAME_POS)
        draw_text('score', cls.font, HS_COLUMN_NAME_SIZE, cls.color_1, HS_SCORE_POS)

    @classmethod
    def high_score_stats(cls, high_scores):
        row_position = 0
        spacing = HS_BODY_SPACING

        for i in range(10):
            if len(high_scores) > i:
                row = high_scores[i]
                score = f"{row['score']:04}"
                name = row['name']
            else:
                score = '----'
                name = '----'

            number = i + 1

            draw_text(str(number), cls.font, HS_BODY_SIZE, cls.color_2, (HS_BODY_NUMBER_POS_X, HS_BODY_POS_Y + row_position))
            draw_text(str(name), cls.font, HS_BODY_SIZE, cls.color_2, (HS_BODY_NAME_POS_X, HS_BODY_POS_Y + row_position))
            draw_text(str(score), cls.font, HS_BODY_SIZE, cls.color_2, (HS_BODY_SCORE_POS_X, HS_BODY_POS_Y + row_position))

            row_position += spacing

        draw_text('press any key to proceed', cls.font, HS_PRESS_ANY_KEY_SIZE, cls.color_1,
            (645, 220 + row_position))

    @classmethod
    def enter_name(cls, input):

        draw_text('TOP 10 SCORE!', cls.font, ENTER_NAME_TITLE_SIZE, cls.color_2, ENTER_NAME_TITLE_POS)
        draw_text('Enter name:', cls.font, ENTER_NAME_BODY_SIZE, cls.color_1, ENTER_NAME_BODY_POS)
        draw_text(input, cls.font, ENTER_NAME_INPUT_SIZE, cls.color_2, ENTER_NAME_INPUT_POS)

    @classmethod
    def win(cls, score):

        draw_text('YOU WIN!', cls.font, YOU_WIN_TITLE_SIZE, cls.color_2, YOU_WIN_TITLE_POS)
        draw_text(f'SCORE: {score:04}', cls.font, YOU_WIN_SCORE_SIZE, cls.color_2, YOU_WIN_SCORE_POS)
        draw_text('Press any key to proceed', cls.font, YOU_WIN_PRESS_ANY_KEY_SIZE, cls.color_2, YOU_WIN_PRESS_ANY_KEY_POS)

    @classmethod
    def game_over(cls):

        draw_text('GAME OVER', cls.font, GAME_OVER_TITLE_SIZE, cls.color_2, GAME_OVER_TITLE_POS)
        draw_text('Press any key to restart', cls.font, GAME_OVER_PRESS_ANY_KEY_SIZE, cls.color_2, GAME_OVER_PRESS_ANY_KEY_POS)





# self.center_pos_x = 640
# self.center_pos_y = 360