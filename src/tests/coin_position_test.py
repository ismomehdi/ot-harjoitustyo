import unittest
from build_world import BuildWorld
from config.general import TILE_SIZE
from config.display import display_surface

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
        self.world = BuildWorld(level_map_0, display_surface)

    def assert_coordinates_equal(self, sprite, x):
        self.assertEqual(sprite.rect.x, x)

    def test_coin_position(self):
        coins = self.world.coin_sprites

        for coin in coins:
            self.assert_coordinates_equal(coin, TILE_SIZE)
