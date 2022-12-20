import pygame
from services.draw_text import draw_text
from config.display import DISPLAY_WIDTH, DISPLAY_HEIGHT

class FinishScreen:
    def __init__(self):
        self.font = 'src/assets/fonts/Broken Console Bold.ttf'
        self.color = '#b392ac'
        self.upper_text_size = 80
        self.lower_text_size = 50
        self.center_pos_x = DISPLAY_WIDTH / 2
        self.center_pos_y = DISPLAY_HEIGHT / 2
        self.ready_to_exit = False
        self.exit = False

    def keys_released(self):
        keys = pygame.key.get_pressed()
        return not any(keys)

    def key_pressed(self):
        keys = pygame.key.get_pressed()
        return any(keys)

    def run(self, points):
        draw_text('YOU WIN!', self.font, self.upper_text_size, self.color, (self.center_pos_x, self.center_pos_y - 70))
        draw_text(f'{points:04} points', self.font, self.lower_text_size, self.color, (self.center_pos_x, self.center_pos_y))
        draw_text(f'Press any key to proceed', self.font, self.lower_text_size -30, self.color, (self.center_pos_x, self.center_pos_y + 45))

        if self.keys_released():
            self.ready_to_exit = True

        if self.key_pressed() and self.ready_to_exit:
            self.exit = True