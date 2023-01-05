import json
from pathlib import Path

from models.files_models import JsonFile
from tests.models.utils.test_file_utils import TestFile


class TestJsonFile(TestFile):
    def setUp(self) -> None:
        super().setUp()
        self.file_directory = Path(Path.cwd(), "tests", "models", "json", "testing.json")
        self.db = JsonFile(file_path=self.file_directory)

    def test_get_content(self):
        self.write_data_to_json()
        users = self.db.get_all_users()
        self.delete_data_from_json()

        self.assertCountEqual(users, [self.user_1, self.user_2])

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

    def _test_get_user(self):
        pass

    def _test_update_user_games_played(self):
        pass