#!/usr/bin/python3
import sys
""" function to print an integer """


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return (False)
