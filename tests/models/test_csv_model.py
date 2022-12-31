import csv
import os

from models.files_models import CSVFile
from tests.models.utils.test_file_utils import TestFile


class TestCSVFile(TestFile):
    def setUp(self) -> None:
        super().setUp()
        self.file_directory = os.getcwd() + "/tests/models/csv/testing.csv"
        self.db = CSVFile()

    def test_get_content(self):
        self.write_data_to_csv()

        opened_file = open(self.file_directory, "r")
        data = self.db.get_content(opened_file)
        opened_file.close()
        self.delete_data_from_csv()

        self.assertCountEqual(data, [self.user_1, self.user_2])

    def test_write_to_file(self):
        user = {
            "name": "new user",
            "age": "22",
            "email": "new-user@fake-email.com"
        }
        saved_user = self.db.write_to_file(user, data=[], file_path=self.file_directory)
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
