import hashlib
import unittest
from unittest.mock import patch

from main.password import Password
from main.settings import SECRET_KEY


class TestLogin(unittest.TestCase):
    @patch.object(Password, "get_hashed_password")
    @patch.object(Password, "salt_password")
    def test_hash_password(self, mock_salt_password, mock_get_hashed):
        password = "mypassword"
        mock_salt_password.return_value = b"mypassword"
        mock_get_hashed.return_value = "mypasswordextra"

        result = Password.hash_password(password)

        self.assertEqual(result, "mypasswordextra")
        mock_salt_password.assert_called_once_with(password)
        mock_get_hashed.assert_called_once()

    def test_salt_password(self):
        password = "password"
        password_salted = str(password + SECRET_KEY).encode("utf-8")

        result = Password.salt_password(password)

        self.assertEqual(result, password_salted)
        self.assertIsInstance(result, bytes)

    def test_get_hashed_password(self):
        password_bytes = b"my_password"
        hash_obj = hashlib.sha256()
        hash_obj.update(password_bytes)

        result = Password.get_hashed_password(password_bytes)

        self.assertEqual(result, hash_obj.hexdigest())
        self.assertIsInstance(result, str)

    @patch.object(Password, "get_hashed_password")
    @patch.object(Password, "salt_password")
    def test_check_password(self, mock_salt_password, mock_get_hashed):
        mock_salt_password.return_value = "password"
        mock_get_hashed.return_value = "hashed_password"

        result = Password.check_password("password", "hashed_password")

        self.assertTrue(result)
        mock_salt_password.assert_called_once_with("password")
        mock_get_hashed.assert_called_once()

    @patch.object(Password, "get_hashed_password")
    @patch.object(Password, "salt_password")
    def test_check_password_wrong(self, mock_salt_password, mock_get_hashed):
        mock_salt_password.return_value = "password"
        mock_get_hashed.return_value = "hashed_password"

        result = Password.check_password("password", "hashed_password_real")

        self.assertFalse(result)
        mock_salt_password.assert_called_once_with("password")
        mock_get_hashed.assert_called_once()
