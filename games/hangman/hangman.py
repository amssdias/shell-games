import random

from games.game import Game
from games.hangman.hangmandraw import HangmanDraw


class Hangman(Game, HangmanDraw):
    """
    Game to guess a word.
    """

    easy_words = ["them", "four", "dog", "law"]
    medium_words = ["duplex", "jogging", "walkway", "buffalo", "funny"]
    hard_words = [
        "joyful",
        "bikini",
        "megahertz",
        "spritz",
        "lengths",
        "subway",
        "hyphen",
        "nightclub",
        "rhythm",
    ]
    random = ["four", "dog", "bikini", "megahertz", "jogging"]

    game_difficulty = {"1": easy_words, "2": medium_words, "3": hard_words}

    def __init__(self):
        self.word = None
        self.letters = set()
        self.guesses = 6

    def start_game_settings(self):
        difficulty = self.get_difficulty_level()
        self.word = self.get_random_word(difficulty)
        self.letters = self.get_letters()

    @staticmethod
    def get_difficulty_level() -> str:
        while True:
            difficulty = input(
                """Choose your level:
1 - Beginner
2 - Medium
3 - Hard
Write your number: """
            )

            if difficulty in ["1", "2", "3"]:
                break
            else:
                print("Choose a number correctly.")

        return difficulty

    def get_random_word(self, difficulty: str) -> str:
        return random.choice(self.game_difficulty.get(difficulty, self.random))

    def get_letters(self) -> set():
        return set(random.choices(self.word))

    def start_game(self) -> bool:
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
                self.display_draw()
                print("You lost!!! :(")
                print(f"The word was {self.word}.")
                return False

    def display_game(self):
        self.display_draw()

        for letter in self.word:
            if letter in self.letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")

    def check_letter_on_word(self, letter: str):
        if not isinstance(letter, str):
            raise TypeError("Argument must be of type str.")
        if letter in self.word:
            return True
        return False

    def check_user_won(self):
        for letter in self.word:
            for used_letter in self.letters:
                if letter == used_letter:
                    break
            else:
                return False
        return True

    def update_guesses(self):
        self.guesses -= 1