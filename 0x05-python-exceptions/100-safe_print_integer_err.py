#!/usr/bin/python3
""" function to print an integer """


import sys
def safe_print_integer_err(value):
    try:
        digit = int(value)
        print("{:d}".format(digit))
        return (True)
    except (TypeError, ValueError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return (False)
