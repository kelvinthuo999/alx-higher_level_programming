#!/usr/bin/python3
""" function to print a dictionary by ordered keys """


def print_sorted_dictionary(a_dictionary):
    sort_keys = sorted(a_dictionary.keys())

    for key in sort_keys:
        value = a_dictionary.get(key)
        print(f"{key}: {value}")
