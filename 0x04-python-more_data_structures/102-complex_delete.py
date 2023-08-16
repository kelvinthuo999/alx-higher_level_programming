#!/usr/bin/python3
""" function that deletes keys with specific values """


def complex_delete(a_dictionary, value):
    keys_delete = [key for key, val in a_dictionary.items() if val == value]
    for key in keys_delete:
        del a_dictionary[key]
