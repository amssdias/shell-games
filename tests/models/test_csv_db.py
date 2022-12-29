import csv
import os
import unittest
from unittest.mock import patch
from models.abstract import DB

from models.csv_model import CSVDB


class TestCSVDB(unittest.TestCase):
    def setUp(self) -> None:
        self.db = CSVDB()
        self.file_directory = os.getcwd() + "\\tests\models\csv\\testing.csv"

    def test_inheritance(self):
        self.assertIsInstance(self.db, DB)

    def _test_save_user(self):
        pass

    def test_read_file(self):
        output_file, output_file_reader = self.db.read_file(self.file_directory)
        self.assertIsInstance(output_file_reader, csv.DictReader)
        output_file.close()

    def test_user_exists(self):
        with open(self.file_directory, "r") as new_file:
            file_reader = csv.DictReader(new_file, delimiter=",")

            self.assertTrue(self.db.user_exists("testing@bogusemail.com", file_reader))
            new_file.seek(0)

            self.assertTrue(self.db.user_exists("maryjacobs@bogusemail.com", file_reader))
            new_file.seek(0)

            self.assertFalse(self.db.user_exists("nouser@bogusemail.com", file_reader))

    def _test_save_user_to_file(self):
        pass

    def test_close_file(self):
        new_file = open(self.file_directory, "r")
        self.assertFalse(new_file.closed)

        self.db.close_file(new_file)
        self.assertTrue(new_file.closed)
        
