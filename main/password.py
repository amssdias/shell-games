import hashlib

from main.settings import SECRET_KEY

class Password:
    encode_format = "utf-8"

    @classmethod
    def hash_password(cls, password):
        salted_password = cls.salt_password(password)
        return cls.get_hashed_password(salted_password)

    @classmethod
    def salt_password(cls, password_encoded):
        return str(password_encoded + SECRET_KEY).encode(cls.encode_format)

    @classmethod
    def get_hashed_password(cls, salted_password):
        hash_object = hashlib.sha256()
        hash_object.update(salted_password)
        return hash_object.hexdigest()

    @classmethod
    def check_password(cls, password, hashed_password):
        salted_password = cls.salt_password(password)
        hashed_user_password = cls.get_hashed_password(salted_password)

        if hashed_user_password == hashed_password:
            return True
        return False