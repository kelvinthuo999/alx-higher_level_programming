#!/usr/bin/python3
""" Determine if class is inherited directly or inderictly """


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.
    Args:
        obj: The object to check.
        a_class: The class to compare against.
    Returns:
        True if obj's class is a subclass of a_class; otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
