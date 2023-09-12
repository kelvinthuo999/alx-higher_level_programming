#!/usr/bin/python3
""" function to save an object to a text file """
import json


def save_to_json_file(my_obj, filename):
    """
    function saves an object to a text file
    using its JSON representation.
    Args:
        my_obj: The Python object to be serialized to JSON and saved.
        filename (str): name of the file
        to save the JSON representation to.
    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
