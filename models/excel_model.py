from pathlib import Path

from models.file_model import FileDB
from models.files_models.excel_file import ExcelFile


class ExcelDB(FileDB):
    def __init__(self, file_path: Path = Path(Path.cwd(), "data.xlsx")):
        self.validate_file(file_path)
        super().__init__(file_type=ExcelFile(file_path=file_path))

    def validate_file(self, file_path: Path):
        if file_path.suffix != ".xlsx":
            raise Exception("File should be a .xlsx extension.")
        if not file_path.exists():
            raise Exception("File path does not exist.")
        return True
