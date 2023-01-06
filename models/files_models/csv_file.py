import csv

from models.constants.database_actions import DatabaseActions


class CSVFile:

    def __init__(self, file_path):
        self.file_path = file_path

    def get_all_users(self):
        opened_file = open(self.file_path, "r")
        users = list(csv.DictReader(opened_file, delimiter=","))
        opened_file.close()
        return users
    
    def get_user(self, email):
        with open(self.file_path, "r") as csv_file:
            users = list(csv.DictReader(csv_file, delimiter=","))

        for user in users:
            if user["email"] == email:
                return user

    def save_user(self, user: dict):
        with open(self.file_path, "a", newline="") as update_csv:
            writer = csv.DictWriter(update_csv, fieldnames=["name", "age", "email", "score", "games_played"], delimiter=",")
            writer.writerow(user)
        return True
    
    def update_user_games_played(self, player):
        users = self.get_all_users()

        with open(self.file_path, "w", newline="") as update_csv:
            writer = csv.DictWriter(update_csv, fieldnames=["name", "age", "email", "score", "games_played"], delimiter=",")
            writer.writeheader()
            for user in users:
                if user["email"] == player["email"]:
                    try:
                        user["games_played"] = int(user["games_played"]) + 1
                    except TypeError as e:
                        raise TypeError(e)
                    player = user
                writer.writerow(user)
        return player

    def update_user_score(self, player):
        users = self.get_all_users()

        with open(self.file_path, "w", newline="") as update_csv:
            writer = csv.DictWriter(update_csv, fieldnames=["name", "age", "email", "score", "games_played"], delimiter=",")
            writer.writeheader()
            for user in users:
                if user["email"] == player["email"]:
                    try:
                        user["score"] = int(user["score"]) + 1
                    except TypeError as e:
                        raise TypeError(e)
                    player = user
                writer.writerow(user)
        return player
