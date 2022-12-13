import sys
import pygame
from config.display import display
from config.paths import MAIN_MENU_IMAGES_PATH
from services.import_images import import_folder
from services.timer import timer_start, timer_stop
from menus.menu_init import MenuInit


class MainMenu(MenuInit):
    def __init__(self):
        super().__init__()
        self.state = 'new_game'
        self.game_menu = True
        self.timer_stop = None

        self.images = import_folder(MAIN_MENU_IMAGES_PATH)
        self.image = self.images[self.cursor]

        self.player_image = pygame.image.load(
            'src/assets/images/player/idle/player_idle_frame_01.png')
        self.player_rect = self.player_image.get_rect(bottomleft=(144, 720))

    def process_player_input(self):
        keys = pygame.key.get_pressed()
        self.timer_stop = timer_stop(self.input_timer)

        if keys[pygame.K_RETURN]:
            if self.state == 'new_game':
                self.game_menu = False
            elif self.state == 'options':
                return
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
        self.process_cursor_movement('new_game', 'options', 'quit')

    def run_menu(self):
        self.process_player_input()
        self.image = self.images[self.cursor]
        display.blit(self.image, (0, 0))
        display.blit(self.player_image, self.player_rect)
