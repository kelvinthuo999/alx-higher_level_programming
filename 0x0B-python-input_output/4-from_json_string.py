#!/usr/bin/python3
""" function to parse a JSON string """
import json


def from_json_string(my_str):
    """
    function parses a JSON string
    and returns the corresponding Python data structure.
    Args:
        my_str (str): The JSON string to be parsed.
    Returns:
        object: The Python data structure represented by the JSON string.
    """
    python_obj = json.loads(my_str)
    return python_obj
