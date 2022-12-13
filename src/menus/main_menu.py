from config.display import display
from config.paths import MAIN_MENU_IMAGES_PATH
from services.timer import timer_start, timer_stop
from services.import_images import import_folder
import sys
import pygame


class MainMenu:
    def __init__(self):
        self.cursor = 0
        self.state = 'new_game'

        self.input_timer = 0
        self.input_delay = 200
        self.game_menu = True
        
        self.images = import_folder(MAIN_MENU_IMAGES_PATH)
        self.image = self.images[self.cursor]

        self.player_image = pygame.image.load(
            'src/assets/images/player/idle/player_idle_frame_01.png')
        self.player_rect = self.player_image.get_rect(bottomleft=(144, 720))

    def get_player_input(self):
        keys = pygame.key.get_pressed()
        self.timer_stop = timer_stop(self.input_timer)

        if keys[pygame.K_RETURN]:
            if self.state == 'new_game':
                self.game_menu = False
            elif self.state == 'options':
                pass
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
            self.state = 'new_game'
        elif self.cursor == 1:
            self.state = 'options'
        elif self.cursor == 2:
            self.state = 'quit'

        return self.state

    def run_menu(self):
        self.get_player_input()
        self.image = self.images[self.cursor]
        display.blit(self.image, (0, 0))
        display.blit(self.player_image, self.player_rect)
