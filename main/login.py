import re

from main import settings
from main.password import Password


class Login(Password):

    def __init__(self):
        self.db = settings.DATABASE

    def run(self):
        email = input("Email: ")
        password = input("Password: ")

        return self.login_user(email, password)

    def login_user(self, email, password):
        user_exists = self.db.user_exists(email)

        if user_exists and self.check_password(password, user_exists["password"]):
            return user_exists

        print("Sorry user email not found. Try to Signup first.")
        return False
