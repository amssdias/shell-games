class HangmanDraw:
    def display_draw(self):
        for _ in range(15):
            print("_", end="")
        print()

        for _ in range(4):
            self.print_base()

        self.display_draw_head()
        self.display_draw_body_arms()
        self.display_draw_legs()

        print("|")
        print("|" + "".rjust(19, "_"))

    def display_draw_head(self):
        if self.guesses < 6:
            print("|         ____|____")
            print("|        /         \\")
            print("|       /           \\")
            print("|      /             \\")
            print("|      |             |")
            print("|      |             |")
            print("|       \           /")
            print("|        \_________/")
        else:
            for _ in range(8):
                print("|")
    
    def display_draw_body_arms(self):
        if self.guesses < 1:

            self.print_base()

            print("|         \   |   /")
            print("|          \  |  /")
            print("|           \ | /")
            print("|            \|/")

            for _ in range(4):
                self.print_base()
        
        elif self.guesses < 2:
            print("|             |")
            print("|         \   |")
            print("|          \  |")
            print("|           \ |")
            print("|            \|")
            for _ in range(4):
                self.print_base()

        elif self.guesses < 5:
            
            # Print only the body
            for _ in range(9):
                self.print_base()
        else:
            for _ in range(9):
                print("|")

    def display_draw_legs(self):
        if self.guesses < 3:

            # Print both legs
            right_leg_spaces = 2
            for i in range(13, 9, -1):
                print("|" + "/".rjust(i) + "\\".rjust(right_leg_spaces))
                right_leg_spaces += 2

        elif self.guesses < 4:
            
            # Print one leg
            for i in range(13, 9, -1):
                print("|" + "/".rjust(i))
        
        else:
            for _ in range(4):
                print("|")

    def print_base(self):
        print("|" + "|".rjust(14))