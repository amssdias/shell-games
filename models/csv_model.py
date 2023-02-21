from pathlib import Path

from models.file_model import FileDB
from models.files_models.csv_file import CSVFile


class CSVDB(FileDB):
    ext = ".csv"

    def __init__(self, file_path: Path = Path(Path.cwd(), "data.csv")):
        self.validate_file(file_path)
        super().__init__(file_type=CSVFile(file_path=file_path))
