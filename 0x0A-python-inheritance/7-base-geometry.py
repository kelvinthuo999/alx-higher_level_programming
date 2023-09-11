#!/usr/bin/python3
""" a class definition that validates integers """


class BaseGeometry:
    """ a class definition that validate integers """
    def area(self):
        """
        Raises an Exception with the message "area() is not implemented."
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value:
        - If value is not an integer, raises a TypeError exception
        with the message "<name> must be an integer."
        - If value is less than or equal to 0,
        raises a ValueError exception with a message.

        Args:
            name (str): The name of the value being validated (a string).
            value: The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
