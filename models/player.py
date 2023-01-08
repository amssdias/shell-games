import re

from models.abstract import DB
from models.constants.database_actions import DatabaseActions
from tasks.thread_tasks import ThreadTask


class Player:
    def __init__(self, db: DB):
        self.db = db
        
        self.logged = False
        self.email = None
        self.age = None
        self.password = None

    def register_player(self, email, age, password):
        self.email = email
        self.age = age
        self.password = password

    def update_games_played(self):
        player = {
            "email": self.email,
            "age": self.age,
            "password": self.password,
        }
        ThreadTask.task(self.db.update_user, player, DatabaseActions.GAMES_PLAYED)

    def update_score(self):
        player = {
            "email": self.email,
            "age": self.age,
            "password": self.password,
        }
        ThreadTask.task(self.db.update_user, player, DatabaseActions.SCORE)
