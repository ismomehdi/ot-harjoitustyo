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

        self.assert_coordinates_equal(player, 0, 10 * TILE_SIZE)

        player.rect.x += TILE_SIZE
        self.assert_coordinates_equal(
            player, TILE_SIZE, 10 * TILE_SIZE)

        player.rect.y += TILE_SIZE
        self.assert_coordinates_equal(
            player, TILE_SIZE, 11 * TILE_SIZE)
