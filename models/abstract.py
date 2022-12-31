from abc import ABC, abstractmethod

class DB(ABC):
    @abstractmethod
    def save_user(self, name, age, email, file_name):
        """Save user to database"""
