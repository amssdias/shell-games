from threading import Thread
import unittest
from unittest.mock import patch

from models import DB, CSVDB, Player
from tests.models.utils.testing_db import TestDBCSV


class TestPlayer(unittest.TestCase):

    def setUp(self) -> None:
        self.db = TestDBCSV()
        self.user = {
            "email": "testing@hotmail.com",
            "age": "23",
            "password": "password",
        }
        self.player = Player(self.db)

    def test_initialize(self):
        player_initial_variables = self.player.__dict__.keys()
        self.assertIn("db", player_initial_variables)
        self.assertIn("email", player_initial_variables)
        self.assertIn("age", player_initial_variables)
        self.assertIn("password", player_initial_variables)

        self.assertIsInstance(self.player.db, DB)

        self.assertEqual(self.player.db, self.db)
        self.assertEqual(self.player.email, None)
        self.assertEqual(self.player.age, None)
        self.assertEqual(self.player.password, None)

    def test_register_player(self):
        pass 

    def test_update_games_played(self):
        self.player.register_player(**self.user)
        with patch("models.file_model.FileDB.update_user") as mocked_upate_player:
            mocked_upate_player.return_value = True
            thread_1 = Thread(target=self.player.update_games_played)
            thread_1.start()
            thread_1.join()

            self.assertFalse(thread_1.is_alive())
