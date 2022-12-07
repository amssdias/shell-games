from games import Hangman, BattleShip

games = {
    "Hangman": Hangman,
    "Battleship": BattleShip,
}

while True:

    print("Hello! Which game you would like to play?")

    for game in games.keys():
        print(f"1 - {game}")

    user_game = input("Write the name of the game: ")

    game = games[user_game.capitalize()]

    game().play()

    user_answer = input("Would you like to retry? (Y/N)")
    if user_answer in ["Y", "y"]:
        continue
    else:
        print("Goodbye. :)")
        break
