import unittest
import pygame
from config.general import PLAYER_JUMP_SPEED
from services.player_input import player_input

class TestPlayerInput(unittest.TestCase):
    def setUp(self):
        self.keys = {}
        self.direction = pygame.math.Vector2()
        self.jump_speed = PLAYER_JUMP_SPEED
        self.player_on_ground = True

        self.keys[pygame.K_RIGHT] = False
        self.keys[pygame.K_LEFT] = False
        self.keys[pygame.K_UP] = False

    def test_player_right_key_input(self):
        self.keys[pygame.K_RIGHT] = True

        player_input(self.direction, self.jump_speed, self.player_on_ground, self.keys)

        self.assertEqual(self.direction.x, 1)

    def test_player_left_key_input(self):
        self.keys[pygame.K_LEFT] = True

        player_input(self.direction, self.jump_speed, self.player_on_ground, self.keys)

        self.assertEqual(self.direction.x, -1)

    def test_player_up_key_input(self):
        self.keys[pygame.K_UP] = True

        player_input(self.direction, self.jump_speed, self.player_on_ground, self.keys)

        self.assertEqual(self.direction.y, -self.jump_speed)    

        