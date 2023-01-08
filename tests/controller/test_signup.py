from pathlib import Path
from threading import Thread
import unittest
from unittest.mock import patch
from main.signup import Signup



class TestSignup(unittest.TestCase):

    def setUp(self) -> None:
        self.signup = Signup()

    def test_initialize(self):
        pass

    def test_validate_email(self):
        with patch("main.signup.input") as mocked_input:
            mocked_input.side_effect = [
                "ad.hotmail.com",
                "other.-@.com",
                "testing@fake-email.com",
            ]
            email = self.signup.validate_email("1234")
            self.assertEqual(email, "testing@fake-email.com")

    def test_validate_email_strip(self):
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

    @patch("main.signup.print")
    @patch("main.signup.input", return_value="testing1@hotmail.com")
    def test_validate_email_exists(self, mocked_input, mocked_print):
        user = {
            "email": "testing@hotmail.com",
            "age": 23,
            "password": "randompassword"
        }
        self.signup.db.create_user(**user)

        self.assertEqual(self.signup.validate_email(user["email"]), "testing1@hotmail.com")

    def test_validate_age(self):
        with patch("main.signup.input") as mocked_input:
            mocked_input.side_effect = ["123", "a2s", "2e", "000", "10"]
            age = self.signup.validate_age("1234")
            self.assertEqual(age, "10")

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

    
    @patch("main.password.Password.hash_password", return_value="password123.")
    @patch("main.signup.getpass", side_effect=["password123.", "password123."])
    def test_validate_password(self, mocked_getpass, mocked_hashed_password):
        self.assertEqual(self.signup.validate_password(), "password123.")

    @patch("main.signup.print")
    @patch("main.password.Password.hash_password", return_value="password123.")
    @patch("main.signup.getpass", side_effect=["password123.", "password123", "password123.", "password123."])
    def test_validate_password_mismatch(self, mocked_getpass, mocked_hashed_password, mocked_print):
        self.assertEqual(self.signup.validate_password(), "password123.")

    @patch("main.signup.print")
    @patch("main.password.Password.hash_password", return_value="12345678")
    @patch("main.signup.getpass", side_effect=["1234567", "1234567", "12345678", "12345678"])
    def test_validate_password_short_length(self, mocked_getpass, mocked_hashed_password, mocked_print):
        self.assertEqual(self.signup.validate_password(), "12345678")
