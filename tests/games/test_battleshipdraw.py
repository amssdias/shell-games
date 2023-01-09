import unittest
from unittest.mock import MagicMock, patch

from games.battleship.battleshipdraw import BattleShipDraw


class TestBattleshipDraw(unittest.TestCase):
    def setUp(self) -> None:
        self.game_draw = BattleShipDraw()

    @patch("games.battleship.battleshipdraw.print")
    def test_print_battlefield(self, mock_print):
        self.game_draw.print_battlefield_columns = MagicMock()
        self.game_draw.print_battlefield_rows = MagicMock()

        self.game_draw.print_battlefield()

        self.game_draw.print_battlefield_columns.assert_called_once()
        self.game_draw.print_battlefield_rows.assert_called_once()
