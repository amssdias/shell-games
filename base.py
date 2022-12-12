import colorama
from colorama import Fore
from games import Hangman, BattleShip, Game

colorama.init(autoreset=True)


class Controller:
    games = {
        "Hangman": Hangman,
        "Battleship": BattleShip,
    }

    def start(self):
        print(Fore.YELLOW + "Hello!")

        while True:
            print("Which game you would like to play?")
            game = self.get_game()
            if not game:
                continue
            
            print(Fore.RESET)
            user_result = game.play()

            self.display_result(user_result)

            user_answer = input("Would you like to retry? Type 'Y' to retry, or press any key to exit. ")
            if user_answer in ["Y", "y"]:
                continue
            else:
                print("Goodbye. :)")
                break

    def get_game(self):
        for game in self.games.keys():
            print(f"- {Fore.CYAN}{game}")

        user_input = input(f"Write the name of the game: {Fore.LIGHTCYAN_EX}")

        validated = self.validate_game(user_input)
        if validated:
            return self.games[validated]()
        return False

    def validate_game(self, user_input: str):
        user_input_capitalized = user_input.capitalize()
        if user_input_capitalized not in self.games.keys():
            print(Fore.RED + "Game not found.")
            return False
        return user_input_capitalized

    def display_result(self, won: bool):
        if won:
            print(Fore.GREEN + "You Won!!! :D")
        else:
            print(Fore.RED + "You lost!!! :(")


c = Controller()
c.start()
