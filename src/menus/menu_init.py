import sys
import pygame
from services.timer import timer_start, timer_stop


class MenuInit:
    def __init__(self):
        """The MenuInit class is used to initialize the pause and
            the main menus.
        """
        self.cursor = 0
        self.options = []
        self.option = None

        self.state = {
            'on_pause': False,
            'restart': False,
            'main_menu': True
        }

        self.input_delay = 170
        self.input_timer = 0
        self.timer_stop = None

    def increase_cursor_value(self, options):
        """Increases the menu cursor value.

        Args:
            options: A list of menu options.
        """
        if self.cursor < 2:
            self.cursor += 1
            self.option = self.process_cursor_value(options)

    def decrease_cursor_value(self, options):
        """Decreases the menu cursor value.

        Args:
            options: A list of menu options.
        """
        if self.cursor > 0:
            self.cursor -= 1
            self.option = self.process_cursor_value(options)

    def process_cursor_value(self, options):
        """Updates the self.option value based on the cursor value.

        Args:
            options: A list of menu options.

        Returns:
            string: A string representing the current menu option.
        """
        if self.cursor == 0:
            self.option = options[0]
        elif self.cursor == 1:
            self.option = options[1]
        elif self.cursor == 2:
            self.option = options[2]

        return self.option

    def process_player_input(self, keys):
        """Processes the player input.

        Args:
            keys: pygame.key.get_pressed() object.
        """
        self.timer_stop = timer_stop(self.input_timer)

        self.process_return_key(keys)

        if self.timer_stop < self.input_delay:
            return

        self.process_up_and_down_keys(keys)
        self.process_cursor_value(self.options)

    def process_return_key(self, keys):
        """Processes the return key input.

        Args:
            keys: pygame.key.get_pressed() object.
        """
        if keys[pygame.K_RETURN]:

            if self.option == 'new_game':
                self.state['main_menu'] = False

            elif self.option == 'continue':
                self.state['on_pause'] = False

            elif self.option == 'options':
                pass

            elif self.option == 'main_menu':
                self.state['restart'] = True
                self.state['on_pause'] = False

            elif self.option == 'quit':
                pygame.quit()
                sys.exit()

    def process_up_and_down_keys(self, keys):
        """Processes the up and down keys input.

        Args:
            keys: pygame.key.get_pressed() object.
        """
        if keys[pygame.K_DOWN]:
            self.increase_cursor_value(self.options)
            self.input_timer = timer_start()

        elif keys[pygame.K_UP]:
            self.decrease_cursor_value(self.options)
            self.input_timer = timer_start()
