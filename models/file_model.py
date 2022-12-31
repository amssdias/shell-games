from models.abstract import DB
from models.files_models import JsonFile


class FileDB(DB):

    def __init__(self, file_type=JsonFile(), file_path="data.json"):
        self.db = file_type
        self.file_path = file_path

    def save_user(self, name, age, email):
        if self.user_exists(email, self.file_path):
            print("Seems like you have been here before. Enjoy :D")
            return False

        data = self.get_file_content(self.file_path)
        user = {
            "name": name,
            "age": age,
            "email": email,
        }
        self.db.write_to_file(user, data, self.file_path)
        return True
    
    def user_exists(self, email, file_path):
        data = self.get_file_content(file_path)
        for line in data:
            if line["email"] == email:
                return True
        return False

    def get_file_content(self, file_path):
        opened_file = open(file_path, "r")
        file_content = self.db.get_content(opened_file)
        opened_file.close()
        return file_content

