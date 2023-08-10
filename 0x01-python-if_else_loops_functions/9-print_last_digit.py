#!/usr/bin/python3
"""
Print the Last Digit of a Number

This function calculates and prints the last digit of a given number.
"""


def print_last_digit(number):
    # Calculate the last digit
    last_digit = abs(number) % 1

    # Print the last digit without a newline
    print("{:d}".format(last_digit), end='')

    # Return the last digit
    return last_digit
