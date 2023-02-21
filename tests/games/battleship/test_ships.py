import unittest
from games.battleship.constants.ships_names import ShipsNames

from games.battleship.ships import Ships


class TestShips(unittest.TestCase):
    def setUp(self) -> None:
        self.ships = Ships()

    def test_init(self):
        ships_initial_variables = self.ships.__dict__.keys()
        self.assertIn("ships_positions", ships_initial_variables)
        self.assertIsInstance(self.ships.ships_positions, set)

        ships = self.ships.keys()

        for ship_name in ShipsNames:
            self.assertIn(ship_name.value, ships)

    def test_set_ships_positions(self):
        self.ships.set_ships_positions()

        self.assertTrue(self.ships.ships_positions)

        len_all_ships = 0
        for ship_values in self.ships.values():
            self.assertIn("position", ship_values)

            if ship_values.get("position"):
                len_all_ships += len(ship_values["position"])

    def test_get_ship_positions_horizontal(self):
        ship_positions = self.ships.get_ship_positions_horizontal(
            ship_size=5, ship_column=9, ship_row=9
        )
        self.assertEqual(ship_positions, {(9, 9), (9, 8), (9, 7), (9, 6), (9, 5)})

        ship_positions = self.ships.get_ship_positions_horizontal(
            ship_size=5, ship_column=0, ship_row=0
        )
        self.assertEqual(ship_positions, {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)})

        ship_positions = self.ships.get_ship_positions_horizontal(
            ship_size=5, ship_column=5, ship_row=5
        )
        self.assertEqual(ship_positions, {(5, 5), (5, 1), (5, 2), (5, 3), (5, 4)})

    def test_get_ship_positions_vertically(self):
        ship_positions = self.ships.get_ship_positions_vertically(
            ship_size=5, ship_column=9, ship_row=9
        )
        self.assertEqual(ship_positions, {(9, 9), (8, 9), (7, 9), (6, 9), (5, 9)})

        ship_positions = self.ships.get_ship_positions_vertically(
            ship_size=5, ship_column=0, ship_row=0
        )
        self.assertEqual(ship_positions, {(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)})

        ship_positions = self.ships.get_ship_positions_vertically(
            ship_size=5, ship_column=5, ship_row=5
        )
        self.assertEqual(ship_positions, {(5, 5), (4, 5), (3, 5), (2, 5), (1, 5)})
