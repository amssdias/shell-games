import colorama
from colorama import Fore

from games import BattleShip, Hangman

colorama.init(autoreset=True)

class Controller:
    games = {
        "Hangman": Hangman,
        "Battleship": BattleShip,
    }

    def __init__(self, player):
        self.player = player

    def start(self):
        print(Fore.YELLOW + f"Hello {self.player.name}!")

        while True:
            print("Which game you would like to play?")
            game = self.get_game()
            if not game:
                continue
            
            print(Fore.RESET)
            self.player.update_games_played()
            user_result = game.play()

            self.display_result(user_result)

            user_answer = input("Would you like to retry? Type 'Y' to retry, or press any key to exit. ")
            if user_answer in ["Y", "y"]:
                continue
            else:
                print("Goodbye. :)")
                break

    def get_game(self):
        self.display_games()

        user_input = input(f"Write the name of the game: {Fore.LIGHTCYAN_EX}")

        validated = self.validate_user_game_choice(user_input)
        if validated:
            return self.games[validated]()
        return False

    def display_games(self):
        for game in self.games.keys():
            print(f"- {Fore.CYAN}{game}")

    def validate_user_game_choice(self, user_input: str):
        user_input_capitalized = user_input.capitalize()
        if user_input_capitalized not in self.games.keys():
            print(Fore.RED + "Game not found.")
            return False
        return user_input_capitalized

    def display_result(self, won: bool):
        if won:
            self.player.update_score()
            print(Fore.GREEN + "You Won!!! :D")
        else:
            print(Fore.RED + "You lost!!! :(")

