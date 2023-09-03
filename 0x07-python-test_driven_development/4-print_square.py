#!/usr/bin/python3
""" function to print a square with # """


def print_square(size):
    """
    Prints a square of a specified size using the '#' character.

    Args:
        size (int): The size length of the square.
    Raises:
        TypeError: If size is not an integer or is a float less than 0.
        ValueError: If size is less than 0.
    """
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    # Check if size is greater than or equal to 0
    if size < 0:
        raise ValueError("size must be >= 0")
    # Print the square
    for i in range(size):
        print("#" * size)
