#!/usr/bin/python3
""" function to return a dictionary description """


def class_to_json(obj):
    """
    Convert an object's attributes into a serializable dictionary.
    Args:
        obj: An instance of a class with serializable attributes.
    Returns:
        dict: A dictionary representation of the object.
    """
    # Get all attributes of the object
    attributes = dir(obj)

    # Create a dictionary to store the attributes and their values
    obj_dict = {}

    for attr_name in attributes:
        # Check if the attribute is not a special method or attribute
        if not attr_name.startswith("__"):
            attr_value = getattr(obj, attr_name)
            # Check if the attribute value is serializable
            if isinstance(attr_value, (list, dict, str, int, bool)):
                obj_dict[attr_name] = attr_value

    return obj_dict
