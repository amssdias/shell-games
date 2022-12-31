import csv


class CSVFile:
    def get_content(self, open_file):
        return list(csv.DictReader(open_file, delimiter=","))

    def write_to_file(self, user: dict, data: list, file_path: str):
        with open(file_path, "a", newline="") as update_csv:
            writer = csv.DictWriter(update_csv, fieldnames=["name", "age", "email"], delimiter=",")
            writer.writerow(user)
        return True