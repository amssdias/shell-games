from abc import ABC, abstractmethod
from typing import List


class Board(ABC):
    def __init__(self, columns, rows):
        self.positions: List[List] = self.build_board(columns=columns, rows=rows)

    @abstractmethod
    def build_board(self, columns, rows):
        """Create a fresh new board"""

    @abstractmethod
    def display_board(self):
        """Display the current board"""
