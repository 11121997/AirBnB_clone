#!/usr/bin/python3
""" tests for BaseModel"""
import unittest
import json
from datetime import datetime
from io import StringIO
import sys
from unittest.mock import patch
from models.base_model import BaseModel
import models

captured_output = StringIO()
sys.stdout = captured_output


class TestBaseModel(unittest.TestCase):
    """Test case for the BaseModel class"""

    def setUp(self):
        """Set up the test environment"""
        self.filepath = models.storage._FileStorage__file_path
        with open(self.filepath, 'w') as file:
            file.truncate(0)
        models.storage.all().clear()

    def tearDown(self):
        """Tear down the test environment"""
        printed_output = captured_output.getvalue()
        sys.stdout = sys.__stdout__

    def test_init_method(self):
        """Test the __init__ method of BaseModel"""
        new_inst = BaseModel()

        # Check if it has the required methods
        self.assertTrue(hasattr(new_inst, "__init__"))
        self.assertTrue(hasattr(new_inst, "__str__"))
        self.assertTrue(hasattr(new_inst, "save"))
        self.assertTrue(hasattr(new_inst, "to_dict"))

        # Check existence of attributes and types
        self.assertTrue(hasattr(new_inst, "id"))
        self.assertIsInstance(new_inst.id, str)
        self.assertTrue(hasattr(new_inst, "created_at"))
        self.assertIsInstance(new_inst.created_at, datetime)
        self.assertTrue(hasattr(new_inst, "updated_at"))
        self.assertIsInstance(new_inst.updated_at, datetime)

        # Check if object is saved in storage
        key_name = "BaseModel." + new_inst.id
        self.assertIn(key_name, models.storage.all())
        self.assertIs(models.storage.all()[key_name], new_inst)

        # Test attribute update
        new_inst.name = "My First Model"
        new_inst.my_number = 89
        self.assertTrue(hasattr(new_inst, "name"))
        self.assertTrue(hasattr(new_inst, "my_number"))
        self.assertTrue(hasattr(models.storage.all()[key_name], "name"))
        self.assertTrue(hasattr(models.storage.all()[key_name], "my_number"))

        # Check if save() updates updated_at time
        old_time = new_inst.updated_at
        new_inst.save()
        self.assertNotEqual(old_time, new_inst.updated_at)
        self.assertGreater(new_inst.updated_at, old_time)

        # Check if __init__ calls models.storage.save()
        with patch('models.storage.save') as mock_function:
            obj = BaseModel()
            obj.save()
            mock_function.assert_called_once()

        # Check if object is saved in JSON file
        key_name = "BaseModel." + new_inst.id
        with open(self.filepath, 'r') as file:
            saved_data = json.load(file)
        self.assertIn(key_name, saved_data)
        self.assertEqual(saved_data[key_name], new_inst.to_dict())

    def test_init_with_dict(self):
        """Test initializing a BaseModel with a dictionary"""
        new_inst = BaseModel()
        new_inst.name = "John"
        new_inst.my_number = 89
        new_inst2 = BaseModel(**new_inst.to_dict())

        self.assertEqual(new_inst.id, new_inst2.id)
        self.assertEqual(new_inst.name, "John")
        self.assertEqual(new_inst.my_number, 89)
        self.assertEqual(new_inst.to_dict(), new_inst2.to_dict())

    def test_str_method(self):
        """Test the __str__ method of BaseModel"""
        new_inst = BaseModel()
        self.assertEqual(
            str(new_inst),
            "[BaseModel] ({}) {}".format(new_inst.id, new_inst.__dict__)
        )

        old_time = new_inst.updated_at
        new_inst.save()
        self.assertGreater(new_inst.updated_at, old_time)


if __name__ == '__main__':
    unittest.main()
