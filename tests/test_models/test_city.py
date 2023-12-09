#!/usr/bin/python3
"""city testing module"""
import unittest
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    """tests for city class"""
    def test_city(self):
        """check attributes exist and types"""
        ct = City()
        self.assertTrue(hasattr(ct, "id"))
        self.assertIsInstance(ct.id, str)
        self.assertTrue(hasattr(ct, "created_at"))
        self.assertIsInstance(ct.created_at, datetime)
        self.assertTrue(hasattr(ct, "updated_at"))
        self.assertIsInstance(ct.updated_at, datetime)
        self.assertTrue(hasattr(ct, "state_id"))
        self.assertIsInstance(ct.state_id, str)
        self.assertTrue(hasattr(ct, "name"))
        self.assertIsInstance(ct.name, str)     


if __name__ == "__main__":
    unittest.main()
