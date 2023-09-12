#!/usr/bin/python3
""" function to append a string to a txt file """


def append_write(filename="", text=""):
    """
    This function appends a string to the end of a text file
    and returns the number of characters added.
    Args:
        filename (str): The name of the file to append to.
        text (str): The text to be appended to the file.
    Returns:
        int: The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        num_chars_added = file.write(text)
    return num_chars_added
