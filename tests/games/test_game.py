import unittest
from unittest.mock import patch

from games.game import Game


class TestGameABC(unittest.TestCase):
    """
    If you set __abstractmethods__ attribute to be an empty set you'll be able to instantiate abstract class.
    """

    @patch("games.game.Game.start_game_settings", return_value=None)
    @patch("games.game.Game.start_game", return_value=True)
    def test_play_won(self, mocked_start_game, mocked_game_settings):
        Game.__abstractmethods__ = set()
        self.assertTrue(Game().play())

    @patch("games.game.Game.start_game_settings", return_value=None)
    @patch("games.game.Game.start_game", return_value=False)
    def test_play_lost(self, mocked_start_game, mocked_game_settings):
        Game.__abstractmethods__ = set()
        self.assertFalse(Game().play())