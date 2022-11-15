from games import Hangman, BattleShip

games = {
    "hangman": Hangman,
    "battleship": BattleShip,
}

game = Hangman()

while True:

    game.play()

    user_answer = input("Would you like to retry? (Y/N)")
    if user_answer in ["Y", "y"]:
        continue
    else:
        print("Goodbye. :)")
        break
