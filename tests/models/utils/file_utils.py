import unittest


class TestFileUtils(unittest.TestCase):
    def setUp(self) -> None:
        self.user_1 = {
            "email": "testing@bogusemail.com",
            "age": 20,
            "password": "password",
            "score": 0,
            "games_played": 0,
        }
        self.user_2 = {
            "email": "maryjacobs@bogusemail.com",
            "age": 23,
            "password": "password",
            "score": 0,
            "games_played": 0,
        }

        self.headers = ["email", "age", "password", "score", "games_played"]

        self.users = [self.user_1, self.user_2]
