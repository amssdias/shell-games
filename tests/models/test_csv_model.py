import csv
from pathlib import Path

from models.files_models import CSVFile
from tests.models.utils.test_file_utils import TestFile


class TestCSVFile(TestFile):
    def setUp(self) -> None:
        super().setUp()
        self.file_directory = Path(Path.cwd(), "tests", "models", "csv", "testing.csv")
        self.db = CSVFile(file_path=self.file_directory)

    def test_get_content(self):
        self.write_data_to_csv()
        users = self.db.get_all_users()
        self.delete_data_from_csv()

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
            read_file = csv.DictReader(testing_file, delimiter=",")
            for line in read_file:
                if line["email"] == user["email"]:
                    self.assertEqual(line["email"], user["email"])
                    break
            else:
                assert False, "It did not saved a user to the file"
        
        self.delete_data_from_csv()

    def _test_get_user(self):
        pass

    def _test_update_user_games_played(self):
        pass