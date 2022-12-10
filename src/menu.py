from config.display import display
from services.draw_text import draw_text
import pygame


class Menu:
    def __init__(self):
        self.title_font = './src/assets/fonts/PixelStick-Regular.ttf'
        self.title_shadow_font = './src/assets/fonts/PixelStick-Regular.ttf'
        self.body_font = './src/assets/fonts/PixelStick-Regular.ttf'

        self.font_size = 80
        self.title_font_size = 100
        self.font_color = '#5D6E80'
        self.center_x, self.center_y = display.get_width() / 2, display.get_height() / 2

    def run_menu(self):
        draw_text('HOKU', self.title_shadow_font, self.title_font_size, '#869EB8', (self.center_x - 5, self.center_y - 208))
        draw_text('HOKU', self.title_font, self.title_font_size, '#5D6C6E', (self.center_x, self.center_y - 210))



        draw_text('-> NEW GAME <-', self.body_font, self.font_size, self.font_color, (self.center_x, self.center_y - 90))
        draw_text('OPTIONS', self.body_font, self.font_size, self.font_color, (self.center_x, self.center_y - 10))
        draw_text('QUIT GAME', self.body_font, self.font_size, self.font_color, (self.center_x, self.center_y + 70))
