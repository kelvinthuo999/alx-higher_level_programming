#!/usr/bin/python3
"""Unittests for Base class"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def test_base_id(self):
        """Test if id is correctly assigned"""
        base1 = Base()
        self.assertEqual(base1.id, 1)
        base2 = Base()
        self.assertEqual(base2.id, 2)
        base3 = Base(100)
        self.assertEqual(base3.id, 100)

    def test_to_json_string(self):
        """Test to_json_string method"""
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")
        json_str = Base.to_json_string([{'id': 1}])
        self.assertEqual(json_str, "[{\"id\": 1}]")

    def test_from_json_string(self):
        """Test from_json_string method"""
        from_json = Base.from_json_string("[]")
        self.assertEqual(from_json, [])
        from_json = Base.from_json_string(None)
        self.assertEqual(from_json, [])
        from_json = Base.from_json_string("[{\"id\": 1}]")
        self.assertEqual(from_json, [{"id": 1}])

    def test_create(self):
        """Test create method"""
        dummy_dict = {'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5}
        dummy_instance = Base.create(**dummy_dict)
        self.assertEqual(dummy_instance.id, 1)
        self.assertEqual(dummy_instance.__dict__, dummy_dict)

    def test_save_to_file_csv(self):
        """Test save_to_file_csv method"""
        base1 = Base(1)
        base2 = Base(2)
        base_list = [base1, base2]
        Base.save_to_file_csv(base_list)
        with open("Base.csv", "r") as file:
            data = file.read()
            self.assertTrue("1,1\n2,2" in data)

    def test_load_from_file_csv(self):
        """Test load_from_file_csv method"""
        base_list = Base.load_from_file_csv()
        self.assertEqual(len(base_list), 2)
        self.assertEqual(base_list[0].id, 1)
        self.assertEqual(base_list[1].id, 2)


if __name__ == "__main__":
    unittest.main()
