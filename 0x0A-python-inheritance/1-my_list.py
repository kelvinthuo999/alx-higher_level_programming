#!/usr/bin/python3
"""
    definition of a class MyList
    that inherits from class list
"""


class MyList(list):
    """ a class that inherits from base class list """
    def print_sorted(self):
        """
        Prints the elements of the list in ascending order
        """
        new_list = sorted(self)
        print(new_list)
