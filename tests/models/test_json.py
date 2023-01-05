import json
from pathlib import Path

from models.files_models import JsonFile
from tests.models.utils.test_file_utils import TestFile


class TestJsonFile(TestFile):
    def setUp(self) -> None:
        super().setUp()
        self.file_directory = Path(Path.cwd(), "tests", "models", "db", "testing.json")
        self.db = JsonFile(file_path=self.file_directory)

    def test_initial_data(self):
        json_initial_variables = self.db.__dict__.keys()
        self.assertIn("file_path", json_initial_variables)
        self.assertIsInstance(self.db.file_path, Path)
        self.assertEqual(self.db.file_path, self.file_directory)

    def test_get_all_users(self):
        self.write_data_to_json()
        users = self.db.get_all_users()
        self.delete_data_from_json()

        self.assertCountEqual(users, [self.user_1, self.user_2])

    def test_get_user(self):
        self.write_data_to_json()
        user = self.db.get_user(self.user_1["email"])
        self.delete_data_from_json()

        self.assertEqual(user, self.user_1)

    def test_save_user(self):
        user = {
            "name": "new user",
            "age": "22",
            "email": "new-user@fake-email.com"
        }
        saved_user = self.db.save_user(user)
        self.assertTrue(saved_user)

        # Check a user was added to the testing file
        with open(self.file_directory, "r") as testing_file:
            data = json.load(testing_file)
            for line in data:
                if line["email"] == user["email"]:
                    self.assertEqual(line["email"], user["email"])
                    break
            else:
                assert False, "It did not saved a user to the file"
        
        self.delete_data_from_json()

    def test_update_user_games_played(self):
        self.write_data_to_json()
        self.db.update_user_games_played(self.user_1)

        user = self.db.get_user(self.user_1["email"])

        # We get an int because we loading json data
        self.assertEqual(user["games_played"], 1)
        self.delete_data_from_json()
