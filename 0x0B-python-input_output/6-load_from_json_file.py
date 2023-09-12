#!/usr/bin/python3
""" function to load an object from a JSON file """
import json


def load_from_json_file(filename):
    """
    function loads an object from a JSON file.
    Args:
        filename (str): The name of the JSON file to read.
    Returns:
        object: Python object represented by the JSON data in the file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        loaded_obj = json.load(file)
    return loaded_obj
