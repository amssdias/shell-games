import csv
import json
import unittest


class TestFile(unittest.TestCase):

    def setUp(self) -> None:
        self.user_1 = {
            "name": "testing",
            "age": "20",
            "email": "testing@bogusemail.com"
        }
        self.user_2 = {
            "name": "Mary",
            "age": "23",
            "email": "maryjacobs@bogusemail.com"
        }

        self.users = [self.user_1, self.user_2]

    def write_data_to_csv(self):
        with open(self.file_directory, "a", newline="") as write_file:
            writer = csv.DictWriter(write_file, fieldnames=["name", "age", "email"], delimiter=",")
            writer.writerows([self.user_1, self.user_2])
    
    def delete_data_from_csv(self):
        with open(self.file_directory, "w", newline="") as write_file:
            writer = csv.DictWriter(write_file, fieldnames=["name", "age", "email"], delimiter=",")
            writer.writeheader()

    def write_data_to_json(self):
        with open(self.file_directory, "w", newline="") as write_file:
            json.dump(self.users, write_file)
        return True
    
    def delete_data_from_json(self):
        with open(self.file_directory, "w", newline="") as write_file:
            json.dump([], write_file)
        return True
