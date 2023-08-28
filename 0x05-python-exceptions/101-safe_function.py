#!/usr/bin/python3
import sys
""" function that executes a function safely """


def safe_function(fct, *args):
    try:
        return (fct(*args))
    except Exception as e:
        print("Exception: ".format(e), file=sys.stderr)
        return (None)
