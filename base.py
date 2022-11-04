from games.hangman import Hangman

games = {
    "hangman": Hangman,
}

game = Hangman()

while True:

    won = game.play()

    user_answer = input("Would you like to retry? (Y/N)")

    if user_answer in ["Y", "y"]:
        continue
    else:
        print("Goodbye. :)")
        break
