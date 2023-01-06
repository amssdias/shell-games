import json
from pathlib import Path


class JsonFile:

    def __init__(self, file_path: Path):
        self.file_path = file_path

    def get_all_users(self):
        opened_file = open(self.file_path, "r")
        file_content = json.load(opened_file)
        opened_file.close()
        return file_content

    def get_user(self, email):
        with open(self.file_path, "r") as json_file:
            file_content = json.load(json_file)

        for line in file_content:
            if line["email"] == email:
                return line

    def save_user(self, user: dict):
        users = self.get_all_users()
        users.append(user)
        with open(self.file_path, "w") as json_file:
            json.dump(users, json_file, indent=2)
        return True

    def update_user_games_played(self, player):
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
            json.dump(users, json_file, indent=2)
        return player

    def update_user_score(self, player):
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
            json.dump(users, json_file, indent=2)
        return player
