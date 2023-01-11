import unittest
from unittest.mock import patch

from games.hangman.hangman import Hangman


class TestHangman(unittest.TestCase):
    def setUp(self) -> None:
        self.game = Hangman()

    def test_hangman_initial(self):
        self.assertEqual(self.game.letters, set())
        self.assertEqual(self.game.guesses, 6)
        self.assertEqual(self.game.word, None)
        self.assertEqual(self.game.easy_words, ["them", "four", "dog", "law"])
        self.assertEqual(
            self.game.medium_words, ["duplex", "jogging", "walkway", "buffalo", "funny"]
        )
        self.assertEqual(
            self.game.hard_words,
            [
                "joyful",
                "bikini",
                "megahertz",
                "spritz",
                "lengths",
                "subway",
                "hyphen",
                "nightclub",
                "rhythm",
            ],
        )

    def test_hangman_get_random_word(self):
        self.assertIn(self.game.get_random_word("1"), self.game.easy_words)
        self.assertIn(self.game.get_random_word("2"), self.game.medium_words)
        self.assertIn(self.game.get_random_word("3"), self.game.hard_words)

        self.assertIn(self.game.get_random_word("ad"), self.game.random)
        self.assertIn(self.game.get_random_word(0), self.game.random)
        self.assertIn(self.game.get_random_word(2.5), self.game.random)
        self.assertIn(self.game.get_random_word(True), self.game.random)
        self.assertIsInstance(self.game.get_random_word("as"), str)

    @patch("builtins.print", return_value=None)
    @patch("builtins.input", side_effect=["5", "2"])
    def test_hangman_get_difficulty_level(self, mock_input, mock_print):
        self.assertEqual(self.game.get_difficulty_level(), "2")

    def test_hangman_get_letters(self):
        word = "animal"
        self.game.word = word
        self.assertIn("".join(self.game.get_letters()), word)

    def test_hangman_game_settings(self):

        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["1", "2", "3"]
            
            self.game.start_game_settings()
            self.assertIn(self.game.word, self.game.easy_words)
            self.assertIn("".join(self.game.letters), self.game.word)

            self.game.start_game_settings()
            self.assertIn(self.game.word, self.game.medium_words)
            self.assertIn("".join(self.game.letters), self.game.word)

            self.game.start_game_settings()
            self.assertIn(self.game.word, self.game.hard_words)
            self.assertIn("".join(self.game.letters), self.game.word)

    @patch("builtins.print", return_value=None)
    def test_display_game(self, mock_print):
        self.game.word = "animal"
        self.game.letters.add("a")

        with patch("builtins.input") as mock_input:

            mock_input.side_effect = ["t", "n", "i", "m", "l"]
            self.assertTrue(self.game.start_game())
            self.assertEqual(self.game.guesses, 5)

            self.game.guesses = 6
            self.game.letters = set("a")
            mock_input.side_effect = ["t", "g", "l", "u", "z", "h", "r", "e"]
            self.assertFalse(self.game.start_game())
            self.assertEqual(self.game.guesses, 0)

    def test_check_letter_on_word(self):
        self.game.word = "animal"

        self.assertEqual(self.game.check_letter_on_word("a"), True)
        self.assertEqual(self.game.check_letter_on_word("A"), False)
        self.assertEqual(self.game.check_letter_on_word("b"), False)

        with self.assertRaises(TypeError) as err:
            self.game.check_letter_on_word(12)

    def test_check_user_won(self):
        self.game.word = "animal"
        self.game.letters = {"a", "f", "d", "e"}

        self.assertFalse(self.game.check_user_won())

        self.game.letters = {"a", "f", "d", "e", "n", "i", "m", "a", "l"}
        self.assertTrue(self.game.check_user_won())

    def test_update_guesses(self):
        self.game.update_guesses()
        self.assertEqual(self.game.guesses, 5)
        
        self.game.update_guesses()
        self.assertEqual(self.game.guesses, 4)
