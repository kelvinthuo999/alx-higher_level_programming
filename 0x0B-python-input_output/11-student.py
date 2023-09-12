#!/usr/bin/python3
""" definition of class Student """


class Student:
    """
    Class representing a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance with first_name, last_name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.
        Args:
            attrs (list of str, optional): A list of attribute names
            to include in the dictionary.
                If None, all attributes are included.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            # Include all attributes
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
        else:
            # Include only specified attributes
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student
        instance based on a dictionary rep.
        Args:
            json (dict): A dictionary containing attribute names
            and their values.
        """
        for key, value in json.items():
            setattr(self, key, value)
