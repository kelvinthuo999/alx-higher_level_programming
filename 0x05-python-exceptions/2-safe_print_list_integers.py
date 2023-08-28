#!/usr/bin/python3
""" function to print x integer elements in a list """


def safe_print_list_integers(my_list=[], x=0):
    printed_elements = 0
    try:
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                printed_elements += 1
            except (ValueError, TypeError):
                pass
    except (IndexError):
        pass
    finally:
        print()
    return (printed_elements)
