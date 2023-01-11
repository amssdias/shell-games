import unittest
from colorama import Fore
from unittest.mock import MagicMock, Mock
from unittest.mock import patch

from games import Hangman, BattleShip
from models.player import Player
from main.controller import Controller


class TestController(unittest.TestCase):
    def setUp(self) -> None:
        # Mock Player and initial values of player
        mock_player = MagicMock()
        mock_player.name = "Testing"
        mock_player.age = "22"
        mock_player.email = "testing@hotmail.com"

        self.controller = Controller(mock_player)

    def test_initial(self):
        initial_attributes = self.controller.__dict__.keys()
        self.assertIn("player", initial_attributes)

    @patch("builtins.input", return_value="N")
    @patch("builtins.print", return_value=None)
    def test_start(self, mock_print, mock_input):
        mock_player = MagicMock()
        mock_game = MagicMock()
        mock_game.play.return_value = True

        controller = Controller(mock_player)

        # Patch the games attribute of the controller object with a dictionary that contains the mock game object
        patch.object(controller, "games", {"Mock Game": mock_game})

        controller.get_game = MagicMock(return_value=mock_game)
        controller.display_result = MagicMock()

        controller.start()

        controller.get_game.assert_called_once()
        controller.display_result.assert_called_once()
        mock_player.update_games_played.assert_called_once()
        mock_game.play.assert_called_once()

    @patch("builtins.input", side_effect=["Y", "N"])
    @patch("builtins.print", return_value=None)
    def test_start_repeat(self, mock_print, mock_input):
        mock_player = MagicMock()
        mock_game = MagicMock()
        mock_game.play.return_value = True

        controller = Controller(mock_player)

        # Patch the games attribute of the controller object with a dictionary that contains the mock game object
        patch.object(controller, "games", {"Mock Game": mock_game})

        controller.get_game = MagicMock(return_value=mock_game)
        controller.display_result = MagicMock()

        controller.start()

        self.assertEqual(controller.get_game.call_count, 2)
        self.assertEqual(controller.display_result.call_count, 2)
        self.assertEqual(mock_player.update_games_played.call_count, 2)
        self.assertEqual(mock_game.play.call_count, 2)

    @patch("builtins.input", return_value="N")
    @patch("builtins.print", return_value=None)
    def test_start_game_dont_exist(self, mock_print, mock_input):
        mock_player = MagicMock()
        mock_game = MagicMock()
        mock_game.play.return_value = True

        controller = Controller(mock_player)

        # Patch the games attribute of the controller object with a dictionary that contains the mock game object
        patch.object(controller, "games", {"Mock Game": mock_game})

        controller.get_game = MagicMock(side_effect=[False, mock_game])
        controller.display_result = MagicMock()

        controller.start()

        self.assertEqual(controller.get_game.call_count, 2)
        controller.display_result.assert_called_once()
        mock_player.update_games_played.assert_called_once()
        mock_game.play.assert_called_once()
    
    @patch("builtins.input")
    def test_get_game_battleship(self, mock_input):
        self.controller.display_games = MagicMock()
        self.controller.validate_user_game_choice = MagicMock(return_value="Battleship")
        
        result = self.controller.get_game()

        self.controller.display_games.assert_called_once()
        self.controller.validate_user_game_choice.assert_called_once()
        self.assertIsInstance(result, BattleShip)

    @patch("builtins.input")
    def test_get_game_hangman(self, mock_input):
        self.controller.display_games = MagicMock()
        self.controller.validate_user_game_choice = MagicMock(return_value="Hangman")

        result = self.controller.get_game()

        self.controller.display_games.assert_called_once()
        self.controller.validate_user_game_choice.assert_called_once()
        self.assertIsInstance(result, Hangman)

    @patch("builtins.input")
    def test_get_game_dont_exist(self, mock_input):
        self.controller.display_games = MagicMock()
        self.controller.validate_user_game_choice = MagicMock(return_value=False)

        result = self.controller.get_game()

        self.controller.display_games.assert_called_once()
        self.controller.validate_user_game_choice.assert_called_once()
        self.assertIsInstance(result, bool)
        self.assertEqual(result, False)

    @patch("builtins.print")
    def test_display_games(self, mock_print):
        self.controller.display_games()
        values_printed = []
        for game in self.controller.games.keys():
            values_printed.append(f"- {Fore.CYAN}{game}")

        for index, called in enumerate(mock_print.mock_calls):
            self.assertEqual(called.args[0], values_printed[index])

    def test_validate_user_game_choice(self):
        self.assertEqual(self.controller.validate_user_game_choice("hanGmAn"), "Hangman")
        self.assertEqual(self.controller.validate_user_game_choice("HANGman"), "Hangman")
        self.assertEqual(self.controller.validate_user_game_choice("battLeShip"), "Battleship")
        self.assertEqual(self.controller.validate_user_game_choice("BATTLEship"), "Battleship")

    @patch("builtins.print", return_value=None)
    def test_validate_user_game_choice_invalid(self, mock_print):
        self.assertEqual(self.controller.validate_user_game_choice("hannGmAn"), False)
        mock_print.assert_called_once()
        self.assertEqual(self.controller.validate_user_game_choice("HANGmaan"), False)
        self.assertEqual(self.controller.validate_user_game_choice("batLeShip"), False)
        self.assertEqual(self.controller.validate_user_game_choice("BATTLship"), False)

    @patch("builtins.print")
    def test_display_result_won(self, mock_print):
        self.controller.player.update_score = MagicMock()

        self.controller.display_result(won=True)
        value_printed = Fore.GREEN + "You Won!!! :D"

        self.assertEqual(mock_print.mock_calls[0].args[0], value_printed)
        mock_print.assert_called_once()
        self.controller.player.update_score.assert_called_once()
    
    @patch("builtins.print")
    def test_display_result_lost(self, mock_print):
        self.controller.display_result(won=False)
        value_printed = Fore.RED + "You lost!!! :("

        self.assertEqual(mock_print.mock_calls[0].args[0], value_printed)
        mock_print.assert_called_once()
