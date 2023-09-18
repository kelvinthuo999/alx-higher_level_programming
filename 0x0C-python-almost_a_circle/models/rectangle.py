#!/usr/bin/python3
""" definition of class Rectangle """
import os
import sys
from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from Base class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor for Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): x-coordinate of the rectangle's position. Defaults to 0.
            y (int): y-coordinate of the rectangle's position. Defaults to 0.
            id (int): ID for the Rectangle object. Defaults to None.
        """
        """ Call the superclass constructor with the provided ID """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """ Getter and setter for width """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # Getter and setter for height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # Getter and setter for x-coordinate
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # Getter and setter for y-coordinate
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    # Public method to display the Rectangle with #
    def display(self):
        """Display the Rectangle instance using # characters."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    # Override the __str__ method
    def __str__(self):
        """Return a custom string representation of the Rectangle.

        Returns:
            str: A custom string representation of the Rectangle.
        """
        return (
                f"[Rectangle] ({self.id}) "
                f"{self.__x}/{self.__y} - {self.__width}/{self.__height}"
                )

    # Public method to update attributes using *args or **kwargs
    def update(self, *args, **kwargs):
        """
        Update Rectangle attributes using positional and keyword arguments.
        Args:
            *args: Positional arguments for id, width, height, x, and y.
            **kwargs: Keyword arguments for attribute assignments.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def area(self):
        """Calculate and return the area of the Rectangle."""
        return self.__width * self.__height

    def to_dictionary(self):
        """Return a dictionary representation of the Rectangle instance.

        Returns:
            dict: A dictionary with the attributes of the Rectangle.
        """
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }
