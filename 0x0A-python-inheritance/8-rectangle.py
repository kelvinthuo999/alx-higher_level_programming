#!/usr/bin/python3
""" definition of classes BaseGeometry and Rectangle """


class BaseGeometry:
    """ definition of a class BaseGeometry """
    def area(self):
        """
        Raises an Exception with the message "area() is not implemented."
        This method should be overridden by subclasses
        to calculate the area of the geometric shape.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.

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


class Rectangle(BaseGeometry):
    """ definition of a class Rectangle """
    def __init__(self, width, height):
        """
        Initializes Rectangle object with width and height attributes.
        Args:
            width (int): The width of the rectangle (positive integer).
            height (int): The height of the rectangle (positive integer).

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.__width = 0  # Private width attribute
        self.__height = 0  # Private height attribute
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of the Rectangle object.

        Returns:
            str: A string in the format "[Rectangle] width/height".
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
