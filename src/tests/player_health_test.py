import unittest
import pygame
from unittest.mock import Mock
from sprites.player import Player

class PlayerHealthTest(unittest.TestCase):
    def setUp(self):
        self.mock_group = Mock()
        self.player_sprite = pygame.sprite.GroupSingle()
        self.player = Player((0,0), self.player_sprite, self.mock_group, self.mock_group, self.mock_group)
        self.player._player_health = 3

    def test_decrease_player_health(self):
        self.player.decrease_health()
        self.player.invincible = False
        self.player.decrease_health()
        self.player.invincible = False
        self.player.decrease_health()

        self.assertTrue(self.player.dead)

    def test_player_invincibility(self):
        self.player.decrease_health()
        self.assertTrue(self.player.invincible)
        self.player._grace_period = 0
        self.player.hurt_timer()
        self.assertFalse(self.player.invincible)

    def test_get_player_score(self):
        self.assertEqual(self.player.score, self.player.get_score())