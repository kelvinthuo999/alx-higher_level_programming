#!/usr/bin/python3

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Import the 'add' function from the 'add_0' module
    from add_0 import add

    # Assign values to respective variables
    a = 1
    b = 2

    # Use string to print the values and result for the addition
    print('{:d} + {:d} = {:d}' .format(a, b, add(a, b)))
