#!/usr/bin/python3
""" definition of class Square """


class BaseGeometry:
    """ definition of class BaseGeometry """
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
    """ definition of class Rectangle """
    def __init__(self, width, height):
        """
        Initializes a Rectangle object with width and height attributes.
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

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the Rectangle object.
        Returns:
            str: A string in the format "[Rectangle] <width>/<height>".
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """ definition of class Square """
    def __init__(self, size):
        """
        Initializes a Square object with a validated size attribute.
        Args:
            size (int): The size of the square (positive integer).
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.__size = 0  # Private size attribute
        self.integer_validator("size", size)
        self.__size = size
        # Call the superclass (Rectangle)
        # constructor with size for both width and height
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the Square object.
        Returns:
            str: A string in the format "[Square] <size>/<size>".
        """
        return f"[Square] {self.__size}/{self.__size}"
