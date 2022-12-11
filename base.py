import colorama
from colorama import Fore
from games import Hangman, BattleShip

colorama.init(autoreset=True)

games = {
    "Hangman": Hangman,
    "Battleship": BattleShip,
}

while True:

    print("Hello! Which game you would like to play?")

    for game in games.keys():
        print(f"- {Fore.CYAN}{game}")

    user_game = input(f"Write the name of the game: {Fore.LIGHTCYAN_EX}")
    print(Fore.RESET)

    game = games[user_game.capitalize()]

    game().play()

    user_answer = input("Would you like to retry? (Y/N)")
    if user_answer in ["Y", "y"]:
        continue
    else:
        print("Goodbye. :)")
        break
