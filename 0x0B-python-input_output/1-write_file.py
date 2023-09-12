#!/usr/bin/python3
""" function to write a string to a text file """


def write_file(filename="", text=""):
    """
    This function writes a string to a text file
    and returns the number of characters written.
    Args:
        filename (str): The name of the file to write to.
        text (str): The text to be written to the file.
    Returns:
        int: The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        num_chars_written = file.write(text)
    return num_chars_written
