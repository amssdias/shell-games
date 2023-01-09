from pathlib import Path

from models.file_model import FileDB
from models.files_models.json_file import JsonFile


class JsonDB(FileDB):
    def __init__(self, file_path: Path = Path(Path.cwd(), "data.json")):
        self.validate_file(file_path)
        super().__init__(file_type=JsonFile(file_path=file_path))

    def validate_file(self, file_path: Path):
        if file_path.suffix != ".json":
            raise Exception("File should be a json extension.")
        if not file_path.exists():
            raise Exception("File path does not exist.")
        return True
