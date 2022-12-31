import json


class JsonFile:
    def get_content(self, opened_file):
        return json.load(opened_file)

    def write_to_file(self, user: dict, data: list, file_path: str):
        data.append(user)
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=2)
        return True
