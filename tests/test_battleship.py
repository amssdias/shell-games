import unittest
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
        self.assertEqual(self.game.user_points, 70)

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
        ship_positions = self.game.get_ship_positions_horizontal(ship_size=5, ship_column=9, ship_row=9)
        self.assertEqual(ship_positions, {(9, 9), (9, 8), (9, 7), (9, 6), (9, 5)})

        ship_positions = self.game.get_ship_positions_horizontal(ship_size=5, ship_column=0, ship_row=0)
        self.assertEqual(ship_positions, {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)})

        ship_positions = self.game.get_ship_positions_horizontal(ship_size=5, ship_column=5, ship_row=5)
        self.assertEqual(ship_positions, {(5, 5), (5, 1), (5, 2), (5, 3), (5, 4)})

    def test_get_ship_positions_vertically(self):
        ship_positions = self.game.get_ship_positions_vertically(ship_size=5, ship_column=9, ship_row=9)
        self.assertEqual(ship_positions, {(9, 9), (8, 9), (7, 9), (6, 9), (5, 9)})

        ship_positions = self.game.get_ship_positions_vertically(ship_size=5, ship_column=0, ship_row=0)
        self.assertEqual(ship_positions, {(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)})

        ship_positions = self.game.get_ship_positions_vertically(ship_size=5, ship_column=5, ship_row=5)
        self.assertEqual(ship_positions, {(5, 5), (4, 5), (3, 5), (2, 5), (1, 5)})

    @patch("games.battleship.battleship.print", return_value=None)
    def test_validate_user_shot(self, mocked_print):
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

    def test_update_battlefield(self):
        self.game.update_battlefield(hit=False, coordinates=(2, 2))
        self.assertEqual(self.game.battlefield[2][2], "O")

        self.game.update_battlefield(hit=True, coordinates=(3, 2))
        self.assertEqual(self.game.battlefield[3][2], "X")

    def _test_print_boat_hit(self):
        pass

    def _test_check_user_won(self):
        pass