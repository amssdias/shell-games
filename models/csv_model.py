import csv

from models.abstract import DB


class CSVDB(DB):
    def save_user(self, name, age, email, file_path="data.csv"):
        if self.user_exists(email, file_path):
            print("Seems like you have been here before. Enjoy :D")
            return False

        self.save_user_to_file(name, age, email, file_path)
        return True

    @staticmethod
    def read_file(file_path):
        csv_file = open(file_path, "r")
        return csv_file, csv.DictReader(csv_file, delimiter=",")

    def user_exists(self, email, file_path):
        csv_file_reader, csv_reader = self.read_file(file_path)
        for line in csv_reader:
            if line["email"] == email:
                self.close_file(csv_file_reader)
                return True
        self.close_file(csv_file_reader)
        return False

    def save_user_to_file(self, name, age, email, file_path):
        with open(file_path, "a", newline="") as update_csv:
            writer = csv.DictWriter(update_csv, fieldnames=["name", "age", "email"], delimiter=",")

            new_user = {
                "name": name,
                "age": age,
                "email": email,
            }
            writer.writerow(new_user)

        return True

    @staticmethod
    def close_file(filename):
        filename.close()
