#!/usr/bin/python3
import sys
""" function that executes a function safely """


def safe_function(fct, *args):
    try:
        ans = fct(*args)
        return (ans)
    except Exception as e:
        print("Exception: {} ".format(e), file=sys.stderr)
        return (None)
