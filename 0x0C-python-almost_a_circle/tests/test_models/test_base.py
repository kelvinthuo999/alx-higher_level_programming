#!/usr/bin/python3
"""Unittests for Base class"""
import os
import sys
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

if __name__ == "__main__":
    unittest.main()
