import unittest
from unittest.mock import patch

from games.abstracts.game import Game


class TestGame(unittest.TestCase):
    """
    If you set __abstractmethods__ attribute to be an empty set you'll be able to instantiate abstract class.
    """

    def setUp(self) -> None:
        Game.__abstractmethods__ = set()
        self.game = Game()
        return super().setUp()

    @patch("games.game.Game.start_game_settings", return_value=None)
    @patch("games.game.Game.start_game", return_value=True)
    def test_play_won(self, mock_start_game, mock_game_settings):
        self.assertTrue(self.game.play())

    @patch("games.game.Game.start_game_settings", return_value=None)
    @patch("games.game.Game.start_game", return_value=False)
    def test_play_lost(self, mock_start_game, mock_game_settings):
        self.assertFalse(self.game.play())
