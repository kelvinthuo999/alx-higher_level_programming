#!/usr/bin/python3
# Check if the script is being run as the main program
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    # set values to specific variables
    a = 10
    b = 5

    # print values and perform respective arithmetic operation
    print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
    print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))
    print('{:d} * {:d} = {:d}'.format(a, b, mul(a, b)))
    print('{:d} / {:d} = {:d}'.format(a, b, div(a, b)))
