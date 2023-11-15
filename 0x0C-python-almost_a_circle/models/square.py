#!/usr/bin/python3
""" definition of class Square """
import os
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor for Square.

        Args:
            size (int): The size of the square.
            x (int): x-coordinate of the square's position. Defaults to 0.
            y (int): y-coordinate of the square's position. Defaults to 0.
            id (int): The ID for the Square object. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    # Getter and setter for size
    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square (width and height)."""
        if not isinstance(value, int):
            raise TypeError("width/size must be an integer")
        if value <= 0:
            raise ValueError("width/size must be > 0")
        self.width = value
        self.height = value

    # Override the __str__ method
    def __str__(self):
        """Return a custom string representation of the Square.

        Returns:
            str: A custom string representation of the Square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    # Public method to update attributes using *args or **kwargs
    def update(self, *args, **kwargs):
        """Update Square attributes using positional and keyword arguments.

        Args:
            *args: Positional arguments for id, size, x, and y.
            **kwargs: Keyword arguments for attribute assignments.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    # Public method to return a dictionary representation of the Square
    def to_dictionary(self):
        """Return a dictionary representation of the Square.

        Returns:
            dict: A dictionary containing the attributes of the Square.
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
