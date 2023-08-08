#!/usr/bin/python3
import random
number = random.randint(-10, 10)

# Check the sign of the number
if number > 0:
    # Print a message for positive numbers
    print(f"{number} is positive")
elif number == 0:
    # Print a message for zero
    print(f"{number} is zero")
else:
    # Print a message for negative numbers
    print(f"{number} is negative")
