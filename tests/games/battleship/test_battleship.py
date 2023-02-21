import string
import unittest
from colorama import Fore
from unittest.mock import patch
from games.abstracts.board import Board

from games.battleship import BattleShip
from games.battleship.constants.ships_names import ShipsNames


class TestBattleship(unittest.TestCase):
    def setUp(self) -> None:
        self.game = BattleShip()

    def test_battleship_initial(self):
        battleship_initial_variables = self.game.__dict__.keys()
        self.assertIn("ships", battleship_initial_variables)
        self.assertIn("user_points", battleship_initial_variables)
        self.assertIn("board", battleship_initial_variables)

        self.assertIsInstance(self.game.ships, dict)
        self.assertIsInstance(self.game.board, Board)
        self.assertIsInstance(self.game.user_points, int)

    @patch("builtins.print", return_value=None)
    def test_start_game(self, mock_print):
        self.game.start_game_settings()

        with patch("builtins.input") as mock_input:
            s = list(self.game.ships.ships_positions)
            ships_positions = self._change_rows_for_alphabet(s)
            mock_input.side_effect = ships_positions
            mock_input.return_value = None

            user_won = self.game.start_game()

            self.assertEqual(user_won, True)

    @staticmethod
    def _change_rows_for_alphabet(ships_positions):
        ascii_upper = string.ascii_uppercase

        new_ship_positions = list()
        for row, column in list(ships_positions):
            row_letter = ascii_upper[row]
            new_ship_positions.append(f"{row_letter}-{column + 1}")

        return new_ship_positions

    @patch("builtins.print", return_value=None)
    def test_validate_user_shot(self, mocked_print):
        self.game.start_game_settings()
        self.assertEqual(self.game.validate_user_shot("D-5"), (3, 4))
        self.assertEqual(self.game.validate_user_shot("5-D"), (3, 4))
        self.assertEqual(self.game.validate_user_shot("5--D"), (3, 4))
        self.assertEqual(self.game.validate_user_shot("D5"), False)
        self.assertEqual(self.game.validate_user_shot("5D"), False)
        self.assertEqual(self.game.validate_user_shot("5d"), False)
        self.assertEqual(self.game.validate_user_shot("d5"), False)
        self.assertEqual(self.game.validate_user_shot("D 5"), False)
        self.assertEqual(self.game.validate_user_shot("5 D"), False)
        self.assertEqual(self.game.validate_user_shot("5 - D"), False)
        self.assertEqual(self.game.validate_user_shot("5/D"), False)
        self.assertEqual(self.game.validate_user_shot("-5D"), False)
        self.assertEqual(self.game.validate_user_shot("5D-"), False)
        self.assertEqual(self.game.validate_user_shot("5-J"), (9, 4))
        self.assertEqual(self.game.validate_user_shot("5-K"), False)
        self.assertEqual(self.game.validate_user_shot("-K"), False)
        self.assertEqual(self.game.validate_user_shot("3-"), False)

    def test_print_boat_hit(self):
        with patch("builtins.print", return_value=None) as mock_print:
            self.game.start_game_settings()

            ship_position = tuple(self.game.ships[ShipsNames.CARRIER.value]["position"])[0]
            self.game.print_boat_hit(coordinates=ship_position)

            self.assertNotIn(ship_position, self.game.ships.ships_positions)

    def test_check_user_won(self):
        self.assertEqual(self.game.check_user_won(), True)
        self.game.ships.ships_positions.add((4, 5))
        self.assertEqual(self.game.check_user_won(), False)
