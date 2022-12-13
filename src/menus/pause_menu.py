import sys
import pygame
from config.display import display
from config.paths import PAUSE_MENU_IMAGES_PATH
from services.timer import timer_start, timer_stop
from services.import_images import import_folder
from menus.menu_init import MenuInit


class PauseMenu(MenuInit):
    def __init__(self):
        super().__init__()
        self.state = 'continue'
        self.timer_stop = None

        self.active = False
        self.restart = False

        self.images = import_folder(PAUSE_MENU_IMAGES_PATH)
        self.image = self.images[self.cursor]

    def process_player_input(self):
        keys = pygame.key.get_pressed()
        self.timer_stop = timer_stop(self.input_timer)

        if keys[pygame.K_RETURN]:
            if self.state == 'continue':
                self.active = False
            elif self.state == 'main_menu':
                self.restart = True
                self.active = False
            elif self.state == 'quit':
                pygame.quit()
                sys.exit()

        elif self.timer_stop < self.input_delay:
            return

        elif keys[pygame.K_DOWN]:
            self.increase_cursor_value(self.update_state)
            self.input_timer = timer_start()

        elif keys[pygame.K_UP]:
            self.decrease_cursor_value(self.update_state)
            self.input_timer = timer_start()

    def update_state(self):
        if self.cursor == 0:
            self.state = 'continue'
        elif self.cursor == 1:
            self.state = 'main_menu'
        elif self.cursor == 2:
            self.state = 'quit'

        return self.state

    def run_menu(self):
        self.process_player_input()
        self.image = self.images[self.cursor]
        display.blit(self.image, (0, 0))
