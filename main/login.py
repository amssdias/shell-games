from getpass import getpass

from main import settings
from main.password import Password


class Login(Password):

    def __init__(self):
        self.db = settings.DATABASE

    def run(self, player):
        email = input("Email: ")
        password = getpass("Password: ")

        return self.login_user(player, email, password)

    def login_user(self, player, email, password):
        user_exists = self.db.user_exists(email)

        if user_exists and self.check_password(password, user_exists["password"]):
            player.logged = True
            return user_exists

        print("Sorry user email not found. Try to Signup first.")
        return False
