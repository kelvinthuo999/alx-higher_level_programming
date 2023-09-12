#!/usr/bin/python3
""" function to return the JSON rep """
import json


def to_json_string(my_obj):
    """
    function returns the JSON rep of an object as a string.
    Args:
        my_obj: The Python object to be serialized to JSON.
    Returns:
        str: The JSON representation of the object as a string.
    """
    json_string = json.dumps(my_obj)
    return json_string
