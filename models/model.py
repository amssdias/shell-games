import csv
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



class CsvDB(DB):
    def save_user(self, name, age, email, file_name="data.csv"):
        csv_file_reader, csv_reader = self.read_file(file_name)
        if self.user_exists(email, csv_reader):
            print("Seems like you have been here before. Enjoy :D")
            return self

        self.save_user_to_file(name, age, email, file_name, csv_file_reader, csv_reader)
        return csv_file_reader

    @staticmethod
    def read_file(file_name):
        with open(file_name, "r") as csv_file:
            return csv_file, csv.DictReader(csv_file, delimiter=",")

    @staticmethod
    def user_exists(email, csv_reader):
        next(csv_reader) # Skip headers
        for line in csv_reader:
            if line["email"] == email:
                return True
        return False

    def save_user_to_file(self, name, age, email, file_name, csv_file_reader, csv_reader):
        with open(file_name, "w", newline="") as update_csv:
            fieldnames = ["name", "age", "email"]
            csv_writer = csv.DictWriter(update_csv, fieldnames=fieldnames, delimiter=",")

            csv_writer.writeheader()
            csv_file_reader.seek(0)
            next(csv_reader) # Skip headers

            for line in csv_reader:
                csv_writer.writerow(line)

            new_user = {
                "name": name,
                "age": age,
                "email": email,
            }
            csv_writer.writerow(new_user)

        return update_csv

