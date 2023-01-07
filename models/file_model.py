from pathlib import Path
from models.abstract import DB
from models.constants.database_actions import DatabaseActions
from models.files_models import JsonFile
from models.files_models.csv_file import CSVFile


class FileDB(DB):

    def __init__(self, file_type):
        self.db = file_type

    def create_user(self, email: str, age: str, password: str):
        if self.user_exists(email):
            print("Seems like you have been here before. Enjoy :D")
            return self.db.get_user(email)

        user = {
            "email": email,
            "age": age,
            "password": password,
            "score": "0",
            "games_played": "0",
        }
        self.db.save_user(user)
        return user
    
    def user_exists(self, email):
        data = self.db.get_all_users()
        for line in data:
            if line["email"] == email:
                return line
        return False

    def update_user(self, player, action: DatabaseActions):
        if action == DatabaseActions.GAMES_PLAYED:
            return self.db.update_user_games_played(player)
        elif action == DatabaseActions.SCORE:
            return self.db.update_user_score(player)


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

