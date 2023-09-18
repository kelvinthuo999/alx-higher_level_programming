#!/usr/bin/python3
"""Unittest for Rectangle class"""
import os
import sys
import unittest
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.r1 = Rectangle(10, 2, 1, 9)
        self.r2 = Rectangle(2, 4)
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_init(self):
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r1.x, 1)
        self.assertEqual(self.r1.y, 9)
        self.assertEqual(self.r1.id, 5)

        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r2.height, 4)
        self.assertEqual(self.r2.x, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r2.id, 6)

    def test_area(self):
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r2.area(), 8)

    def test_str(self):
        self.assertEqual(str(self.r1), "[Rectangle] (7) 1/9 - 10/2")
        self.assertEqual(str(self.r2), "[Rectangle] (8) 0/0 - 2/4")

    def test_update_kwargs(self):
        self.r2.update(id=89)
        self.assertEqual(str(self.r2), "[Rectangle] (89) 0/0 - 2/4")

        self.r2.update(width=3, id=89)
        self.assertEqual(str(self.r2), "[Rectangle] (89) 0/0 - 3/4")

        self.r2.update(height=5, width=3, id=89)
        self.assertEqual(str(self.r2), "[Rectangle] (89) 0/0 - 3/5")

        self.r2.update(x=6, height=5, width=3, id=89)
        self.assertEqual(str(self.r2), "[Rectangle] (89) 6/0 - 3/5")

        self.r2.update(y=7, x=6, height=5, width=3, id=89)
        self.assertEqual(str(self.r2), "[Rectangle] (89) 6/7 - 3/5")

    def test_update_args_kwargs(self):
        self.r1.update(89, 2, 3, 4, 5, id=90, width=6)
        self.assertEqual(
                str(self.r1),
                "[Rectangle] (89) 4/5 - 2/3"
        )

    def test_to_dictionary(self):
        r1_dict = self.r1.to_dictionary()
        self.assertEqual(
                r1_dict,
                {'id': 9, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        )

        r2_dict = self.r2.to_dictionary()
        self.assertEqual(
                r2_dict,
                {'id': 10, 'width': 2, 'height': 4, 'x': 0, 'y': 0}
        )


if __name__ == '__main__':
    unittest.main()
