from config.display import display
from services.timer import timer_start, timer_stop
from services.import_images import import_folder
from config.paths import PAUSE_MENU_IMAGES_PATH
import sys
import pygame


class PauseMenu:
    def __init__(self):
        self.cursor = 0
        self.state = 'continue'

        self.input_timer = 0
        self.input_delay = 200
        self.on = False
        self.restart = False
        
        self.images = import_folder(PAUSE_MENU_IMAGES_PATH)
        self.image = self.images[self.cursor]

    def get_player_input(self):
        keys = pygame.key.get_pressed()
        self.timer_stop = timer_stop(self.input_timer)

        if keys[pygame.K_RETURN]:
            if self.state == 'continue':
                self.on = False
            elif self.state == 'main_menu':
                self.restart = True
                self.on = False
            elif self.state == 'quit':
                pygame.quit()
                sys.exit()

        elif self.timer_stop < self.input_delay:
            return

        elif keys[pygame.K_DOWN]:
            self.increase_cursor_value()
            self.input_timer = timer_start()

        elif keys[pygame.K_UP]:
            self.decrease_cursor_value()
            self.input_timer = timer_start()

    def increase_cursor_value(self):
        if self.cursor < 2:
            self.cursor += 1
            self.state = self.update_state()

    def decrease_cursor_value(self):
        if self.cursor > 0:
            self.cursor -= 1
            self.state = self.update_state()

    def update_state(self):
        if self.cursor == 0:
            self.state = 'continue'
        elif self.cursor == 1:
            self.state = 'main_menu'
        elif self.cursor == 2:
            self.state = 'quit'

        return self.state

    def run_menu(self):
        self.get_player_input()
        self.image = self.images[self.cursor]
        display.blit(self.image, (0, 0))
        