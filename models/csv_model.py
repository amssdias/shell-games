import csv

from models.abstract import DB


class CSVDB(DB):
    def save_user(self, name, age, email, file_name="data.csv"):
        csv_file_reader, csv_reader = self.read_file(file_name)
        if self.user_exists(email, csv_reader):
            print("Seems like you have been here before. Enjoy :D")
            return self

        self.save_user_to_file(name, age, email, file_name)

        self.close_file(csv_file_reader)
        return {"name": name, "age": age, "email": email}

    @staticmethod
    def read_file(file_name):
        csv_file = open(file_name, "r")
        return csv_file, csv.DictReader(csv_file, delimiter=",")

    @staticmethod
    def user_exists(email, csv_reader):
        for line in csv_reader:
            if line["email"] == email:
                return True
        return False

    def save_user_to_file(self, name, age, email, file_name):
        with open(file_name, "a", newline="") as update_csv:
            writer = csv.DictWriter(update_csv, fieldnames=["name", "age", "email"], delimiter=",")

            new_user = {
                "name": name,
                "age": age,
                "email": email,
            }
            writer.writerow(new_user + "\n")

        return update_csv

    @staticmethod
    def close_file(filename):
        filename.close()
