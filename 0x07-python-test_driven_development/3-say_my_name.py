#!/usr/bin/python3
""" function to print name """


def say_my_name(first_name, last_name=""):
    """
    Prints a message containing the first name and optionally the last name.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name (default is an empty string).

    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string.
    """
    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    # Print the message based on whether last_name is provided
    if last_name:
        print(f"My name is {first_name} {last_name}.")
    else:
        print(f"My name is {first_name}.")
