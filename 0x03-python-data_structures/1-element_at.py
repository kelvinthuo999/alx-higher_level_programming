#!/usr/bin/python3
""" A function to return element at a certain index """


def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        return my_list[idx]
