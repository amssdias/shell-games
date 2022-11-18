from abc import ABC, abstractmethod


class Game(ABC):
    def play(self) -> bool:
        self.start_game_settings()
        won = self.start_game()
        return won

    @abstractmethod
    def start_game_settings(self):
        """Build all settings a game must do before playing."""
        pass

    @abstractmethod
    def start_game(self):
        pass
