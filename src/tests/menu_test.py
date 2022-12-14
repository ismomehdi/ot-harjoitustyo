import unittest
import pygame
from menus.main_menu import MainMenu
from menus.pause_menu import PauseMenu
from menus.menu_init import MenuInit

class TestMenus(unittest.TestCase):
    def setUp(self):
        self.menu_init = MenuInit()
        self.main_menu = MainMenu()
        self.pause_menu = PauseMenu()

        self.keys = {}

    def test_main_menu_up_and_down_key_input(self):
        self.keys[pygame.K_DOWN] = True

        self.main_menu.process_up_and_down_keys(self.keys)
        self.assertEqual(self.main_menu.cursor, 1)
        self.main_menu.process_up_and_down_keys(self.keys)
        self.assertEqual(self.main_menu.cursor, 2)

        self.keys[pygame.K_DOWN] = False
        self.keys[pygame.K_UP] = True

        self.main_menu.process_up_and_down_keys(self.keys)
        self.assertEqual(self.main_menu.cursor, 1)
        self.main_menu.process_up_and_down_keys(self.keys)
        self.assertEqual(self.main_menu.cursor, 0)

    def test_pause_menu_up_and_down_key_input(self):
        self.keys[pygame.K_DOWN] = True

        self.pause_menu.process_up_and_down_keys(self.keys)
        self.assertEqual(self.pause_menu.cursor, 1)
        self.pause_menu.process_up_and_down_keys(self.keys)
        self.assertEqual(self.pause_menu.cursor, 2)

        self.keys[pygame.K_DOWN] = False
        self.keys[pygame.K_UP] = True

        self.pause_menu.process_up_and_down_keys(self.keys)
        self.assertEqual(self.pause_menu.cursor, 1)
        self.pause_menu.process_up_and_down_keys(self.keys)
        self.assertEqual(self.pause_menu.cursor, 0)

    def test_menu_init_return_key(self):
        self.keys[pygame.K_RETURN] = True

        self.menu_init.process_return_key(self.keys)
        self.assertEqual(self.menu_init.option, None)

        self.main_menu.process_return_key(self.keys)
        self.assertEqual(self.main_menu.option, 'new_game')

        self.pause_menu.process_return_key(self.keys)
        self.assertEqual(self.pause_menu.option, 'continue')

        self.menu_init.option = 'main_menu'
        self.menu_init.process_return_key(self.keys)
        self.assertEqual(self.menu_init.state['restart'], True)
        self.assertEqual(self.menu_init.state['on_pause'], False)