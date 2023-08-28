#!/usr/bin/python3
""" function that divides two integers """


def safe_print_division(a, b):
    try:
        answer = a / b
    except (ZeroDivisionError):
        answer = None
    finally:
        print("Inside result: {}".format(answer))
        return (answer)
