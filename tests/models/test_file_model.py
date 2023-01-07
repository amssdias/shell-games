import csv
from pathlib import Path
from unittest.mock import patch

from models.abstract import DB
from models.constants.database_actions import DatabaseActions
from models.file_model import FileDB
from models.files_models import CSVFile
from tests.models.utils.test_file_utils import TestFile


class TestFileModel(TestFile):
    def setUp(self) -> None:
        super().setUp()
        self.file_directory = Path(Path.cwd(), "tests", "models", "db", "testing.csv")
        self.db = FileDB(file_type=CSVFile(file_path=self.file_directory))

    def test_inheritance(self):
        self.assertIsInstance(self.db, DB)
        self.assertIsInstance(self.db.db, CSVFile)

    def test_initial_values(self):
        db_initial_variables = self.db.__dict__.keys()
        self.assertIn("db", db_initial_variables)

    def test_create_user(self):
        user = {
            "email": "new-user@fake-email.com",
            "age": "22",
            "password": "password",
        }
        new_user = self.db.create_user(**user)
        self.assertTrue(new_user)

        # Check user was added to file
        with open(self.file_directory, "r") as testing_file:
            read_file = csv.DictReader(testing_file, delimiter=",")
            for line in read_file:
                if line["email"] == user["email"]:
                    self.assertEqual(line["email"], user["email"])
                    break
            else:
                assert False, "User was not saved to the file"

        self.delete_data_from_csv()

    def test_create_existing_user(self):
        self.write_data_to_csv()
        user = {
            "email": self.user_1["email"],
            "age": self.user_1["age"],
            "password": self.user_1["password"]
        }
        with patch("models.file_model.print") as mocked_print:
            new_user = self.db.create_user(**user)
        
        self.assertEqual(new_user, self.user_1)
        self.delete_data_from_csv()

    def test_user_exists(self):
        self.write_data_to_csv()

        self.assertTrue(self.db.user_exists(self.user_1["email"]))
        self.assertTrue(self.db.user_exists(self.user_2["email"]))
        self.assertFalse(self.db.user_exists("nouser@bogusemail.com"))

        self.delete_data_from_csv()

    def test_update_user_games_played(self):
        user = self.db.update_user(self.user_1, DatabaseActions.GAMES_PLAYED)
        self.user_1["games_played"] = "1"
        self.assertEqual(user, self.user_1)

