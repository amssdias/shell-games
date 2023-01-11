import csv
from pathlib import Path
from unittest.mock import MagicMock

from models.abstracts.db import DB
from models.constants.database_actions import DatabaseActions
from models.file_model import FileDB
from models.files_models import CSVFile
from tests.models.utils.test_file_utils import TestFile


class TestFileModel(TestFile):
    def setUp(self) -> None:
        super().setUp()
        self.file_directory = Path(Path.cwd(), "tests", "models", "db", "testing.csv")
        self.db = FileDB(file_type=CSVFile(file_path=self.file_directory))

    def test_initial_values(self):
        db_initial_variables = self.db.__dict__.keys()
        self.assertIn("db", db_initial_variables)

    def test_initial_values_instance(self):
        self.assertIsInstance(self.db, DB)

    def test_create_user(self):
        self.db.user_exists = MagicMock(return_value=False)
        self.db.db.save_user = MagicMock(return_value=None)
        user = {
            "email": "new-user@fake-email.com",
            "age": 22,
            "password": "password",
        }
        new_user = self.db.create_user(**user)

        self.assertTrue(new_user)
        self.db.db.save_user.assert_called_once()
        self.db.user_exists.assert_called_once()

    def test_create_user_return_value(self):
        self.db.user_exists = MagicMock(return_value=False)
        self.db.db.save_user = MagicMock(return_value=None)
        user = {
            "email": "new-user@fake-email.com",
            "age": 22,
            "password": "password",
        }
        new_user = self.db.create_user(**user)


        self.assertEqual(new_user["email"], user["email"])
        self.assertEqual(new_user["age"], user["age"])
        self.assertEqual(new_user["password"], user["password"])

    def test_create_existing_user(self):
        self.db.user_exists = MagicMock(return_value=True)
        self.db.db.get_user = MagicMock(return_value=True)
        user = self.user_1.copy()
        del user["score"]
        del user["games_played"]
        new_user = self.db.create_user(**user)

        self.assertTrue(new_user)

    def test_user_exists(self):
        self.db.db.get_all_users = MagicMock(return_value=self.users)

        self.assertTrue(self.db.user_exists(self.user_1["email"]))
        self.assertTrue(self.db.user_exists(self.user_2["email"]))
        self.assertFalse(self.db.user_exists("nouser@bogusemail.com"))

    def test_user_exists_false(self):
        self.db.db.get_all_users = MagicMock(return_value=[])

        self.assertFalse(self.db.user_exists("nouser@testing.com"))

    def test_update_user_games_played(self):
        self.db.db.update_user_games_played = MagicMock()
        self.db.update_user(self.user_1, DatabaseActions.GAMES_PLAYED)
        
        self.db.db.update_user_games_played.assert_called_once()

    def test_update_user_score(self):
        self.db.db.update_user_score = MagicMock()
        self.db.update_user(self.user_1, DatabaseActions.SCORE)
        
        self.db.db.update_user_score.assert_called_once()
