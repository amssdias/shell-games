import colorama
from colorama import Fore
import re

from main.password import Password
from main import settings

colorama.init(autoreset=True)


class Signup(Password):
    def __init__(self):
        self.db = settings.DATABASE

    def run(self):
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
        return user

    @staticmethod
    def validate_email(email):
        if not isinstance(email, str):
            raise TypeError(f"Input {email} must be a str.")

        # TODO: Check if email doesn't exist already
        email = email.strip()
        email_regex = re.compile(r"@[a-zA-Z-\d]+\.(com|net|es|org)$")
        while not email_regex.search(email):
            email = input("Email not valid.\nEmail: ")

        return email

    @staticmethod
    def validate_age(age):
        if not isinstance(age, str):
            raise TypeError(f"Input {age} must be a str.")

        # TODO: Validate age is not "00", "01".. till 10 (not included), add tests
        age = age.strip()
        while not age.isnumeric() or len(age) > 2:
            age = input("Age must be a number. Type again: ")

        return age.strip()

    def validate_password(self):
        password = input("Enter your password: ")
        password_1 = input("Enter your password again: ")

        while password != password_1 or len(password) < 8:
            print(Fore.RED + "Passwords mismatch!")
            password = input("Enter your password: ")
            password_1 = input("Enter your password again: ")

        hashed_password = self.hash_password(password)

        return hashed_password
