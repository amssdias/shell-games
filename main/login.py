from getpass import getpass
from typing import Dict, Union

from main import settings
from main.password import Password
from models.player import Player


class Login(Password):
    def __init__(self):
        self.db = settings.DATABASE

    def run(self, player: Player) -> Union[bool, Dict]:
        email = input("Email: ")
        password = getpass("Password: ")

        return self.login_user(player, email, password)

    def login_user(
        self, player: Player, email: str, password: str
    ) -> Union[bool, Dict]:
        user_exists = self.db.user_exists(email)

        if user_exists and self.check_password(password, user_exists["password"]):
            player.logged = True
            player.register_player(
                email=email, age=user_exists["age"], password=password
            )
            return user_exists

        print("Sorry user email not found. Try to Signup first.")
        return False
