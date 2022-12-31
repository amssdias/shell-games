import os
from unittest.mock import patch
from models.abstract import DB

from models.file_model import FileDB
from models.files_models import CSVFile
from tests.models.utils.test_file_utils import TestFile


class TestFileModel(TestFile):
    def setUp(self) -> None:
        super().setUp()
        self.file_directory = os.getcwd() + "/tests/models/csv/testing.csv"
        self.db = FileDB(file_type=CSVFile(), file_path=self.file_directory)

    def test_inheritance(self):
        self.assertIsInstance(self.db, DB)
        self.assertIsInstance(self.db.db, CSVFile)
        self.assertIsInstance(self.db.file_path, str)

        db_initial_variables = self.db.__dict__.keys()
        self.assertIn("db", db_initial_variables)
        self.assertIn("file_path", db_initial_variables)

    def test_save_existing_user(self):
        self.write_data_to_csv()
        with patch("models.file_model.print") as mocked_print:
            new_user = self.db.save_user(**self.user_1)
        self.assertFalse(new_user)
        self.delete_data_from_csv()

    def test_user_exists(self):
        self.write_data_to_csv()

        self.assertTrue(self.db.user_exists(self.user_1["email"], self.file_directory))
        self.assertTrue(self.db.user_exists(self.user_2["email"], self.file_directory))
        self.assertFalse(self.db.user_exists("nouser@bogusemail.com", self.file_directory))

        self.delete_data_from_csv()

    def test_get_content(self):
        self.write_data_to_csv()
        data = self.db.get_file_content(self.file_directory)
        self.assertCountEqual(data, [self.user_1, self.user_2])
        self.delete_data_from_csv()

