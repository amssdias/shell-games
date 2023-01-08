import hashlib

from main.settings import SECRET_KEY

class Password:
    encode_format = "utf-8"

    def hash_password(self, password):
        salted_password = self.salt_password(password)
        return self.get_hashed_password(salted_password)

    def salt_password(self, password_encoded):
        return str(password_encoded + SECRET_KEY).encode(self.encode_format)

    def get_hashed_password(self, salted_password):
        hash_object = hashlib.sha256()
        hash_object.update(salted_password)
        return hash_object.hexdigest()

    def check_password(self, password, hashed_password):
        salted_password = self.salt_password(password)
        hashed_user_password = self.get_hashed_password(salted_password)

        if hashed_user_password == hashed_password:
            return True
        return False