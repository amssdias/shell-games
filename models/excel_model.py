from pathlib import Path

from models.file_model import FileDB
from models.files_models.excel_file import ExcelFile


class ExcelDB(FileDB):
    ext = ".xlsx"

    def __init__(self, file_path: Path = Path(Path.cwd(), "data.xlsx")):
        self.validate_file(file_path)
        super().__init__(file_type=ExcelFile(file_path=file_path))
