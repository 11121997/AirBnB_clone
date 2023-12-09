#!/usr/bin/python3
"""state test module"""
import unittest
from models.state import State


class state_tests(unittest.TestCase):
    """tests for state class"""
    def setter(self):
        """test for setting state"""
        self.state = State()

    def name_test(self):
        """test for name"""
        self.assertEqual(self.state.name, "")


if __name__ == "__main__":
    unittest.main()
