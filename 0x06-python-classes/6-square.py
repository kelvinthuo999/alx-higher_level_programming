#!/usr/bin/python3
""" Definition of a class """


class Square:
    """
    This class defines a square.
    Attributes:__size (int): The size of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.
        Args:size (int, optional): The size defaults to 0.
             position: position of the square
        """
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Getter method for retrieving the size of the square.
        Returns:int: The size of the square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size of the square.
        Args:value (int): The new size for the square.
        Raises:TypeError: If value is not an integer.
               ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.
        Returns:int: The area of the square.
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        Prints a square using the character #
        """
        if self.__size == 0:
            print()
        else:
            height, width = 0, 0
            for height in range(self.__size):
                for width in range(self.__size):
                    print("#", end="")
                print()
