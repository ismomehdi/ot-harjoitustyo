import unittest
import pygame
from services.animate_character import AnimateCharacter
from unittest.mock import Mock
from config import paths

class TestAnimateCharacter(unittest.TestCase):
    def setUp(self):
        self.animate_character = AnimateCharacter(paths.PLAYER_IMAGES_PATH)
        self.direction = pygame.math.Vector2()
        self.ground = False

        self.collisions = Mock()
        self.collisions.ground = False


    def test_get_status(self):
        self.direction.x = 1
        self.animate_character.get_status(self.direction, self.collisions, False, False)
        self.assertEqual(self.animate_character.moving_forward, True)

        self.direction.x = -1
        self.animate_character.get_status(self.direction, self.collisions, False, False)
        self.assertEqual(self.animate_character.moving_forward, False)

        invincible = True
        self.animate_character.get_status(self.direction, self.collisions, invincible, False)
        self.assertEqual(self.animate_character.status, 'hurt')

        invincible = False
        dead = True
        self.animate_character.get_status(self.direction, self.collisions, invincible, dead)
        self.assertEqual(self.animate_character.status, 'death')

        dead = False
        self.direction.y = -1
        self.animate_character.get_status(self.direction, self.collisions, invincible, dead)
        self.assertEqual(self.animate_character.status, 'jump')

        self.direction.y = 0
        self.direction.x = 1
        self.collisions.on_ground = True
        self.animate_character.get_status(self.direction, self.collisions, invincible, dead)
        self.assertEqual(self.animate_character.status, 'run')

        self.direction.x = 0
        self.animate_character.get_status(self.direction, self.collisions, invincible, dead)
        self.assertEqual(self.animate_character.status, 'idle')

    def test_animate(self):
        self.animate_character.frame_index = len(self.animate_character.animations[self.animate_character.status]) + 1
        self.animate_character.animate(self.direction, self.collisions)
        self.assertEqual(self.animate_character.frame_index, 0)

