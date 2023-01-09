from abc import ABC, abstractmethod

class DB(ABC):
    @abstractmethod
    def create_user(self, name, age, email, file_name):
        """Save user to database"""

    def update_user(self, email):
        """Update user on database"""
