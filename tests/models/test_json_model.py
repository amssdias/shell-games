from pathlib import Path

from models import JsonDB


class TestJsonDB:
    def setUp(self) -> None:
        super().setUp()
        self.file_directory = Path(Path.cwd(), "tests", "models", "db", "testing.json")
        self.db = JsonDB(file_path=self.file_directory)

    def _test_initial_data(self):
        pass

    def _test_validate_file(self):
        pass 