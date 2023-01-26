import random
from typing import Set

from colorama import Fore
from games.abstracts.game import Game
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

    def __init__(self) -> None:
        self.word = None
        self.letters = set()
        self.guesses = 6

    def start_game_settings(self) -> None:
        difficulty = self.get_difficulty_level()
        self.word = self.get_random_word(difficulty)
        self.letters = self.get_letters()

    def get_difficulty_level(self) -> str:
        while True:
            difficulty = input(
                f"""Choose your level:
1 - {Fore.GREEN}Beginner{Fore.RESET}
2 - {Fore.BLUE}Medium{Fore.RESET}
3 - {Fore.RED}Hard{Fore.RESET}
Write your number: {Fore.YELLOW}"""
            )

            if difficulty in ["1", "2", "3"]:
                self.reset_color()
                break
            else:
                print(Fore.RED + "Choose a number correctly.")

        return difficulty

    def get_random_word(self, difficulty: str) -> str:
        return random.choice(self.game_difficulty.get(difficulty, self.random))

    def get_letters(self) -> Set:
        return set(random.choices(self.word))

    def start_game(self) -> bool:
        while True:
            self.display_game()

            letter = input("Choose a letter: " + Fore.GREEN)
            self.reset_color()
            self.letters.add(letter)

            if self.check_letter_on_word(letter):
                if self.check_user_won():
                    return True
                continue

            self.update_guesses()

            if self.guesses <= 0:
                self.display_draw()
                self.end_game_display_word()
                return False

    def display_game(self) -> None:
        self.display_draw()

        for letter in self.word:
            if letter in self.letters:
                print(Fore.MAGENTA + letter, end=" ")
            else:
                print("_", end=" ")
        print()

    def check_letter_on_word(self, letter: str) -> bool:
        if not isinstance(letter, str):
            raise TypeError("Argument must be of type str.")
        if letter in self.word:
            return True
        return False

    def check_user_won(self) -> bool:
        for letter in self.word:
            for used_letter in self.letters:
                if letter == used_letter:
                    break
            else:
                return False
        return True

    def update_guesses(self) -> None:
        self.guesses -= 1

    @staticmethod
    def reset_color() -> None:
        print(Fore.RESET)

    def end_game_display_word(self) -> None:
        print(f"The word was {Fore.BLUE}{self.word}.")
