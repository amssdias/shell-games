import random
import string
from typing import List, Set

from colorama import Fore
from games.battleship.battleship_board import BattleshipBoard
from games.battleship.constants import ASCII_A_UNICODE

from games.abstracts.game import Game


class BattleShip(Game):
    """
    Battleship game, try to call your shot and hit a ship!
    """

    def __init__(self):
        self.ships = {
            "carrier": {
                "size": 5,
            },
            "battleship": {
                "size": 4,
            },
            "cruiser": {
                "size": 3,
            },
            "submarine": {
                "size": 3,
            },
            "destroyer": {
                "size": 2,
            },
        }
        self.ships_positions = set()
        self.user_points = 0
        self.board = BattleshipBoard(10, 10)

    def __repr__(self):
        return f"{self.__class__.__name__}()"

    def start_game_settings(self) -> None:
        self.user_points = 70
        self.set_ships_positions()
        print(Fore.YELLOW + "Instructions: You should call your move like: D-4/4-D.")

    def set_ships_positions(self) -> None:
        """Randomly create positions for each ship."""

        for ship, value in self.ships.items():

            # Loop to make sure ship positions aren't colliding
            while True:
                battlefield_ship_column_position = random.randint(0, 9)
                battlefield_ship_row_position = random.randint(0, 9)
                ship_direction_horizontal = random.choice([True, False])

                # Sets are quicker for search
                self.ships[ship]["position"] = set()

                if ship_direction_horizontal:
                    ship_positions = self.get_ship_positions_horizontal(
                        ship_size=value["size"],
                        ship_column=battlefield_ship_column_position,
                        ship_row=battlefield_ship_row_position,
                    )

                else:
                    ship_positions = self.get_ship_positions_vertically(
                        ship_size=value["size"],
                        ship_column=battlefield_ship_column_position,
                        ship_row=battlefield_ship_row_position,
                    )

                if self.ships_positions.isdisjoint(ship_positions):
                    break

            self.ships_positions.update(ship_positions)
            self.ships[ship]["position"].update(ship_positions)

    def get_ship_positions_horizontal(self, ship_size, ship_column, ship_row) -> Set:
        if ship_column + ship_size > 9:
            # Go towards back of row
            return {
                (ship_row, column)
                for column in range(ship_column, ship_column - ship_size, -1)
            }

        else:
            # Go towards front of row
            return {
                (ship_row, column)
                for column in range(ship_column, ship_column + ship_size)
            }

    def get_ship_positions_vertically(self, ship_size, ship_column, ship_row) -> Set:
        if ship_row + ship_size > 9:
            # Go towards up
            return {
                (row, ship_column) for row in range(ship_row, ship_row - ship_size, -1)
            }
        else:
            # Go towards down
            return {(row, ship_column) for row in range(ship_row, ship_row + ship_size)}

    def start_game(self) -> bool:

        while True:
            self.board.display_board()
            user_shot = input("Your call: ")

            coordinates_validated = self.validate_user_shot(user_shot)
            if not coordinates_validated:
                continue

            # If user don't hit a ship
            if {coordinates_validated}.isdisjoint(self.ships_positions):
                hit = False
                print(Fore.BLUE + "Miss!")
                self.user_points -= 1

            else:
                hit = True
                self.print_boat_hit(coordinates_validated)
                won = self.check_user_won()
                if won:
                    return True

            self.board.mark_board_position(hit=hit, coordinates=coordinates_validated)

            if not self.user_points:
                print("Ships sinking...")
                return False

    def validate_user_shot(self, user_shot: str) -> tuple:
        """Validate a user should write only: a letter followed by a '-' and a number. (D-5)"""
        coordinates = [c for c in user_shot.split("-") if c]
        if len(coordinates) != 2 or len(coordinates[0]) > 2 or len(coordinates[1]) > 2:
            print("Write your move like this: A-5 or 5-A")
            return False

        rows = string.ascii_uppercase[: len(self.board.positions)]
        if (coordinates[0] not in rows and coordinates[1] not in rows) or (
            not coordinates[0].isnumeric() and not coordinates[1].isnumeric()
        ):

            print(f"You should provide one row and one column (C-5).")
            return False

        if coordinates[0] in rows:
            row = ord(coordinates[0]) - ASCII_A_UNICODE
            column = int(coordinates[1]) - 1  # User will not write D-0, but D-1
        else:
            row = ord(coordinates[1]) - ASCII_A_UNICODE
            column = int(coordinates[0]) - 1  # User will not write D-0, but D-1

        return (row, column)

    def print_boat_hit(self, coordinates: tuple):
        for ship_name, ship_info in self.ships.items():
            if not {coordinates}.isdisjoint(ship_info["position"]):
                self.ships_positions.remove(coordinates)
                print(f"Hit! {Fore.RED + ship_name.capitalize()}.")
                break

    def check_user_won(self) -> bool:
        if not self.ships_positions:
            return True
        return False
