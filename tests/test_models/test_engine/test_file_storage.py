#!/usr/bin/python3
"""file storage tests module"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
import json


class filestoragetests(unittest.TestCase):
    """tests for filestorage"""
    def tests_for_attr(self):
        """tests for:
            class attributes:
                1-__file_path
                2-__objects
        """
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))

    def tests_all(self):
        """tests for all  instance method"""
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def tests_new(self):
        """tests for new instance method"""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        dict = storage.all()
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertTrue(key in dict)

    def tests_save(self):
        """tests for save instance method"""
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def tests_reload(self):
        """tests for reload instance method"""
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        obj = storage.all()
        FileStorage._FileStorage__objects = {}
        self.assertNotEqual(obj, FileStorage._FileStorage__objects)
        storage.reload()
        for key, val in storage.all().items():
            self.assertEqual(obj[key].to_dict(), val.to_dict())


if __name__ == '__main__':
    unittest.main()
