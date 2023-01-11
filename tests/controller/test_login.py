import unittest
from unittest.mock import MagicMock, patch
from main.login import Login


class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.login = Login()
        self.player = MagicMock()
        self.player.logged = False

    @patch("builtins.input", return_value="test_email@testing.com")
    @patch("main.login.getpass", return_value="password")
    def test_run(self, mock_getpass, mock_input):
        self.login.db = MagicMock()
        self.login.db.user_exists.return_value = {
            "email": "test_email@testing.com",
            "password": "password",
            "age": 20,
            "score": 0,
            "games_played": 1,
        }
        self.login.check_password = MagicMock()

        result = self.login.run(self.player)

        self.assertTrue(self.player.logged)
        self.assertEqual(
            result,
            {
                "email": "test_email@testing.com",
                "password": "password",
                "age": 20,
                "score": 0,
                "games_played": 1,
            },
        )
        self.login.db.user_exists.assert_called_once_with("test_email@testing.com")
        self.login.check_password.assert_called_once_with("password", "password")

    @patch("builtins.print")
    @patch("builtins.input", return_value="test_email@testing.com")
    @patch("main.login.getpass", return_value="password")
    def test_run_user_not_found(self, mock_getpass, mock_input, mock_print):
        self.login.db = MagicMock()
        self.login.db.user_exists.return_value = False
        self.login.check_password = MagicMock()
        result = self.login.run(self.player)

        self.assertFalse(self.player.logged)
        self.assertFalse(result)
        self.login.db.user_exists.assert_called_once_with("test_email@testing.com")
        self.login.check_password.assert_not_called()

    def test_login_user(self):
        self.login.db = MagicMock()
        self.login.db.user_exists.return_value = {"password": "password"}
        self.login.check_password = MagicMock(return_value=True)

        result = self.login.login_user(self.player, "testing@testing.com", "password")

        self.assertTrue(self.player.logged)
        self.assertEqual(result, {"password": "password"})
        self.login.db.user_exists.assert_called_once_with("testing@testing.com")
        self.login.check_password.assert_called_once_with("password", "password")

    @patch("builtins.print")
    def test_login_user_fail(self, mock_print):
        self.login.db = MagicMock()
        self.login.db.user_exists.return_value = False
        self.login.check_password = MagicMock(return_value=True)

        result = self.login.login_user(self.player, "testing@testing.com", "password")

        self.assertFalse(self.player.logged)
        self.assertEqual(result, False)
        self.login.db.user_exists.assert_called_once_with("testing@testing.com")
        self.login.check_password.assert_not_called()
        mock_print.assert_called_once()
