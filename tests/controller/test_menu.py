from colorama import Fore
import unittest
from unittest.mock import MagicMock, patch

from main.login import Login
from main.menu import Menu, menu_options
from main.signup import Signup



class TestMenu(unittest.TestCase):

    @patch("main.menu.Player")
    @patch("main.menu.Menu.initial_menu")
    @patch("builtins.print")
    def setUp(self, mocked_print, mocked_initial_menu, mocked_player) -> None:
        self.menu = Menu()

    def test_initialize(self):
        menu_initialize_variables = self.menu.__dict__.keys()
        self.assertIn("player", menu_initialize_variables)

    def test_initial_menu(self):
        menu_option = MagicMock()
        self.menu.display_initial_menu = MagicMock(return_value=None)
        self.menu.get_user_option = MagicMock(return_value=menu_option)

        self.menu.initial_menu(self.menu.player)

        self.menu.display_initial_menu.assert_called_once()
        self.menu.get_user_option.assert_called_once()
        menu_option.run.assert_called_once()
    
    @patch("builtins.print")
    def test_display_welcome_message(self, mocked_print):
        self.menu.display_welcome_message()
        self.assertEqual(mocked_print.mock_calls[0].args[0], Fore.GREEN + "Hi, welcome to shell games!")

    @patch("builtins.print")
    def test_display_initial_menu(self, mocked_print):
        self.menu.display_initial_menu()
        values_printed = [Fore.GREEN + "What would you like to do?"]
        for option in menu_options:
            values_printed.append(f"- {Fore.CYAN}{option}")

        for index, called in enumerate(mocked_print.mock_calls):
            self.assertEqual(called.args[0], values_printed[index])

        self.assertEqual(mocked_print.call_count, 3)

    @patch("builtins.input")
    def test_get_user_option_signup(self, mocked_input):
        self.menu.validate_user_option = MagicMock(return_value="Signup")
        result = self.menu.get_user_option()

        self.assertTrue(result)
        self.assertIsInstance(result, Signup)
        mocked_input.assert_called_once()
        self.menu.validate_user_option.assert_called_once()

    @patch("builtins.input")
    def test_get_user_option_signup_wrong(self, mocked_input):
        self.menu.validate_user_option = MagicMock(return_value=False)
        result = self.menu.get_user_option()

        self.assertFalse(result)
        self.menu.validate_user_option.assert_called_once()
        mocked_input.assert_called_once()

    @patch("builtins.input")
    def test_get_user_option_login(self, mocked_input):
        self.menu.validate_user_option = MagicMock(return_value="Login")
        result = self.menu.get_user_option()

        self.assertTrue(result)
        self.assertIsInstance(result, Login)
        self.menu.validate_user_option.assert_called_once()
        mocked_input.assert_called_once()

    @patch("builtins.input", return_value="log in")
    def test_get_user_option_login_wrong(self, mocked_input):
        self.menu.validate_user_option = MagicMock(return_value=False)
        result = self.menu.get_user_option()

        self.assertFalse(result)
        self.menu.validate_user_option.assert_called_once()
        mocked_input.assert_called_once()

    @patch("builtins.print")
    def test_validate_user_option_signup(self, mocked_print):
        validated = self.menu.validate_user_option("signup")

        self.assertEqual(validated, "Signup")
        mocked_print.assert_not_called()

    @patch("builtins.print")
    def test_validate_user_option_login(self, mocked_print):
        validated = self.menu.validate_user_option("login")
        self.assertEqual(validated, "Login")
        mocked_print.assert_not_called()

    @patch("builtins.print")
    def test_validate_user_option_wrong_option(self, mocked_print):
        validated = self.menu.validate_user_option("abcd")

        self.assertFalse(validated)
        mocked_print.assert_called_once()
        mocked_print.assert_called_once_with(Fore.RED + "Option not available.")
