import json
from pathlib import Path
from typing import Dict, List, Union

from models.abstracts.file_operations import FileOperations


class JsonFile(FileOperations):

    def __init__(self, file_path: Path):
        self.file_path = file_path

    def get_all_users(self) -> List:
        opened_file = open(self.file_path, "r")
        file_content = json.load(opened_file)
        opened_file.close()
        return file_content

    def get_user(self, email) -> Union[Dict, None]:
        with open(self.file_path, "r") as json_file:
            file_content = json.load(json_file)

        for line in file_content:
            if line["email"] == email:
                return line

    def save_user(self, user: Dict) -> bool:
        users = self.get_all_users()
        users.append(user)
        with open(self.file_path, "w") as json_file:
            json.dump(users, json_file, indent=2)
        return True

    def update_user_games_played(self, player) -> Dict:
        users = self.get_all_users()
        with open(self.file_path, "w") as json_file:
            for user in users:
                if user["email"] == player["email"]:
                    try:
                        user["games_played"] = int(user["games_played"]) + 1
                    except TypeError as e:
                        raise TypeError(e)
                    player = user
                    break
            else:
                raise ValueError("Missing user from database.")
            json.dump(users, json_file, indent=2)
        return player

    def update_user_score(self, player: Dict) -> Union[Dict, Exception]:
        users = self.get_all_users()
        with open(self.file_path, "w") as json_file:
            for user in users:
                if user["email"] == player["email"]:
                    try:
                        user["score"] = int(user["score"]) + 1
                    except TypeError as e:
                        raise TypeError(e)
                    player = user
                    break
            else:
                raise ValueError("Missing user from database.")
            json.dump(users, json_file, indent=2)
        return player
