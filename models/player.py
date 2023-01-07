import re

from models.abstract import DB
from models.constants.database_actions import DatabaseActions
from tasks.thread_tasks import ThreadTask


class Player:
    def __init__(self, db: DB, email, age, password):
        self.db = db
        
        self.email = email
        self.age = age
        self.password = password
        self.user = {
            "email": self.email,
            "age": self.age,
            "password": self.password,
        }

    def update_games_played(self):
        ThreadTask.task(self.db.update_user, self.user, DatabaseActions.GAMES_PLAYED)

    def update_score(self):
        ThreadTask.task(self.db.update_user, self.user, DatabaseActions.SCORE)
