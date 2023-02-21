from pathlib import Path

from models.file_model import FileDB
from models.files_models.json_file import JsonFile


class JsonDB(FileDB):
    ext = ".json"

    def __init__(self, file_path: Path = Path(Path.cwd(), "data.json")):
        self.validate_file(file_path)
        super().__init__(file_type=JsonFile(file_path=file_path))
