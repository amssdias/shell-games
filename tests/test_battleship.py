import unittest
from unittest.mock import patch

from games.battleship import BattleShip


class TestBattleship(unittest.TestCase):
    def setUp(self) -> None:
        self.game = BattleShip()

    def test_battleship_initial(self):
        self.assertIsInstance(self.game.ships, dict)
        self.assertIsInstance(self.game.battlefield, list)
        self.assertEqual(self.game.user_points, 50)

        ships = self.game.ships.keys()
        self.assertIn("carrier", ships)
        self.assertIn("battleship", ships)
        self.assertIn("cruiser", ships)
        self.assertIn("submarine", ships)
        self.assertIn("destroyer", ships)

