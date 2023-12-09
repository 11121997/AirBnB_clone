#!/usr/bin/python3
"""User test module"""
import unittest
from models.user import User


class test_User(unittest.TestCase):
    """test cases for user class"""
    def setter(self):
        """test for user"""
        self.user = User()

    def test_E(self):
        """test for email"""
        self.assertEqual(self.user.email, "")

    def test_pass(self):
        """test for password"""
        self.assertEqual(self.user.password, "")

    def test_f_name(self):
        """test for first name"""
        self.assertEqual(self.user.first_name, "")

    def test_l_name(self):
        """test for last name"""
        self.assertEqual(self.user.last_name, "")


if __name__ == "__main__":
    unittest.main()
