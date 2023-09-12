#!/usr/bin/python3
""" function that inserts a line of  text """


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text into a file after each line containing a specific string.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each line.
        new_string (str): The string to insert after lines containing the search string.

    Returns:
        None
    """
    # Open the input file and create a temporary output file
    with open(filename, 'r', encoding='utf-8') as file, open('temp_file.txt', 'w', encoding='utf-8') as temp_file:
        for line in file:
            temp_file.write(line)
            if search_string in line:
                temp_file.write(new_string + '\n')

    # Replace the original file with the modified file
    import os
    os.replace('temp_file.txt', filename)
