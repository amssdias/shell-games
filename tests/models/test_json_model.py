import unittest
from pathlib import Path

from models import JsonDB


class TestJsonDB(unittest.TestCase):
    def setUp(self):
        self.file_directory = Path(Path.cwd(), "tests", "models", "db", "testing.json")
        self.db = JsonDB(file_path=self.file_directory)

    def test_initial_data(self):
        db_initial_variables = self.db.__dict__.keys()
        self.assertIn("db", db_initial_variables)

    def test_validate_file(self):
        self.assertTrue(self.db.validate_file(self.file_directory))
    
    def test_validate_wrong_file_extension(self):
        wrong_file_extension = Path(Path.cwd(), "tests", "models", "db", "testing.jso")
        with self.assertRaises(Exception) as err:
            self.db.validate_file(wrong_file_extension)

    def test_validate_wrong_file_path(self):
        wrong_file_extension = Path(Path.cwd(), "tests", "models", "random", "testing.json")
        with self.assertRaises(Exception) as err:
            self.db.validate_file(wrong_file_extension)
