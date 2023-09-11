#!/usr/bin/python3
""" Determine if the object is an instance of the inherited class """


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of,
    or if it's an instance of a class
    that inherited from, the specified class; otherwise False.
    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class
        or its subclasses; otherwise False.
    """
    return isinstance(obj, a_class)
