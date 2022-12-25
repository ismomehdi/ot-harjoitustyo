import unittest
import pygame
from services.finish_screen import FinishScreen

class FinishScreenTest(unittest.TestCase):
    def setUp(self):
        self.finish = FinishScreen()
        pygame.font.init() 
    
    def test_draw_high_score_screen(self):
        self.finish.ready_to_exit = False
        self.finish.draw_high_score_screen(1)
        self.assertTrue(self.finish.ready_to_exit)
    
    def test_draw_game_over_screen(self):
        self.finish.ready_to_exit = False
        self.finish.draw_game_over_screen()
        self.assertTrue(self.finish.ready_to_exit)

    def test_win_screen(self):
        self.finish.ready_to_exit = False
        self.finish.draw_win_screen(100)
        self.assertTrue(self.finish.ready_to_exit)
