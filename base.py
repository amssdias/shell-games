from main import settings
from main.controller import Controller

from models.player import Player


player_model = Player(settings.DB)
c = Controller(player_model)
c.start()
