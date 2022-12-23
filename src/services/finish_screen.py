import pygame
from services.draw_text import draw_text
from config.display import DISPLAY_WIDTH, DISPLAY_HEIGHT
from db.high_score_repository import HighScoreRepository


class FinishScreen:
    def __init__(self):
        self.font = 'src/assets/fonts/Broken Console Bold.ttf'
        self.color = '#b392ac'
        self.lower_text_size = 70
        self.upper_text_size = 50
        self.center_pos_x = DISPLAY_WIDTH / 2
        self.center_pos_y = DISPLAY_HEIGHT / 2
        self.ready_to_exit = False
        self.win_screen = True
        self.high_score = False
        self.high_scores_screen = False
        self.user_input = ''
        self.database = HighScoreRepository()

    def keys_released(self):
        keys = pygame.key.get_pressed()
        return not any(keys)

    def key_pressed(self):
        keys = pygame.key.get_pressed()
        return any(keys)

    def draw_win_screen(self, score):
        level = 1

        draw_text('YOU WIN!', self.font, self.lower_text_size,
                  self.color, (self.center_pos_x, self.center_pos_y - 70))
        draw_text(f'SCORE: {score:04}', self.font, self.upper_text_size,
                  self.color, (self.center_pos_x, self.center_pos_y))
        draw_text('Press any key to proceed', self.font, self.upper_text_size -
                  30, self.color, (self.center_pos_x, self.center_pos_y + 45))

        if self.keys_released():
            self.ready_to_exit = True

        if self.ready_to_exit and self.key_pressed():
            self.high_score = self.database.check_if_top_ten(score, level)
            self.win_screen = False

            if not self.high_score:
                self.high_scores_screen = True

            self.ready_to_exit = False

    def draw_enter_name_screen(self):
        draw_text('TOP 10 SCORE!', self.font, 60, self.color,
                  (self.center_pos_x, self.center_pos_y - 70))
        draw_text('Enter name:', self.font, 30, '#735d78',
                  (self.center_pos_x, self.center_pos_y - 20))
        draw_text(self.user_input, self.font, self.upper_text_size,
                  self.color, (self.center_pos_x, self.center_pos_y + 30))

    def enter_name(self, score):
        self.database.add(1, self.user_input, score)

    def draw_high_scores(self):
        level = 1
        high_scores = self.database.get_top_ten(level)
        pos = 170
        number = 1

        draw_text('HIGH SCORES', 'src/assets/fonts/Broken Console Bold.ttf',
                  60, '#735d78', (self.center_pos_x + 15, self.center_pos_y - pos - 60))

        draw_text('#', self.font, 30, '#735d78',
                  (self.center_pos_x - 205, self.center_pos_y - pos - 5))
        draw_text('name', self.font, 30, '#735d78',
                  (self.center_pos_x, self.center_pos_y - pos - 5))
        draw_text('score', self.font, 30, '#735d78',
                  (self.center_pos_x + 195, self.center_pos_y - pos - 5))

        for i in range(10):
            pos -= 30

            if len(high_scores) > i:
                row = high_scores[i]
            else:
                row = {'name': None, 'score': None}

            score = '----' if row['score'] is None else f"{row['score']:04}"
            name = '----' if row['name'] is None else row['name']
            number = i + 1

            draw_text(str(number), self.font, 30, self.color,
                      (self.center_pos_x - 205, self.center_pos_y - pos))
            draw_text(str(name), self.font, 30, self.color,
                      (self.center_pos_x, self.center_pos_y - pos))
            draw_text(str(score), self.font, 30, self.color,
                      (self.center_pos_x + 195, self.center_pos_y - pos))

        draw_text('press any key to proceed', self.font, 25, '#735d78',
                  (self.center_pos_x + 5, self.center_pos_y - pos + 40))

        if self.keys_released():
            self.ready_to_exit = True

        if self.ready_to_exit and self.key_pressed():
            self.high_scores_screen = False
