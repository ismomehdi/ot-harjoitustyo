import unittest
from world import World
from maps import TILE_SIZE
from display import display_surface

level_map_0 = [
    '                                                        ',
    '                                                        ',
    '                                                        ',
    '                                                        ',
    '                                                        ',
    '                                                        ',
    '                                                        ',
    '                                                        ',
    '                                                        ',
    '                                                        ',
    ' o                                                      ',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']


class TestWorld(unittest.TestCase):
    def setUp(self):
        self.world = World(level_map_0, display_surface)

    def assert_coordinates_equal(self, sprite, x):
        self.assertEqual(sprite.rect.x, x)

    def test_coin_position(self):
        coins = self.world.coin_sprite_group

        for coin in coins:
            self.assert_coordinates_equal(coin, TILE_SIZE)

        
