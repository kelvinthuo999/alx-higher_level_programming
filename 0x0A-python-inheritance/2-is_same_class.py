#!/usr/bin/python3
""" determine if an object is an instance of a class """


def is_same_class(obj, a_class):
    """
    Returns True if the object is an instance of the class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class; otherwise False.
    """
    return type(obj) is a_class
