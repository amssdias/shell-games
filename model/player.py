import json
from .abstract import DB


class JsonDB(DB):
    def save_name(self, name, file="data.json"):
        with open("data.json", "r") as json_file:
            data = json.load(json_file)

        data.append({"name": name})

        with open("data.json", "w") as json_file:
            data = json.dump(data, json_file)
            return True


class CsvDB(DB):
    def save_name(self, name, file="data.csv"):
        pass


class PlayerModel():
    def __init__(self, db):
        self.db = db
        self.name = self.validate_name(input("Hey, what's your name? "))
        self.db.save_name(self.name)

    def validate_name(self, name):
        if not isinstance(name, str):
            raise Exception("Input must be a str.")
        return name.strip()
