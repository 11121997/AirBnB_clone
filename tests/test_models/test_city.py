#!/usr/bin/python3
"""city testing module"""
import unittest
from models.city import City


class city_tests(unittest.TestCase):
    """tests for city class"""
    def set_city(self):
        """test for setting city"""
        self.city = City()

    def test_stt_id(self):
        """test for state_id"""
        self.assertEqual(self.city.state_id, "")

    def test_name(self):
        """test for name of city"""
        self.assertEqual(self.city.name, "")


if __name__ == "__main__":
    unittest.main()
