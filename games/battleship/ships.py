import random
from typing import List, Set
from games.battleship.constants.ships_names import ShipsNames


class Ships(dict):

    def __init__(self):
        self.update({
            ShipsNames.CARRIER.value: {
                "size": 5,
            },
            ShipsNames.BATTLESHIP.value: {
                "size": 4,
            },
            ShipsNames.CRUISER.value: {
                "size": 3,
            },
            ShipsNames.SUBMARINE.value: {
                "size": 3,
            },
            ShipsNames.DESTROYER.value: {
                "size": 2,
            },
        })
        self.ships_positions = set()

    def set_ships_positions(self) -> None:
        """Randomly create positions for each ship."""

        for ship, value in self.items():

            # Loop to make sure ship positions aren't colliding
            while True:
                battlefield_ship_column_position = random.randint(0, 9)
                battlefield_ship_row_position = random.randint(0, 9)
                ship_direction_horizontal = random.choice([True, False])

                # Sets are quicker for search
                self[ship]["position"] = set()

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
            # self.all_ships.append(Ship())
            self[ship]["position"].update(ship_positions)

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
