import json

from models.abstract import DB


class JsonDB(DB):
    def save_user(self, name, age, email, file_name="data.json"):
        with open("data.json", "r") as json_file:
            data = json.load(json_file)
        
        data.append({"name": name})

        with open("data.json", "w") as json_file:
            data = json.dump(data, json_file)
            return True
