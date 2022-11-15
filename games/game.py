from abc import ABC, abstractmethod


class Game(ABC):
    def play(self) -> bool:
        self.start_game_settings()
        won = self.start_game()
        return won

    @abstractmethod
    def start_game_settings(self):
        pass

    @abstractmethod
    def start_game(self):
        pass
