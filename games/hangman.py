import random
from .game import Game


class Hangman(Game):
    """
    Game to guess a word.
    """
    easy_words = ["them", "four", "dog", "law"]
    medium_words = ["duplex", "jogging", "walkway", "buffalo", "funny"]
    hard_words = ["joyful", "bikini", "megahertz", "spritz", "lengths", "subway", "hyphen", "nightclub", "rhythm"]

    game_difficulty = {
        "1": easy_words,
        "2": medium_words,
        "3": hard_words
    }

    guesses = 6

    def __init__(self):
        self.word = None
        self.letters = set()

    def start_game_settings(self):
        difficulty = self.get_difficulty_level()
        self.word = self.get_random_word(difficulty)
        self.letters = self.get_letters()

    @staticmethod
    def get_difficulty_level():
        while True:
            difficulty = input("""Choose your level:
1 - Beginner
2 - Medium
3 - Hard
Write your number: """)

            if difficulty in ["1", "2", "3"]:
                break
            else:
                print("Choose a number correctly.")

        return difficulty
    
    def get_random_word(self, difficulty: str):
        return random.choice(self.game_difficulty.get(difficulty, []))
    
    def get_letters(self):
        # TODO: Change this method to be more consive depending on the level of difficulty as well.
        if len(self.word) < 6:
            return random.choices(self.word)
        else:
            return random.choices(self.word)

    def start_game(self):
        while True:
            self.display_game()

            letter = input("Choose a letter: ")
            self.letters.add(letter)

            guessed = self.check_letter_on_word(letter)

            if guessed:
                won = self.check_user_won()
                if won:
                    print("You Won!!! :D")
                    return True
                continue

            self.update_guesses()

            if self.guesses <= 0:
                print("You lost!!! :(")
                print(f"The word was {self.word}.")
                return False

    def display_game(self):
        for letter in self.word:
            if letter in self.letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")

    def check_letter_on_word(self, letter):
        if letter in self.word:
            return True
        return False

    def check_user_won(self):
        for letter in self.word:

            # TODO: Use a binary search tree
            for used_letter in self.letters:
                if letter == used_letter:
                    break
            else:
                return False
        return True

    def update_guesses(self):
        self.guesses -= 1
