#!/usr/bin/python3
""" function to print x elements of a list """


def safe_print_list(my_list=[], x=0):
    elements_printed = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            elements_printed += 1
    except IndexError:
        pass
    finally:
        print()
    return (elements_printed)
