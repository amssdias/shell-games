from abc import ABC, abstractmethod


class FileOperations(ABC):

    @abstractmethod
    def get_all_users(self):
        """Get all users from database"""

    @abstractmethod
    def get_user(self, email: str):
        """Get user by email"""

    @abstractmethod
    def save_user(self, user: dict):
        """Save user on file"""

    @abstractmethod
    def update_user_games_played(self, player: dict):
        """Update player 'games player' on database"""

    @abstractmethod
    def update_user_score(self, player: dict):
        """Update player 'score' on database"""
