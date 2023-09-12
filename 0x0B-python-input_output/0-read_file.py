#!/usr/bin/python3
""" function to read a file """


def read_file(filename=""):
    """
    This function reads a text file and prints its contents to stdout.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
