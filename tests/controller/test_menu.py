from colorama import Fore
import unittest
from unittest.mock import patch

from main.menu import menu_options
from main.menu import Menu



class TestMenu(unittest.TestCase):

    @patch("main.menu.Player")
    @patch("main.menu.Menu.initial_menu")
    @patch("main.menu.print")
    def setUp(self, mocked_print, mocked_initial_menu, mocked_player) -> None:
        self.menu = Menu()

    def test_initialize(self):
        menu_initialize_variables = self.menu.__dict__.keys()
        self.assertIn("player", menu_initialize_variables)

    def _test_initial_menu(self):
        pass
    
    @patch("main.menu.print")
    def test_display_welcome_message(self, mocked_print):
        self.menu.display_welcome_message()
        self.assertEqual(mocked_print.mock_calls[0].args[0], Fore.GREEN + "Hi, welcome to shell games!")

    @patch("main.menu.print")
    def test_display_initial_menu(self, mocked_print):
        self.menu.display_initial_menu()
        values_printed = [Fore.GREEN + "What would you like to do?"]
        for option in menu_options:
            values_printed.append(f"- {Fore.CYAN}{option}")

        for index, called in enumerate(mocked_print.mock_calls):
            self.assertEqual(called.args[0], values_printed[index])

    @patch("main.menu.input")
    def test_get_user_option_signup(self, mocked_input):
        mocked_input.return_value = "signup"
        self.assertTrue(self.menu.get_user_option())

    @patch("main.menu.print")
    @patch("main.menu.input")
    def test_get_user_option_signup_wrong(self, mocked_input, mocked_print):
        mocked_input.return_value = "sign up"
        self.assertFalse(self.menu.get_user_option())

    @patch("main.menu.input")
    def test_get_user_option_login(self, mocked_input):
        mocked_input.return_value = "login"
        self.assertTrue(self.menu.get_user_option())

    @patch("main.menu.print")
    @patch("main.menu.input")
    def test_get_user_option_login_wrong(self, mocked_input, mocked_print):
        mocked_input.return_value = "log in"
        self.assertFalse(self.menu.get_user_option())

    @patch("main.menu.print")
    def test_validate_user_option(self, mocked_print):
        validated = self.menu.validate_user_option("signup")
        self.assertEqual(validated, "Signup")
