from pathlib import Path
from models.file_model import FileDB
from models.files_models.csv_file import CSVFile
from models.files_models.json_file import JsonFile


class TestDBJson(FileDB):
    def __init__(self, file_path: Path = Path(Path.cwd(), "tests", "models", "db", "testing.json")):
        super().__init__(file_type=JsonFile(file_path=file_path))


class TestDBCSV(FileDB):
    def __init__(self, file_path: Path = Path(Path.cwd(), "tests", "models", "db", "testing.csv")):
        super().__init__(file_type=CSVFile(file_path=file_path))
