import random

from games.game import Game

class BattleShip(Game):

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
        self.battlefield = self.build_battlefield()

    def build_battlefield(self):
        battle_field = [["." for row in range(10)] for column in range(10)]
        return battle_field

    def start_game_settings(self):
        self.set_ships_positions()

    def set_ships_positions(self):

        for ship, value in self.ships.items():
            battlefield_ship_column_position = random.randint(0, 9)
            battlefield_ship_row_position = random.randint(0, 9)
            ship_direction_horizontal = random.choice([True, False])

            # Sets are quicker for search
            self.ships[ship]["position"] = set()

            if ship_direction_horizontal:
                ship_positions = self.get_ship_positions_horizontal(
                    ship_size=value["size"], 
                    ship_column=battlefield_ship_column_position, 
                    ship_row=battlefield_ship_row_position
                )

            else:
                ship_positions = self.get_ship_positions_vertically(
                    ship_size=value["size"], 
                    ship_column=battlefield_ship_column_position, 
                    ship_row=battlefield_ship_row_position
                )

            self.ships[ship]["position"].update(ship_positions)

    def get_ship_positions_horizontal(self, ship_size, ship_column, ship_row):
        if ship_column + ship_size > 9:
            # Go towards back
            return {(ship_row, column) for column in range(ship_column, ship_column - ship_size, -1)}

        else:
            # Go towards front of row
            return {(ship_row, column) for column in range(ship_column, ship_column + ship_size)}

    def get_ship_positions_vertically(self, ship_size, ship_column, ship_row):
        if ship_row + ship_size > 9:
            # Go towards up
            return {(row, ship_column) for row in range(ship_row, ship_row - ship_size, -1)}
        else:
            # Go towards down
            return {(row, ship_column) for row in range(ship_row, ship_row + ship_size)}

    def start_game(self):
        pass
