import unittest
from unittest.mock import MagicMock, patch

from colorama import Fore

from games.battleship.battleship_board import BattleshipBoard


class TestBattleshipBoard(unittest.TestCase):
    def setUp(self) -> None:
        self.battleship_board = BattleshipBoard(10, 10)

    def test_battleshipboard_initial(self):
        battleshipboard_initial_variables = self.battleship_board.__dict__.keys()
        self.assertIn("positions", battleshipboard_initial_variables)

    def test_build_battlefield(self):
        board = [["." for _ in range(10)] for _ in range(10)]
        self.assertEqual(self.battleship_board.build_board(10, 10), board)

    def test_display_board(self):
        self.battleship_board.print_battlefield_columns = MagicMock()
        self.battleship_board.print_battlefield_rows = MagicMock()
        self.battleship_board.display_board()

        self.battleship_board.print_battlefield_columns.assert_called_once()
        self.battleship_board.print_battlefield_rows.assert_called_once()

    def test_print_battlefield_columns(self):
        with patch("builtins.print", return_value=None) as mock_print:
            result = self.battleship_board.print_battlefield_columns()

            self.assertEqual(result, None)
            mock_print.assert_called()

    def test_print_battlefield_rows(self):
        with patch("builtins.print", return_value=None) as mock_print:
            result = self.battleship_board.print_battlefield_rows()

            self.assertEqual(result, None)
            mock_print.assert_called()

    def test_mark_board_position_hit_true(self):
        self.battleship_board.mark_board_position(hit=True, coordinates=(3, 2))
        self.assertEqual(self.battleship_board.positions[3][2], Fore.RED + "X")

    def test_mark_board_position_hit_false(self):
        self.battleship_board.mark_board_position(hit=False, coordinates=(2, 2))
        self.assertEqual(self.battleship_board.positions[2][2], Fore.LIGHTBLUE_EX + "O")
