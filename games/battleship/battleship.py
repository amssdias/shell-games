import random
import string

from colorama import Fore
from games.battleship.constants import ASCII_A_UNICODE

from games.game import Game


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
        self.battlefield = []

    def build_battlefield(self):
        """Build battlefield to print out."""
        battle_field = [["." for _ in range(10)] for _ in range(10)]
        return battle_field

    def start_game_settings(self):
        self.user_points = 70
        self.set_ships_positions()
        self.battlefield = self.build_battlefield()
        print("Instructions: You should call your move like: D-4/4-D.")

    def set_ships_positions(self):
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

    def get_ship_positions_horizontal(self, ship_size, ship_column, ship_row):
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

    def get_ship_positions_vertically(self, ship_size, ship_column, ship_row):
        if ship_row + ship_size > 9:
            # Go towards up
            return {
                (row, ship_column) for row in range(ship_row, ship_row - ship_size, -1)
            }
        else:
            # Go towards down
            return {(row, ship_column) for row in range(ship_row, ship_row + ship_size)}

    def start_game(self):

        while True:
            self.print_battlefield()
            user_shot = input("Your call: ")

            coordinates_validated = self.validate_user_shot(user_shot)
            if not coordinates_validated:
                continue

            # If user don't hit a ship
            if {coordinates_validated}.isdisjoint(self.ships_positions):
                print(Fore.BLUE + "Miss!")
                self.user_points -= 1
                self.update_battlefield(hit=False, coordinates=coordinates_validated)

            else:
                self.print_boat_hit(coordinates_validated)
                won = self.check_user_won()
                if won:
                    return True

                self.update_battlefield(hit=True, coordinates=coordinates_validated)

            if not self.user_points:
                print("Sorry you lost. Ships sinking...")
                return False

    def print_battlefield(self):
        self.print_battlefield_columns()
        print()
        self.print_battlefield_rows()

    def print_battlefield_columns(self):
        for column in range(len(self.battlefield) + 1):
            if column == 0:
                print(" ", end="  ")
                continue
            print(column, end="  ")

    def print_battlefield_rows(self):
        for index, row in enumerate(self.battlefield, ASCII_A_UNICODE):
            print(chr(index), end="  ")
            for dot in row:
                print(dot, end="  ")
            print()

    def validate_user_shot(self, user_shot: str) -> tuple:
        """Validate a user should write only: a letter followed by a '-' and a number. (D-5)"""
        coordinates = user_shot.split("-")
        if len(coordinates) != 2 or len(coordinates[0]) > 2 or len(coordinates[1]) > 2:
            print("Write your move like this: A-5 or 5-A")
            return False

        rows = string.ascii_uppercase[: len(self.battlefield)]
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

    def update_battlefield(self, hit: bool, coordinates: tuple):
        row, column = coordinates
        self.battlefield[row][column] = (
            Fore.RED + "X" if hit else Fore.LIGHTBLUE_EX + "O"
        )

    def print_boat_hit(self, coordinates: tuple):
        for ship_name, ship_info in self.ships.items():
            if not {coordinates}.isdisjoint(ship_info["position"]):
                self.ships_positions.remove(coordinates)
                print(f"Hit! {Fore.RED + ship_name.capitalize()}.")
                break

    def check_user_won(self):
        if not self.ships_positions:
            return True
        return False
