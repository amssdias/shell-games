import csv

from tests.models.utils.file_utils import TestFileUtils


class TestCSVFileUtils(TestFileUtils):
    def write_data_to_csv(self):
        with open(self.file_directory, "a", newline="") as write_file:
            writer = csv.DictWriter(write_file, fieldnames=self.headers, delimiter=",")
            writer.writerows([self.user_1, self.user_2])

    def delete_data_from_csv(self):
        with open(self.file_directory, "w", newline="") as write_file:
            writer = csv.DictWriter(write_file, fieldnames=self.headers, delimiter=",")
            writer.writeheader()
