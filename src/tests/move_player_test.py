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
    'P                           f                           ',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']


class TestWorld(unittest.TestCase):
    def setUp(self):
        self.world = BuildWorld(level_map_0, display_surface)

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

    def test_check_if_reached_goal(self):
        self.world.player.rect.x = 150
        self.world.goal.rect.x = 100
        self.world.check_if_reached_goal()

        self.assertTrue(self.world.reached_goal)

    def test_check_if_didnt_reach_goal(self):
        self.world.player.rect.x = 10
        self.world.goal.rect.x = 200
        self.world.check_if_reached_goal()

        self.assertFalse(self.world.reached_goal)

