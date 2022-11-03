from abc import ABC, abstractmethod


class Game(ABC):

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def start_game_settings(self):
        pass
