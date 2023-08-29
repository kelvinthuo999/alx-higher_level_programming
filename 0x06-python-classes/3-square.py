#!/usr/bin/python3
""" Definition of a square """


class Square:
    """
    This class defines a square.
    Attributes:size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.
        Args:size (int, optional): The size of the square. Defaults to 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.
        Returns:int: The area of the square.
        """
        return (self.__size ** 2)
