from pathlib import Path

from models.file_model import FileDB
from models.files_models.csv_file import CSVFile


class CSVDB(FileDB):
    def __init__(self, file_path: Path = Path(Path.cwd(), "data.csv")):
        self.validate_file(file_path)
        super().__init__(file_type=CSVFile(file_path=file_path))

    def validate_file(self, file_path: Path):
        if file_path.suffix != ".csv":
            raise Exception("File should be a csv extension.")
        if not file_path.exists():
            raise Exception("File path does not exist.")
        return True
