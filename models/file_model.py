from pathlib import Path
from typing import Dict, Union
from models.abstracts.db import DB
from models.abstracts.file_operations import FileOperations
from models.constants.database_actions import DatabaseActions


class FileDB(DB):
    ext = ""

    def __init__(self, file_type: FileOperations):
        self.db = file_type

    def validate_file(self, file_path: Path):
        if file_path.suffix != self.ext:
            raise Exception(
                f"Invalid file format for the current DB. It should be {self.ext}"
            )
        if not file_path.exists():
            raise Exception("File path does not exist.")
        return True

    def create_user(self, email: str, age: int, password: str) -> Dict:
        if self.user_exists(email):
            return self.db.get_user(email)

        user = {
            "email": email,
            "age": age,
            "password": password,
            "score": 0,
            "games_played": 0,
        }
        self.db.save_user(user)
        return user

    def user_exists(self, email) -> Union[Dict, bool]:
        data = self.db.get_all_users()
        for line in data:
            if line["email"] == email:
                return line
        return False

    def update_user(self, player: dict, action: DatabaseActions) -> None:
        if action == DatabaseActions.GAMES_PLAYED:
            return self.db.update_user_games_played(player)
        elif action == DatabaseActions.SCORE:
            return self.db.update_user_score(player)
