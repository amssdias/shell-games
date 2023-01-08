import unittest
from unittest.mock import Mock, patch, MagicMock

from main.signup import Signup
from models.player import Player
from tests.models.utils.testing_db import TestDBJson



class TestSignup(unittest.TestCase):

    def setUp(self) -> None:
        self.signup = Signup()

    def test_initialize(self):
        signup_initial_variables = self.signup.__dict__.keys()
        
        self.assertIn("db", signup_initial_variables)

    def test_run(self):
        player = Player(TestDBJson)
        self.signup.db.create_user = MagicMock()

        self.signup.validate_email = MagicMock(return_value="test@example.com")
        self.signup.validate_age = MagicMock(return_value="22")
        self.signup.validate_password = MagicMock(return_value="mypassword")
        
        with patch("builtins.input", return_value="test@example.com"):
            with patch("getpass.getpass", return_value="password"):
                with patch("builtins.print") as mock_print:
                    result = self.signup.run(player)

        self.assertIsInstance(result, Player)
        self.signup.db.create_user.assert_called_once()
        mock_print.assert_not_called()
        self.assertEqual(player.email, "test@example.com")
        self.assertEqual(player.age, "22")
        self.assertEqual(player.password, "mypassword")

    def test_validate_email(self):
        self.signup.db.user_exists = MagicMock(return_value=False)
        with patch("main.signup.input", return_value="valid@hotmail.com"):
            result = self.signup.validate_email("valid@hotmail.com")

        self.assertEqual(result, "valid@hotmail.com")

    def test_validate_email_strip(self):
        self.signup.db.user_exists = MagicMock(return_value=False)

        self.assertEqual(
            self.signup.validate_email("testing@fake-email.com  "),
            "testing@fake-email.com",
        )
        self.assertEqual(
            self.signup.validate_email("  testing@fake-email.com"),
            "testing@fake-email.com",
        )
        self.assertEqual(
            self.signup.validate_email("  testing@fake-email.com  "),
            "testing@fake-email.com",
        )

    def test_validate_email_exception(self):
        emails = [
            1234,
            ["testing@fake-email.com"],
            {"testing@fake-email.com"},
            {"email": "testing@fake-email.com"},
        ]

        for email in emails:
            with self.assertRaises(TypeError) as msg:
                self.signup.validate_email(email)

            self.assertEqual(str(msg.exception), f"Input {email} must be a str.")

    def test_validate_email_exists(self):
        self.signup.db.user_exists = MagicMock(side_effect=[True, False])
        with patch("builtins.input", return_value="valid@hotmail.com") as mocked_input:
            result = self.signup.validate_email("invalid@hotmail.com")

        self.assertEqual(result, "valid@hotmail.com")
        mocked_input.assert_called_once()

    def test_validate_age(self):
        with patch("builtins.input", return_value="10"):
            result = self.signup.validate_age("10")

            self.assertEqual(result, "10")

    def test_validate_age_invalid_length(self):
        with patch("builtins.input", side_effect=["123", "a2s", "2e", "000", "10"]):
            result = self.signup.validate_age("1234")

            self.assertEqual(result, "10")

    def test_validate_age_strip(self):
        age = "20"
        self.assertEqual(self.signup.validate_age("  20"), age)
        self.assertEqual(self.signup.validate_age("20  "), age)
        self.assertEqual(self.signup.validate_age("  20  "), age)

    def test_validate_age_exception(self):
        ages = [1234, ["testing"], {"testing"}, {"name": "testing"}]
        for age in ages:
            with self.assertRaises(TypeError) as msg:
                self.signup.validate_age(age)

            self.assertEqual(str(msg.exception), f"Input {age} must be a str.")

    @patch("main.signup.getpass", side_effect=["password123.", "password123."])
    def test_validate_password(self, mocked_getpass):
        self.signup.hash_password = MagicMock(return_value="password123.")

        self.assertEqual(self.signup.validate_password(), "password123.")
        self.signup.hash_password.assert_called_once()

    @patch("main.password.Password.hash_password", return_value="password123.")
    @patch("main.signup.getpass", side_effect=["password123.", "password123", "password123.", "password123."])
    def test_validate_password_mismatch(self, mocked_getpass, mocked_hashed_password):
        with patch("builtins.print") as mock_print:
            result = self.signup.validate_password()

        self.assertEqual(result, "password123.")
        mock_print.assert_called_once()

    @patch("main.password.Password.hash_password", return_value="12345678")
    @patch("main.signup.getpass", side_effect=["1234567", "1234567", "12345678", "12345678"])
    def test_validate_password_short_length(self, mocked_getpass, mocked_hashed_password):
        with patch("builtins.print") as mock_print:
            result = self.signup.validate_password()

        self.assertEqual(result, "12345678")
        mock_print.assert_called_once()
