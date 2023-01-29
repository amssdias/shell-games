from typing import List, Tuple

from colorama import Fore

from games.abstracts.board import Board
from games.battleship.constants.ascii import ASCII_A_UNICODE


class BattleshipBoard(Board):
    def __init__(self, columns, rows) -> None:
        super().__init__(columns, rows)

    def build_board(self, columns, rows) -> List[List]:
        return [["." for _ in range(columns)] for _ in range(rows)]

    def display_board(self) -> None:
        self.print_battlefield_columns()
        self.print_battlefield_rows()
        return None

    def print_battlefield_columns(self) -> None:
        for column in range(len(self.positions) + 1):
            if column == 0:
                print(" ", end="  ")
                continue
            print(column, end="  ")
        print()
        return None

    def print_battlefield_rows(self) -> None:
        for index, row in enumerate(self.positions, ASCII_A_UNICODE):
            print(chr(index), end="  ")
            for dot in row:
                print(dot, end="  ")
            print()
        return None

    def mark_board_position(self, hit: bool, coordinates: Tuple) -> None:
        row, column = coordinates
        self.positions[row][column] = Fore.RED + "X" if hit else Fore.LIGHTBLUE_EX + "O"
        return None
