import csv
from typing import Dict, List, Optional
from models.abstracts.file_operations import FileOperations


class CSVFile(FileOperations):
    def __init__(self, file_path):
        self.file_path = file_path
        self.fieldnames = ["email", "age", "password", "score", "games_played"]

    def get_all_users(self) -> List:
        opened_file = open(self.file_path, "r")
        users = list(csv.DictReader(opened_file, delimiter=","))
        opened_file.close()
        return users

    def get_user(self, email: str) -> Optional[Dict]:
        with open(self.file_path, "r") as csv_file:
            users = list(csv.DictReader(csv_file, delimiter=","))

        for user in users:
            if user["email"] == email:
                return user

    def save_user(self, user: Dict) -> bool:
        with open(self.file_path, "a", newline="") as update_csv:
            writer = csv.DictWriter(
                update_csv, fieldnames=self.fieldnames, delimiter=","
            )
            writer.writerow(user)
        return True

    def update_user_games_played(self, player: Dict) -> bool:
        users = self.get_all_users()

        with open(self.file_path, "w", newline="") as update_csv:
            writer = csv.DictWriter(
                update_csv, fieldnames=self.fieldnames, delimiter=","
            )
            writer.writeheader()
            for user in users:
                if user["email"] == player["email"]:
                    try:
                        user["games_played"] = int(user["games_played"]) + 1
                    except TypeError as e:
                        raise TypeError(e)
                writer.writerow(user)
        return True

    def update_user_score(self, player: dict) -> bool:
        users = self.get_all_users()

        with open(self.file_path, "w", newline="") as update_csv:
            writer = csv.DictWriter(
                update_csv, fieldnames=self.fieldnames, delimiter=","
            )
            writer.writeheader()
            for user in users:
                if user["email"] == player["email"]:
                    try:
                        user["score"] = int(user["score"]) + 1
                    except TypeError as e:
                        raise TypeError(e)
                writer.writerow(user)
        return True
