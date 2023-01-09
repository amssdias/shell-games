from models.abstracts.db import DB
from models.constants.database_actions import DatabaseActions
from tasks.thread_tasks import ThreadTask


class Player:
    def __init__(self, db: DB):
        self.db = db
        
        self.logged = False
        self.email = None
        self.age = None
        self.password = None

    def register_player(self, email: str, age: int, password: str) -> None:
        self.email = email
        self.age = age
        self.password = password

    def update_games_played(self) -> None:
        player = {
            "email": self.email,
            "age": self.age,
            "password": self.password,
        }
        ThreadTask.task(self.db.update_user, player, DatabaseActions.GAMES_PLAYED)

    def update_score(self) -> None:
        player = {
            "email": self.email,
            "age": self.age,
            "password": self.password,
        }
        ThreadTask.task(self.db.update_user, player, DatabaseActions.SCORE)
