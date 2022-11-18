import random
import string

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
        self.user_points = 50
        self.battlefield = self.build_battlefield()

    def build_battlefield(self):
        """Build battlefield to print out."""
        battle_field = [["." for row in range(10)] for column in range(10)]
        return battle_field

    def start_game_settings(self):
        self.set_ships_positions()
        print("Instructions: You should call your move like: D-4/4-D.")

    def set_ships_positions(self):
        """Randomly create positions for each ship."""

        ships_positions = set()

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
                
                if ships_positions.isdisjoint(ship_positions):
                    break

            ships_positions.update(ship_positions)
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
        index_A = ord("A")
        for index, row in enumerate(self.battlefield, index_A):
            print(chr(index), end="  ")
            for dot in row:
                print(".", end="  ")
            print()

    def validate_user_shot(self, user_shot):
        coordinates = user_shot.split("-")
        if (
            len(coordinates) != 2
            or len(coordinates[0]) != 1
            or len(coordinates[1]) != 1
        ):
            print("Write your move like this: A-5 or 5-A")
            return False

        rows = string.ascii_uppercase[: len(self.battlefield)]
        if (coordinates[0] not in rows and coordinates[1] not in rows) or (
            not coordinates[0].isnumeric() and not coordinates[1].isnumeric()
        ):

            print(f"You should provide one row and one column (C-5).")
            return False

        # TODO: Change row coordinate (letter) to number of row

        return coordinates