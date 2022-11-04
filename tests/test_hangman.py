import unittest

from games.hangman import Hangman


class TestHangman(unittest.TestCase):

    def setUp(self) -> None:
        self.game = Hangman()

    def test_hangman_initial(self):
        self.assertEqual(self.game.letters, set())
        self.assertEqual(self.game.guesses, 6)
        self.assertEqual(self.game.word, None)

    def test_hangman_get_random_word(self):
        self.assertIn(self.game.get_random_word("1"), self.game.easy_words)
        self.assertIn(self.game.get_random_word("2"), self.game.medium_words)
        self.assertIn(self.game.get_random_word("3"), self.game.hard_words)

        self.assertIn(self.game.get_random_word("ad"), self.game.random)
        self.assertIn(self.game.get_random_word(0), self.game.random)
        self.assertIn(self.game.get_random_word(2.5), self.game.random)
        self.assertIn(self.game.get_random_word(True), self.game.random)

    def test_hangman_get_difficulty_level(self):
        pass

    def test_hangman_get_letters(self):
        pass

    def test_hangman_game_settings(self):
        pass
