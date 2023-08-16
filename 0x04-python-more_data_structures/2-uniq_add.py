#!/usr/bin/python3
""" function to sum unique elements of a list """


def uniq_add(my_list=[]):
    unique_int = set()

    for element in my_list:
        if isinstance(element, int):
            unique_int.add(element)
    total = sum(unique_int)
    return (total)
