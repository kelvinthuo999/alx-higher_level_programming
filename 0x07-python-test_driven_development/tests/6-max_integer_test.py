#!/usr/bin/python3
""" unittests for the function def max_integer(list=[]): """


import unittest
from my_module import max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        # Test when the list has positive integers
        result = max_integer([1, 3, 2, 4, 5])
        self.assertEqual(result, 5)

        # Test when the list has negative integers
        result = max_integer([-1, -3, -2, -4, -5])
        self.assertEqual(result, -1)

        # Test when the list has mixed positive and negative integers
        result = max_integer([-1, 3, -2, 4, -5])
        self.assertEqual(result, 4)

        # Test when the list has a single element
        result = max_integer([42])
        self.assertEqual(result, 42)

        # Test when the list is empty, it should raise a ValueError
        with self.assertRaises(ValueError):
            max_integer([])

        # Test when the list is a mix of integers and non-integers
        with self.assertRaises(TypeError):
            max_integer([1, 'a', 2, 'b', 3])


if __name__ == '__main__':
    unittest.main()
