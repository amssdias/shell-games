from games.battleship.constants import ASCII_A_UNICODE


class BattleShipDraw:
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
