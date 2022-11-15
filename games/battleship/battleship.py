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


    def start_game_settings(self):
        self.build_ships()

    def build_ships(self):

        for ship, value in self.ships.items():
            battlefield_ship_column_position = random.randint(0, 9)
            battlefield_ship_row_position = random.randint(0, 9)
            ship_direction_horizontal = random.choice([True, False])

            if ship_direction_horizontal:
                if battlefield_ship_row_position + value["size"] > 9:
                    # Go towards back
                    pass
                else:
                    # Go towards front of row
                    pass

            else:
                if battlefield_ship_column_position + value["size"] > 9:
                    # Go towards up
                    pass
                else:
                    # Go towards down
                    pass

    def build_battlefield(self):
        battle_field = [["." for row in range(10)] for column in range(10)]
        return battle_field

    def start_game(self):
        pass
