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
