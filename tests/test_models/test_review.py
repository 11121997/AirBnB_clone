#!/usr/bin/python3
import unittest
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    ''' Review Tests '''

    def test_review(self):
        ''' check attributes exist and types '''
        rv = Review()
        self.assertTrue(hasattr(rv, 'id'))
        self.assertIsInstance(rv.id, str)
        self.assertTrue(hasattr(rv, "created_at"))
        self.assertIsInstance(rv.created_at, datetime)
        self.assertTrue(hasattr(rv, "updated_at"))
        self.assertIsInstance(rv.updated_at, datetime)
        self.assertTrue(hasattr(rv, "place_id"))
        self.assertIsInstance(rv.place_id, str)
        self.assertTrue(hasattr(rv, "user_id"))
        self.assertIsInstance(rv.user_id, str)
        self.assertTrue(hasattr(rv, "text"))
        self.assertIsInstance(rv.text, str)

    if __name__ == "__main__":
        unittest.main()
