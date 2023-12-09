#!/usr/bin/python3
""" unit test for Review """
import unittest
from models.place import Place
from datetime import datetime


class PlaceTestCase(unittest.TestCase):
    """ class for place test """

    def test_place(self):
        """check attributes exist and types"""
        P = Place()
        self.assertTrue(hasattr(P, "id"))
        self.assertIsInstance(P.id, str)
        self.assertTrue(hasattr(P, "created_at"))
        self.assertIsInstance(P.created_at, datetime)
        self.assertTrue(hasattr(P, "updated_at"))
        self.assertIsInstance(P.updated_at, datetime)
        self.assertTrue(hasattr(P, "city_id"))
        self.assertIsInstance(P.city_id, str)
        self.assertTrue(hasattr(P, "user_id"))
        self.assertIsInstance(P.user_id, str)
        self.assertTrue(hasattr(P, "name"))
        self.assertIsInstance(P.name, str)
        self.assertTrue(hasattr(P, "description"))
        self.assertIsInstance(P.description, str)
        self.assertTrue(hasattr(P, "number_rooms"))
        self.assertIsInstance(P.number_rooms, int)
        self.assertTrue(hasattr(P, "number_bathrooms"))
        self.assertIsInstance(P.number_bathrooms, int)
        self.assertTrue(hasattr(P, "max_guest"))
        self.assertIsInstance(P.max_guest, int)
        self.assertTrue(hasattr(P, "price_by_night"))
        self.assertIsInstance(P.price_by_night, int)
        self.assertTrue(hasattr(P, "latitude"))
        self.assertIsInstance(P.latitude, float)
        self.assertTrue(hasattr(P, "longitude"))
        self.assertIsInstance(P.longitude, float)
        self.assertTrue(hasattr(P, "amenity_ids"))
        self.assertIsInstance(P.amenity_ids, list)


if __name__ == '__main__':
    unittest.main()