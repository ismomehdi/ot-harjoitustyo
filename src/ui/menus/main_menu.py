import pygame
from config.display import display
from config.paths import MAIN_MENU_IMAGES_PATH
from services.import_images import import_folder
from ui.menus.menu_init import MenuInit


class MainMenu(MenuInit):
    def __init__(self):
        """The MainMenu class is used to run the main menu.
        """
        super().__init__()
        self.options = ['new_game', 'options', 'quit']
        self.option = self.options[self.cursor]

        self.images = import_folder(MAIN_MENU_IMAGES_PATH)
        self.image = self.images[self.cursor]

        self.player_image = pygame.image.load(
            'src/assets/images/player/idle/player_idle_frame_01.png')
        self.player_rect = self.player_image.get_rect(bottomleft=(144, 720))

    def run_menu(self):
        """Runs the main menu.
        """
        self.process_player_input(pygame.key.get_pressed())
        self.image = self.images[self.cursor]
        display.blit(self.image, (0, 0))
        display.blit(self.player_image, self.player_rect)
