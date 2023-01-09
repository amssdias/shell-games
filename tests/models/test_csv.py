import csv
from pathlib import Path

from models.files_models import CSVFile
from tests.models.utils.test_file_utils import TestFile


class TestCSVFile(TestFile):
    def setUp(self) -> None:
        super().setUp()
        self.file_directory = Path(Path.cwd(), "tests", "models", "db", "testing.csv")
        self.db = CSVFile(file_path=self.file_directory)

    def test_initial_data(self):
        csv_initial_variables = self.db.__dict__.keys()

        self.assertIn("file_path", csv_initial_variables)
        self.assertIn("fieldnames", csv_initial_variables)
        self.assertIsInstance(self.db.file_path, Path)
        self.assertEqual(self.db.file_path, self.file_directory)

    def test_get_all_users(self):
        self.write_data_to_csv()
        users = self.db.get_all_users()
        self.delete_data_from_csv()

        self.assertCountEqual(users, [self.user_1, self.user_2])

    def test_get_user(self):
        self.write_data_to_csv()
        user = self.db.get_user(self.user_1["email"])
        self.delete_data_from_csv()

        self.assertEqual(user, self.user_1)

    def test_save_user(self):
        user = {
            "email": "new-user@fake-email.com",
            "age": "22",
            "password": "password",
        }
        saved_user = self.db.save_user(user)
        self.assertTrue(saved_user)

        # Check a user was added to the testing file
        with open(self.file_directory, "r") as testing_file:
            read_file = csv.DictReader(testing_file, delimiter=",")
            for line in read_file:
                if line["email"] == user["email"]:
                    self.assertEqual(line["email"], user["email"])
                    break
            else:
                assert False, "It did not saved a user to the file"
        
        self.delete_data_from_csv()

    def test_update_user_games_played(self):
        self.write_data_to_csv()
        self.db.update_user_games_played(self.user_1)

        user = self.db.get_user(self.user_1["email"])

        self.assertEqual(user["games_played"], "1")
        self.delete_data_from_csv()
    
    def test_update_user_score(self):
        self.write_data_to_csv()
        self.db.update_user_score(self.user_1)
        user = self.db.get_user(self.user_1["email"])

        self.assertEqual(user["score"], "1")
        self.delete_data_from_csv()
