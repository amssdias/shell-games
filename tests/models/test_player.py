import unittest
from unittest.mock import patch

import models
from models.abstract import DB
from models.csv_model import CSVDB
from models.player import Player


class TestPlayer(unittest.TestCase):

    @patch.object(models.csv_model.CSVDB, "save_user")
    @patch("models.player.input", side_effect=["testing", "20", "testing@fakeemail.com"])
    def setUp(self, mocked_input, mocked_save_user) -> None:
        self.db = CSVDB()
        self.player = Player(self.db)

    def test_initialize(self):
        player_initial_variables = self.player.__dict__.keys()
        self.assertIn("name", player_initial_variables)
        self.assertIn("age", player_initial_variables)
        self.assertIn("email", player_initial_variables)
        self.assertIn("db", player_initial_variables)

        self.assertIsInstance(self.player.name, str)
        self.assertIsInstance(self.player.age, str)
        self.assertIsInstance(self.player.email, str)
        self.assertIsInstance(self.player.db, DB)

        self.assertEqual(self.player.name, "testing")
        self.assertEqual(self.player.age, "20")
        self.assertEqual(self.player.email, "testing@fakeemail.com")
        self.assertEqual(self.player.db, self.db)

    def test_validate_name(self):
        name = "testing-name"
        self.assertEqual(self.player.validate_name("testing-name"), name)

    def test_validate_name_strip(self):
        name = "testing-name"
        self.assertEqual(self.player.validate_name("testing-name  "), name)
        self.assertEqual(self.player.validate_name("  testing-name  "), name)
        self.assertEqual(self.player.validate_name("  testing-name"), name)

    def test_validate_name_exception(self):
        names = [1234, ["testing"], {"testing"}, {"name": "testing"}]

        for name in names:
            with self.assertRaises(TypeError) as msg:
                self.player.validate_name(name)
            self.assertEqual(str(msg.exception), f"Input {name} must be a str.")
        
    def test_validate_age(self):
        with patch("models.player.input") as mocked_input:
            mocked_input.side_effect = ["123", "a2s", "2e", "000", "10"]
            age = self.player.validate_age("1234")
            self.assertEqual(age, "10")

    def test_validate_age_strip(self):
        age = "20"
        self.assertEqual(self.player.validate_age("  20"), age)
        self.assertEqual(self.player.validate_age("20  "), age)
        self.assertEqual(self.player.validate_age("  20  "), age)

    def test_validate_age_exception(self):
        ages = [1234, ["testing"], {"testing"}, {"name": "testing"}]
        for age in ages:
            with self.assertRaises(TypeError) as msg:
                self.player.validate_age(age)
            self.assertEqual(str(msg.exception), f"Input {age} must be a str.")

    def test_validate_email(self):
        with patch("models.player.input") as mocked_input:
            mocked_input.side_effect = ["ad.hotmail.com", "other.-@.com", "testing@fake-email.com"]
            email = self.player.validate_email("1234")
            self.assertEqual(email, "testing@fake-email.com")

    def test_validate_email_strip(self):
        self.assertEqual(self.player.validate_email("testing@fake-email.com  "), "testing@fake-email.com")
        self.assertEqual(self.player.validate_email("  testing@fake-email.com"), "testing@fake-email.com")
        self.assertEqual(self.player.validate_email("  testing@fake-email.com  "), "testing@fake-email.com")

    def test_validate_email_exception(self):
        emails = [1234, ["testing@fake-email.com"], {"testing@fake-email.com"}, {"email": "testing@fake-email.com"}]

        for email in emails:
            with self.assertRaises(TypeError) as msg:
                self.player.validate_email(email)
            self.assertEqual(str(msg.exception), f"Input {email} must be a str.")