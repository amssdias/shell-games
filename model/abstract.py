from abc import ABC, abstractmethod

class DB(ABC):
    @abstractmethod
    def save_name(self, name):
        pass