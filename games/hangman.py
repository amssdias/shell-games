import random
from .game import Game



class Hangman(Game):
    easy_words = ["them", "four", "dog", "law"]
    medium_words = ["duplex", "jogging", "walkway", "buffalo", "funny"]
    hard_words = ["joyful", "bikini", "megahertz", "spritz", "lengths", "subway", "hyphen", "nightclub", "rhythm"]

    game_difficulty = {
        "1": easy_words,
        "2": medium_words,
        "3": hard_words
    }

    points = 6
    used_letters = []

    def play(self):
        word, letters = self.start_game_settings()

        # Display on user print of hangman wih letter word placed
        while True:
            self.display_game()
            
            letter = input("Choose a letter: ")

            self.process_game(letter)

            finish = self.check_points()

            if finish:
                print(f"You lose. The word was {word}.")
                break
            

            # Check if letter is on the word
            # If it's on the word, go back to step 4
            # If it's on word but already displayed, discount one point
            # If it's not on word, discount one point
            # If user points are over, finish game, and ask if want to start over.
            # Go back to step 4
        return 1

    def start_game_settings(self):
        difficulty = self.get_difficulty_level()
        self.word = self.get_random_word(difficulty)
        self.letters = self.get_letters()
        print(self.word, self.letters)
        return self.word, self.letters

    def get_difficulty_level(self):
        while True:
            difficulty = input("""Choose your level:
1 - Beginner
2 - Medium
3 - Hard
Write your number: """)

            if difficulty in ["1", "2", "3"]:
                break
            else:
                print("Choose a number.")

        return difficulty
    
    def get_random_word(self, difficulty: str):
        return random.choice(self.game_difficulty.get(difficulty, []))
    
    def get_letters(self):
        # TODO: Change this method to be more consive depending on the level of difficulty as well.
        if len(self.word) < 6:
            return random.choices(self.word)
        else:
            return random.choices(self.word)

    def display_game(self):
        for letter in self.word:
            if letter in self.letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")

    def process_game(self, letter):
        if letter in self.word:
            self.letters.append(letter)
        else:
            self.points -= 1

    def check_points(self):
        if self.points <= 0:
            return False