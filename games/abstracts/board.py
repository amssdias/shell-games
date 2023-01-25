from abc import ABC, abstractmethod
from typing import List


class Board(ABC):
    def __init__(self, columns, rows):
        self.positions: List[List] = self.build_board(columns=columns, rows=rows)

    def __str__(self) -> str:
        return f"{self.__class__.__name__} with {len(self.positions[0])} columns and {len(self.positions)} rows."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({len(self.positions[0])}, {len(self.positions)})"

    @abstractmethod
    def build_board(self, columns, rows):
        """Create a fresh new board"""

    @abstractmethod
    def display_board(self):
        """Display the current board"""
