from threading import Thread
from typing import Callable


class ThreadTask:

    @classmethod
    def task(self, target: Callable, *args):
        thread = Thread(target=target, args=[*args])
        thread.start()
