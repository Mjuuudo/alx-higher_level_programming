#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
if number > 0:
    print("{:d} is positive".format(number))
elif number == 0:
    print("0 is zero")
elif number < 0:
    print("{:d} is negative".format(number))
