#!/usr/bin/python3
""" function that deletes keys with specific values """


def complex_delete(a_dictionary, value):
    keys_delete = []
    for key, val in a_dictionary.items():
        if val == value:
            keys_delete.append(key)

    for key in keys_delete:
        del a_dictionary[key]

    return (a_dictionary)
