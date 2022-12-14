import unittest
import pygame
from unittest.mock import Mock
from menus.main_menu import MainMenu
from menus.pause_menu import PauseMenu

class TestMenus(unittest.TestCase):
    def setUp(self):
        self.main_menu = MainMenu()
        self.pause_menu = PauseMenu()

        self.mock_keys = {}

    def test_main_menu_up_and_down_key_input(self):
        self.mock_keys[pygame.K_DOWN] = True

        self.main_menu.process_up_and_down_keys(self.mock_keys)
        self.assertEqual(self.main_menu.cursor, 1)
        self.main_menu.process_up_and_down_keys(self.mock_keys)
        self.assertEqual(self.main_menu.cursor, 2)

        self.mock_keys[pygame.K_DOWN] = False
        self.mock_keys[pygame.K_UP] = True

        self.main_menu.process_up_and_down_keys(self.mock_keys)
        self.assertEqual(self.main_menu.cursor, 1)
        self.main_menu.process_up_and_down_keys(self.mock_keys)
        self.assertEqual(self.main_menu.cursor, 0)

    def test_pause_menu_up_and_down_key_input(self):
        self.mock_keys[pygame.K_DOWN] = True

        self.pause_menu.process_up_and_down_keys(self.mock_keys)
        self.assertEqual(self.pause_menu.cursor, 1)
        self.pause_menu.process_up_and_down_keys(self.mock_keys)
        self.assertEqual(self.pause_menu.cursor, 2)

        self.mock_keys[pygame.K_DOWN] = False
        self.mock_keys[pygame.K_UP] = True

        self.pause_menu.process_up_and_down_keys(self.mock_keys)
        self.assertEqual(self.pause_menu.cursor, 1)
        self.pause_menu.process_up_and_down_keys(self.mock_keys)
        self.assertEqual(self.pause_menu.cursor, 0)

