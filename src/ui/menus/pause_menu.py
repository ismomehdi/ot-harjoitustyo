import pygame
from config.display import display
from config.paths import PAUSE_MENU_IMAGES_PATH
from services.import_images import import_folder
from ui.menus.menu_init import MenuInit


class PauseMenu(MenuInit):
    def __init__(self):
        """The PauseMenu class is used to run the pause menu.
        """
        super().__init__()
        self.options = ['continue', 'main_menu', 'quit']
        self.option = self.options[self.cursor]

        self.images = import_folder(PAUSE_MENU_IMAGES_PATH)
        self.image = self.images[self.cursor]

    def run_menu(self):
        """Runs the pause menu.
        """
        self.process_player_input(pygame.key.get_pressed())
        self.image = self.images[self.cursor]
        display.blit(self.image, (0, 0))
