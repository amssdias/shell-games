import csv
import os
import unittest
from unittest.mock import patch
from models.abstract import DB

from models.csv_model import CSVDB


class TestCSVDB(unittest.TestCase):
    def setUp(self) -> None:
        self.db = CSVDB()
        self.file_directory = os.getcwd() + "/tests/models/csv/testing.csv"

    def test_inheritance(self):
        self.assertIsInstance(self.db, DB)

    def test_save_user(self):
        user = {
            "name": "new user",
            "age": "22",
            "email": "new-user@fake-email.com"
        }
        new_user = self.db.save_user(**user, file_path=self.file_directory)
        self.assertEqual(new_user, user)

    def test_save_user_existing_user(self):
        self.__write_data_to_csv()
        existing_user = {
            "name": "testing",
            "age": "20",
            "email": "testing@bogusemail.com"
        }

        with patch("models.csv_model.print") as mocked_print:
            new_user = self.db.save_user(**existing_user, file_path=self.file_directory)
            self.assertEqual(new_user, self.db)
        
        self.__delete_data_from_csv()

    def test_read_file(self):
        output_file, output_file_reader = self.db.read_file(self.file_directory)
        self.assertIsInstance(output_file_reader, csv.DictReader)
        output_file.close()

    def test_user_exists(self):
        self.__write_data_to_csv()

        with open(self.file_directory, "r") as new_file:
            file_reader = csv.DictReader(new_file, delimiter=",")

            self.assertTrue(self.db.user_exists("testing@bogusemail.com", file_reader))
            new_file.seek(0)

            self.assertTrue(self.db.user_exists("maryjacobs@bogusemail.com", file_reader))
            new_file.seek(0)

            self.assertFalse(self.db.user_exists("nouser@bogusemail.com", file_reader))

        self.__delete_data_from_csv()

    def test_save_user_to_file(self):
        user = {
            "name": "new user",
            "age": "22",
            "email": "new-user@fake-email.com"
        }
        saved_user = self.db.save_user_to_file(**user, file_path=self.file_directory)
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

    def test_close_file(self):
        new_file = open(self.file_directory, "r")
        self.assertFalse(new_file.closed)

        self.db.close_file(new_file)
        self.assertTrue(new_file.closed)
        
    def __write_data_to_csv(self):
        with open(self.file_directory, "a", newline="") as write_file:
            writer = csv.DictWriter(write_file, fieldnames=["name", "age", "email"], delimiter=",")
            writer.writerows([
                {
                    "name": "testing",
                    "age": "20",
                    "email": "testing@bogusemail.com"
                }, 
                {
                    "name": "Mary",
                    "age": "23",
                    "email": "maryjacobs@bogusemail.com"
                }
            ])
    
    def __delete_data_from_csv(self):
        with open(self.file_directory, "w", newline="") as write_file:
            writer = csv.DictWriter(write_file, fieldnames=["name", "age", "email"], delimiter=",")
            writer.writeheader()