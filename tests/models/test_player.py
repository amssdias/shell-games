from pathlib import Path
from threading import Thread
import unittest
from unittest.mock import patch

from models.abstract import DB
from models.file_model import CSVDB
from models.player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self) -> None:
        file_path = Path(Path.cwd(), "tests", "models", "db", "testing.csv")
        self.db = CSVDB(file_path=file_path)
        self.user = {
            "email": "testing@hotmail.com",
            "age": "23",
            "password": "password",
        }
        self.player = Player(self.db, **self.user)

    def test_initialize(self):
        player_initial_variables = self.player.__dict__.keys()
        self.assertIn("db", player_initial_variables)
        self.assertIn("email", player_initial_variables)
        self.assertIn("age", player_initial_variables)
        self.assertIn("password", player_initial_variables)

        self.assertIsInstance(self.player.db, DB)
        self.assertIsInstance(self.player.email, str)
        self.assertIsInstance(self.player.age, str)
        self.assertIsInstance(self.player.password, str)

        self.assertEqual(self.player.db, self.db)
        self.assertEqual(self.player.email, "testing@hotmail.com")
        self.assertEqual(self.player.age, "23")
        self.assertEqual(self.player.password, "password")

    def test_update_games_played(self):
        with patch("models.file_model.FileDB.update_user") as mocked_upate_user:
            mocked_upate_user.return_value = True
            thread_1 = Thread(target=self.player.update_games_played)
            thread_1.start()
            thread_1.join()

            self.assertFalse(thread_1.is_alive())
