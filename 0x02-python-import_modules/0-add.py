#!/usr/bin/python3
# Check if the script is being run as the main program
if __name__ == "__main__":
    from add_0 import add

    # Assign values to variables for addition
    a = 1
    b = 2
    print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
