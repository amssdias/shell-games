from models.abstract import DB


class Player():
    def __init__(self, db):
        self.db = db
        self.name = self.validate_name(input("Hey, what's your name? "))
        self.age = self.validate_age(input("How old are you? "))
        self.email = self.validate_email(input("Tell me your email address (don't worry, we won't spam you): "))
        
        self.db.save_user(self.name, self.age, self.email)

    def validate_name(self, name):
        if not isinstance(name, str):
            raise Exception("Input must be a str.")
        return name.strip()

    def validate_age(self, age):
        if not isinstance(age, str):
            raise Exception("Input must be a str.")

        # TODO: Check if its a number
        return age.strip()

    def validate_email(self, email):
        if not isinstance(email, str):
            raise Exception("Input must be a str.")

        # TODO: Use Regex to make sure its an email
        return email.strip()

