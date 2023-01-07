import csv
import json
import unittest


class TestFile(unittest.TestCase):

    def setUp(self) -> None:
        self.user_1 = {
            "email": "testing@bogusemail.com",
            "age": "20",
            "password": "password",
            "score": "0",
            "games_played": "0",
        }
        self.user_2 = {
            "age": "23",
            "email": "maryjacobs@bogusemail.com",
            "password": "password",
            "score": "0",
            "games_played": "0",
        }

        self.fieldnames = ["email", "age", "password", "score", "games_played"]

        self.users = [self.user_1, self.user_2]

    def write_data_to_csv(self):
        with open(self.file_directory, "a", newline="") as write_file:
            writer = csv.DictWriter(write_file, fieldnames=self.fieldnames, delimiter=",")
            writer.writerows([self.user_1, self.user_2])
    
    def delete_data_from_csv(self):
        with open(self.file_directory, "w", newline="") as write_file:
            writer = csv.DictWriter(write_file, fieldnames=self.fieldnames, delimiter=",")
            writer.writeheader()

    def write_data_to_json(self):
        with open(self.file_directory, "w", newline="") as write_file:
            json.dump(self.users, write_file)
        return True
    
    def delete_data_from_json(self):
        with open(self.file_directory, "w", newline="") as write_file:
            json.dump([], write_file)
        return True
