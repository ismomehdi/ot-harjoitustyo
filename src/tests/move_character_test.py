import unittest
import pygame
from config.general import TILE_SIZE, PLAYER_SPEED, ENEMY_SPEED, ENEMY_AREA_SIZE, ENEMY_CHASE_SPEED
from services.move_character import move_player, move_enemy
from sprites.player import Player
from unittest.mock import Mock

class TestMoveCharacter(unittest.TestCase):
    def setUp(self):
        self.player_pos_x = 0
        self.player_rect = pygame.Rect(self.player_pos_x, 0, TILE_SIZE, TILE_SIZE)
        self.player_direction = pygame.math.Vector2()
        self.player_speed = PLAYER_SPEED

        self.enemy_starting_pos_x = 0
        self.enemy_rect = pygame.Rect(self.enemy_starting_pos_x, 0, TILE_SIZE, TILE_SIZE)
        self.enemy_direction = pygame.math.Vector2()
        self.enemy_speed = ENEMY_SPEED
        self.enemy_area_size = ENEMY_AREA_SIZE
        self.enemy_chase_speed = ENEMY_CHASE_SPEED

        self.mock_group = Mock()
        self.player_sprite = pygame.sprite.GroupSingle()
        self.player = Player((0,0), self.player_sprite, self.mock_group, self.mock_group, self.mock_group)

    def test_move_player_right_and_left(self):
        self.player_direction.x = 1
        move_player(self.player_rect, self.player_direction, self.player_speed)

        self.player_pos_x += self.player_direction.x * self.player_speed
        self.assertEqual(self.player_rect.x, self.player_pos_x)

        self.player_direction.x = -1
        move_player(self.player_rect, self.player_direction, self.player_speed)

        self.player_pos_x += self.player_direction.x * self.player_speed
        self.assertEqual(self.player_rect.x, self.player_pos_x)

    def test_move_enemy_right_and_left(self):
        self.enemy_direction.x = 1
        move_enemy(self.enemy_rect, self.enemy_direction, self.enemy_speed, 
            self.enemy_starting_pos_x, self.enemy_area_size, self.enemy_chase_speed, self.player_sprite)

        self.enemy_starting_pos_x += self.enemy_direction.x * self.enemy_speed
        self.assertEqual(self.enemy_rect.x, self.enemy_starting_pos_x)

        self.enemy_direction.x = -1
        move_enemy(self.enemy_rect, self.enemy_direction, self.enemy_speed, 
            self.enemy_starting_pos_x, self.enemy_area_size, self.enemy_chase_speed, self.player_sprite)

        self.enemy_starting_pos_x += self.enemy_direction.x * self.enemy_speed
        self.assertEqual(self.enemy_rect.x, self.enemy_starting_pos_x)

    def test_enemy_change_direction_at_the_edge_of_the_area(self):
        self.enemy_rect.x = -1
        self.enemy_direction.x = -1
        move_enemy(self.enemy_rect, self.enemy_direction, self.enemy_speed, 
            self.enemy_starting_pos_x, self.enemy_area_size, self.enemy_chase_speed, self.player_sprite)

        self.assertEqual(self.enemy_direction.x, 1)

        self.enemy_rect.x = self.enemy_starting_pos_x + self.enemy_area_size + 1
        move_enemy(self.enemy_rect, self.enemy_direction, self.enemy_speed, 
            self.enemy_starting_pos_x, self.enemy_area_size, self.enemy_chase_speed, self.player_sprite)

        self.assertEqual(self.enemy_direction.x, -1)

    def test_enemy_chase_player(self):
        self.player_sprite.sprite.rect.x = self.enemy_starting_pos_x + self.enemy_chase_speed + 1
        self.enemy_direction.x = -1

        move_enemy(self.enemy_rect, self.enemy_direction, self.enemy_speed, 
            self.enemy_starting_pos_x, self.enemy_area_size, self.enemy_chase_speed, self.player_sprite)

        self.assertEqual(self.enemy_direction.x, 1)

        self.player_sprite.sprite.rect.x = self.enemy_starting_pos_x - self.enemy_chase_speed - 1
        self.enemy_direction.x = 1

        # Quick fix to make sure the characters are inside the level area
        self.enemy_rect.x += 200
        self.player_sprite.sprite.rect.x += 200


        move_enemy(self.enemy_rect, self.enemy_direction, self.enemy_speed, 
            self.enemy_starting_pos_x, self.enemy_area_size, self.enemy_chase_speed, self.player_sprite)

        self.assertEqual(self.enemy_direction.x, -1)








        

        
