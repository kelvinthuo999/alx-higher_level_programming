#!/usr/bin/python3
""" definition of class Base """
import json

class Base:
    """Base class for managing id attribute."""

    # Private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor for Base.
        Args:
            id (int, optional): The ID for the Base object. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # Static method to return JSON string representation of a list of dictionaries
    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: A JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    # Class method to save instances to a file as JSON
    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of instances to a file in JSON format.

        Args:
            list_objs (list): A list of instances.

        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as file:
            json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            file.write(json_string)

    # Static method to return a list of dictionaries from a JSON string
    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): A JSON string representing a list of dictionaries.

        Returns:
            list: A list of dictionaries.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    # Class method to create an instance with attributes from a dictionary
    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes from a dictionary.

        Args:
            **dictionary: Keyword arguments representing the attributes.

        Returns:
            Base: An instance with attributes set based on the provided dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy = cls(1)  # Create a dummy Square instance
        else:
            dummy = None
        dummy.update(**dictionary)  # Update the dummy instance with the provided dictionary
        return dummy

    # Class method to load instances from a JSON file and return a list of instances
    @classmethod
    def load_from_file(cls):
        """Load instances from a JSON file and return a list of instances.

        Returns:
            list: A list of instances.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                instances = [cls.create(**dictionary) for dictionary in dictionaries]
                return instances
        except FileNotFoundError:
            return []
