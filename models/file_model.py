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
