import unittest
from world import World
from sprites.ground_tile import ground_tile_size
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
    'P                                                       ',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']


class TestWorld(unittest.TestCase):
    def setUp(self):
        self.world = World(level_map_0, display_surface)

    def assert_coordinates_equal(self, sprite, x, y):
        self.assertEqual(sprite.rect.x, x)
        self.assertEqual(sprite.rect.y, y)

    def test_can_move_on_ground(self):
        player = self.world.player

        self.assert_coordinates_equal(player, 0, 10 * ground_tile_size)

        player.rect.x += ground_tile_size
        self.assert_coordinates_equal(
            player, ground_tile_size, 10 * ground_tile_size)

        player.rect.y += ground_tile_size
        self.assert_coordinates_equal(
            player, ground_tile_size, 11 * ground_tile_size)
