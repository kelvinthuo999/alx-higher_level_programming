#!/usr/bin/python3
"""Unittest for Square class"""
import os
import unittest
import sys
from io import StringIO
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    def setUp(self):
        self.s1 = Square(5, 1, 2)
        self.s2 = Square(7, 3)
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_init(self):
        self.assertEqual(self.s1.size, 5)
        self.assertEqual(self.s1.x, 1)
        self.assertEqual(self.s1.y, 2)
        self.assertEqual(self.s1.id, 1)

        self.assertEqual(self.s2.size, 7)
        self.assertEqual(self.s2.x, 3)
        self.assertEqual(self.s2.y, 0)
        self.assertEqual(self.s2.id, 2)

    def test_str(self):
        self.assertEqual(str(self.s1), "[Square] (1) 1/2 - 5")
        self.assertEqual(str(self.s2), "[Square] (2) 3/0 - 7")

    def test_update_args(self):
        self.s1.update(89)
        self.assertEqual(str(self.s1), "[Square] (89) 1/2 - 5")

        self.s1.update(89, 2)
        self.assertEqual(str(self.s1), "[Square] (89) 1/2 - 2")

        self.s1.update(89, 2, 3)
        self.assertEqual(str(self.s1), "[Square] (89) 3/2 - 2")

        self.s1.update(89, 2, 3, 4)
        self.assertEqual(str(self.s1), "[Square] (89) 3/4 - 2")

    def test_update_kwargs(self):
        self.s2.update(id=89)
        self.assertEqual(str(self.s2), "[Square] (89) 3/0 - 7")

        self.s2.update(size=3, id=89)
        self.assertEqual(str(self.s2), "[Square] (89) 3/0 - 3")

        self.s2.update(x=6, size=3, id=89)
        self.assertEqual(str(self.s2), "[Square] (89) 6/0 - 3")

        self.s2.update(y=7, x=6, size=3, id=89)
        self.assertEqual(str(self.s2), "[Square] (89) 6/7 - 3")

    def test_update_args_kwargs(self):
        self.s1.update(89, 2, 3, 4, id=90, size=6)
        self.assertEqual(str(self.s1), "[Square] (89) 3/4 - 2")

    def test_to_dictionary(self):
        s1_dict = self.s1.to_dictionary()
        self.assertEqual(s1_dict, {'id': 1, 'size': 5, 'x': 1, 'y': 2})

        s2_dict = self.s2.to_dictionary()
        self.assertEqual(s2_dict, {'id': 2, 'size': 7, 'x': 3, 'y': 0})


if __name__ == '__main__':
    unittest.main()
