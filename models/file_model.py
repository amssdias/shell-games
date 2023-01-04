from pathlib import Path
from models.abstract import DB
from models.files_models import JsonFile
from models.files_models.csv_model import CSVFile


class FileDB(DB):

    def __init__(self, file_type, file_path: Path):
        self.db = file_type
        self.file_path = file_path

    def save_user(self, name: str, age: str, email: str):
        if self.file_path.exists():
        if self.user_exists(email):
            print("Seems like you have been here before. Enjoy :D")
            return False

        data = self.get_file_content()
        else:
            data = []

        user = {
            "name": name,
            "age": age,
            "email": email,
        }
        self.db.write_to_file(user, data, self.file_path)
        return True
    
    def user_exists(self, email):
        data = self.get_file_content()
        for line in data:
            if line["email"] == email:
                return True
        return False

    def get_file_content(self):
        opened_file = open(self.file_path, "r")
        file_content = self.db.get_content(opened_file)
        opened_file.close()
        return file_content


class JsonDB(FileDB):
    def __init__(self, file_path: Path = Path(Path.cwd(), "data.json")):
        self.validate_file(file_path)
        super().__init__(file_type=JsonFile(), file_path=file_path)

    def validate_file(self, file_path: Path):
        if file_path.suffix != ".json":
            raise Exception("File should be a csv extension.")

class CSVDB(FileDB):
    def __init__(self, file_path: Path = Path(Path.cwd(), "data.csv")):
        self.validate_file(file_path)
        super().__init__(file_type=CSVFile(), file_path=file_path)

    def validate_file(self, file_path: Path):
        if file_path.suffix != ".csv":
            raise Exception("File should be a json extension.")