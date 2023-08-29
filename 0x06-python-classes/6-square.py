#!/usr/bin/python3
""" Definition of a class """


class Square:
    """
    This class defines a square.
    Attributes:__size (int): The size of the square.
               __position (tuple): The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.
        Args:size (int): The size defaults to 0.
             position (tuple): The position defaults to (0, 0).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter method for retrieving the position of the square.
        Returns:tuple: The position of the square.
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Setter method for setting the position of the square.
        Args:value (tuple): The new position for the square.
        Raises:TypeError: If value is not a tuple of 2 positive integers.
        """
        if type(value) is not tuple or len(value) != 2 or \
                type(value[0]) is not int or type(value[1]) is not int \
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.
        Returns:int: The area of the square.
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        Prints a square using the character #.
        If size is equal to 0, prints an empty line.
        Position should be used to determine spacing.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for height in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
