import re

from models.abstract import DB
from models.constants.database_actions import DatabaseActions
from tasks.thread_tasks import ThreadTask


class Player:
    def __init__(self, db: DB):
        self.db = db
        self.name = self.validate_name(input("Hey, what's your name? "))
        self.age = self.validate_age(input("Age: "))
        self.email = self.validate_email(
            input("Email address (don't worry, we won't spam you): ")
        )

        self.user = self.db.create_user(self.name, self.age, self.email)

    def validate_name(self, name):
        if not isinstance(name, str):
            raise TypeError(f"Input {name} must be a str.")
        return name.strip()

    def validate_age(self, age):
        if not isinstance(age, str):
            raise TypeError(f"Input {age} must be a str.")

        # TODO: Validate age is not "00", "01".. till 10 (not included), add tests
        age = age.strip()
        while not age.isnumeric() or len(age) > 2:
            age = input("Age must be a number. Type again: ")

        return age.strip()

    def validate_email(self, email):
        if not isinstance(email, str):
            raise TypeError(f"Input {email} must be a str.")

        email = email.strip()
        email_regex = re.compile(r"@[a-zA-Z-\d]+\.(com|net|es|org)$")
        while not email_regex.search(email):
            email = input("Email not valid.\nEmail: ")

        return email

    def update_games_played(self):
        ThreadTask.task(self.db.update_user, self.user, DatabaseActions.GAMES_PLAYED)

    def update_score(self):
        ThreadTask.task(self.db.update_user, self.user, DatabaseActions.SCORE)
