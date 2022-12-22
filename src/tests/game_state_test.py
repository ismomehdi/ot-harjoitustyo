import unittest
import pygame
from game_state import GameState

class TestGameState(unittest.TestCase):
    def test_esc_input_leads_to_pause_screen(self):
        self.game = GameState()
        self.game.menu.state['main_menu'] = False

        event = pygame.event.Event(pygame.KEYDOWN)
        event.key = pygame.K_ESCAPE
        pygame.event.post(event)

        self.game.handle_user_input()
        pause_state = self.game.pause.state['on_pause']
        self.assertTrue(pause_state)

    def test_restart(self):
        self.game = GameState()
        self.game.world = None

        self.game.pause.state['restart'] = True
        self.game.run()

        self.assertIsNotNone(self.game.world)




