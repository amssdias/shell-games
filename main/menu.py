import colorama
from colorama import Fore
import re

from main import settings
from main.login import Login
from main.signup import Signup
from models.player import Player

colorama.init(autoreset=True)


menu_options = {
    "Signup": Signup,
    "Login": Login,
}

class Menu:

    def __init__(self):
        self.display_welcome_message()

        self.player = Player(settings.DATABASE)
        while not self.player.logged:
            self.initial_menu(self.player)


    def initial_menu(self, player: Player):
        while True:
            self.display_initial_menu()
            validated_user_option = self.get_user_option()
            if validated_user_option:
                break

        validated_user_option.run(player)

    def display_welcome_message(self):
        print(Fore.GREEN + "Hi, welcome to shell games!")

    def display_initial_menu(self):
        print(Fore.GREEN + "What would you like to do?")
        for option in menu_options.keys():
            print(f"- {Fore.CYAN}{option}")

    def get_user_option(self):
        validated = self.validate_user_option(input("Write your choice: "))
        if validated:
            return menu_options[validated]()
        return False

    def validate_user_option(self, user_input: str):
        user_input_capitalized = user_input.capitalize()
        if user_input_capitalized not in menu_options.keys():
            print(Fore.RED + "Option not available.")
            return False
        return user_input_capitalized
