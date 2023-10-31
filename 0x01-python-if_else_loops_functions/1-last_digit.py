#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
last_number = abs(number) % 10
if number < 0:
    last_number = last_number * -1 
if last_number > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number,last_number))
elif last_number == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number,last_number))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number,last_number))
