import string
import unittest
from colorama import Fore
from unittest.mock import patch

from games.battleship import BattleShip


class TestBattleship(unittest.TestCase):
    def setUp(self) -> None:
        self.game = BattleShip()

    def test_battleship_initial(self):
        battleship_initial_variables = self.game.__dict__.keys()
        self.assertIn("ships", battleship_initial_variables)
        self.assertIn("ships_positions", battleship_initial_variables)
        self.assertIn("user_points", battleship_initial_variables)
        self.assertIn("battlefield", battleship_initial_variables)

        self.assertIsInstance(self.game.ships, dict)
        self.assertIsInstance(self.game.ships_positions, set)
        self.assertIsInstance(self.game.battlefield, list)
        self.assertIsInstance(self.game.user_points, int)

        ships = self.game.ships.keys()
        self.assertIn("carrier", ships)
        self.assertIn("battleship", ships)
        self.assertIn("cruiser", ships)
        self.assertIn("submarine", ships)
        self.assertIn("destroyer", ships)

    def test_build_battlefield(self):
        battlefield = [["." for _ in range(10)] for _ in range(10)]
        self.assertEqual(self.game.build_battlefield(), battlefield)

    def test_set_ships_positions(self):
        self.game.set_ships_positions()

        self.assertTrue(self.game.ships_positions)

        len_all_ships = 0
        for ship_values in self.game.ships.values():
            self.assertIn("position", ship_values)

            if ship_values.get("position"):
                len_all_ships += len(ship_values["position"])

        self.assertEqual(len(self.game.ships_positions), len_all_ships)

    def test_get_ship_positions_horizontal(self):
        ship_positions = self.game.get_ship_positions_horizontal(
            ship_size=5, ship_column=9, ship_row=9
        )
        self.assertEqual(ship_positions, {(9, 9), (9, 8), (9, 7), (9, 6), (9, 5)})

        ship_positions = self.game.get_ship_positions_horizontal(
            ship_size=5, ship_column=0, ship_row=0
        )
        self.assertEqual(ship_positions, {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)})

        ship_positions = self.game.get_ship_positions_horizontal(
            ship_size=5, ship_column=5, ship_row=5
        )
        self.assertEqual(ship_positions, {(5, 5), (5, 1), (5, 2), (5, 3), (5, 4)})

    def test_get_ship_positions_vertically(self):
        ship_positions = self.game.get_ship_positions_vertically(
            ship_size=5, ship_column=9, ship_row=9
        )
        self.assertEqual(ship_positions, {(9, 9), (8, 9), (7, 9), (6, 9), (5, 9)})

        ship_positions = self.game.get_ship_positions_vertically(
            ship_size=5, ship_column=0, ship_row=0
        )
        self.assertEqual(ship_positions, {(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)})

        ship_positions = self.game.get_ship_positions_vertically(
            ship_size=5, ship_column=5, ship_row=5
        )
        self.assertEqual(ship_positions, {(5, 5), (4, 5), (3, 5), (2, 5), (1, 5)})

    @patch("builtins.print", return_value=None)
    def test_start_game(self, mock_print):
        self.game.start_game_settings()

        with patch("builtins.input") as mock_input:
            s = list(self.game.ships_positions)
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
        self.assertEqual(self.game.validate_user_shot("D5"), False)
        self.assertEqual(self.game.validate_user_shot("5D"), False)
        self.assertEqual(self.game.validate_user_shot("5d"), False)
        self.assertEqual(self.game.validate_user_shot("d5"), False)
        self.assertEqual(self.game.validate_user_shot("D 5"), False)
        self.assertEqual(self.game.validate_user_shot("5 D"), False)
        self.assertEqual(self.game.validate_user_shot("5 - D"), False)
        self.assertEqual(self.game.validate_user_shot("5/D"), False)
        self.assertEqual(self.game.validate_user_shot("5--D"), False)
        self.assertEqual(self.game.validate_user_shot("-5D"), False)
        self.assertEqual(self.game.validate_user_shot("5D-"), False)
        self.assertEqual(self.game.validate_user_shot("5-J"), (9, 4))
        self.assertEqual(self.game.validate_user_shot("5-K"), False)
        self.assertEqual(self.game.validate_user_shot("-K"), False)
        self.assertEqual(self.game.validate_user_shot("3-"), False)

    def test_update_battlefield(self):
        with patch("builtins.print") as mock_print:
            mock_print.return_value = None
            self.game.start_game_settings()

        self.game.update_battlefield(hit=False, coordinates=(2, 2))
        self.assertEqual(self.game.battlefield[2][2], Fore.LIGHTBLUE_EX + "O")

        self.game.update_battlefield(hit=True, coordinates=(3, 2))
        self.assertEqual(self.game.battlefield[3][2], Fore.RED + "X")

    def test_print_boat_hit(self):
        with patch("builtins.print", return_value=None) as mock_print:
            self.game.start_game_settings()

            ship_position = tuple(self.game.ships["carrier"]["position"])[0]
            self.game.print_boat_hit(coordinates=ship_position)

            self.assertNotIn(ship_position, self.game.ships_positions)

    def test_check_user_won(self):
        self.assertEqual(self.game.check_user_won(), True)
        self.game.ships_positions.add((4, 5))
        self.assertEqual(self.game.check_user_won(), False)
