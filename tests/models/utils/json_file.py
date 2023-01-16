import json

from tests.models.utils.file_utils import TestFileUtils


class TestJsonFileUtils(TestFileUtils):
    def write_data_to_json(self):
        with open(self.file_directory, "w", newline="") as write_file:
            json.dump(self.users, write_file)
        return True

    def delete_data_from_json(self):
        with open(self.file_directory, "w", newline="") as write_file:
            json.dump([], write_file)
        return True
