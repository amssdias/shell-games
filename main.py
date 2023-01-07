from main.controller import Controller
from main.menu import Menu


player = Menu().player
c = Controller(player)
c.start()
