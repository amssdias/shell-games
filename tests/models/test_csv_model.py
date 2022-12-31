import csv
import os
import unittest

from models.abstract import DB
from models.files_models import CSVFile


class TestCSVFile(unittest.TestCase):
    def setUp(self) -> None:
        self.db = CSVFile()
        self.file_directory = os.getcwd() + "/tests/models/csv/testing.csv"
        self.user_1 = {
            "name": "testing",
            "age": "20",
            "email": "testing@bogusemail.com"
        }
        self.user_2 = {
            "name": "Mary",
            "age": "23",
            "email": "maryjacobs@bogusemail.com"
        }

    def test_get_content(self):
        self.__write_data_to_csv()

        opened_file = open(self.file_directory, "r")
        data = self.db.get_content(opened_file)
        opened_file.close()
        self.__delete_data_from_csv()

        self.assertEqual(data, [self.user_1, self.user_2])

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
        
        self.__delete_data_from_csv()
        
    def __write_data_to_csv(self):
        with open(self.file_directory, "a", newline="") as write_file:
            writer = csv.DictWriter(write_file, fieldnames=["name", "age", "email"], delimiter=",")
            writer.writerows([self.user_1, self.user_2])
    
    def __delete_data_from_csv(self):
        with open(self.file_directory, "w", newline="") as write_file:
            writer = csv.DictWriter(write_file, fieldnames=["name", "age", "email"], delimiter=",")
            writer.writeheader()