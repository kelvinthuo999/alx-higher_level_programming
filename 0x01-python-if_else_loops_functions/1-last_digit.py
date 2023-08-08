#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    # Check if 'number' is negative
    last_digit = number % -10
    # If negative, find the remainder of the division of 'number' by -10
    # This will give us the last digit as a negative number
else:
    last_digit = number % 10
    # If positive or zero, find the remainder of the division of 'number' by 10
    # This will give us the last digit

if last_digit > 5:
    # Check if the last digit is greater than 5
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
    # Print the appropriate message if the last digit is greater than 5
elif last_digit == 0:
    # Check if the last digit is 0
    print(f"Last digit of {number} is 0 and is 0")
    # Print the appropriate message if the last digit is 0
else:
    # If the last digit is not greater than 5 or 0, it must be between 1 and 5
    print(f"Last digit of {number} is {last_digit} and is less than 6\
 and not 0")
    # Print the appropriate message if the last digit is between 1 and 5
