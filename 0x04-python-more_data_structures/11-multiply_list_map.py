#!/usr/bin/python3
""" function to multiply values by a given number """


def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))
