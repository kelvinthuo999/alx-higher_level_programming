#!/usr/bin/python3
""" print the elements of a list in reverse """


def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for num in my_list:
        print('{:d}'.format(num))
