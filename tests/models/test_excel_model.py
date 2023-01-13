import unittest
from pathlib import Path

from models import ExcelDB


class TestExcelDB(unittest.TestCase):
    def setUp(self):
        self.file_directory = Path(Path.cwd(), "tests", "models", "db", "testing.xlsx")
        self.db = ExcelDB(file_path=self.file_directory)

    def test_initial_data(self):
        db_initial_variables = self.db.__dict__.keys()
        self.assertIn("db", db_initial_variables)

    def test_validate_file(self):
        self.assertTrue(self.db.validate_file(self.file_directory))

    def test_validate_wrong_file_extension(self):
        wrong_file_extension = Path(Path.cwd(), "tests", "models", "db", "testing.xl")
        with self.assertRaises(Exception) as err:
            self.db.validate_file(wrong_file_extension)

    def test_validate_wrong_file_path(self):
        wrong_file_extension = Path(
            Path.cwd(), "tests", "models", "random", "testing.xlsx"
        )
        with self.assertRaises(Exception) as err:
            self.db.validate_file(wrong_file_extension)
