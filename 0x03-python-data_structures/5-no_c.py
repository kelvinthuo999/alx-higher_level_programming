#!/usr/bin/python3
""" remove the characters c and C """


def no_c(my_string):
    if my_string is None:
        return None
    else:
        copy_str = ''
        for char in my_string:
            if char != 'C' and char != 'c':
                copy_str += char
        return (copy_str)
