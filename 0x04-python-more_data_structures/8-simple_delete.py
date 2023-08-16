#!/usr/bin/python3
""" function to delete a key in a dictionary """


def simple_delete(a_dictionary, key=""):
    a_dictionary.discard(key)
