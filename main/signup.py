import colorama
from colorama import Fore
from getpass import getpass
import re

from main.password import Password
from main import settings
from models.player import Player

colorama.init(autoreset=True)


class Signup(Password):
    def __init__(self):
        self.db = settings.DATABASE

    def run(self, player: Player) -> Player:
        email = self.validate_email(
            input("Email address (don't worry, we won't spam you): ")
        )
        age = self.validate_age(input("Age: "))
        password = self.validate_password()
        user = {
            "email": email,
            "age": age,
            "password": password,
        }
        self.db.create_user(**user)
        player.register_player(**user)
        return player

    def validate_email(self, email) -> str:
        if not isinstance(email, str):
            raise TypeError(f"Input {email} must be a str.")

        email = email.strip()
        email_regex = re.compile(r"@[a-zA-Z-\d]+\.(com|net|es|org)$")
        while not email_regex.search(email) or self.db.user_exists(email):
            email = input("Email not valid.\nEmail: ")

        return email

    @staticmethod
    def validate_age(age) -> int:
        if not isinstance(age, str):
            raise TypeError(f"Input {age} must be a str.")

        age = age.strip()
        while not age.isnumeric() or len(age) > 2:
            age = input("Age must be a number. Type again: ")

        return int(age.strip())

    def validate_password(self) -> str:
        password = getpass("Enter your password: ")
        password_1 = getpass("Enter your password again: ")

        while password != password_1 or len(password) < 8:
            if len(password) < 8:
                print(Fore.RED + "Password too short.")
            else:
                print(Fore.RED + "Passwords mismatch!")
            password = getpass("Enter your password: ")
            password_1 = getpass("Enter your password again: ")

        hashed_password = self.hash_password(password)

        return hashed_password
