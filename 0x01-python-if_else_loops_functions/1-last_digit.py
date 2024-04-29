#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    L = number % -10
else:
    L = number % 10
if L > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, L))
elif L < 6 and L != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, L))
else:
    print("last digit of {:d} is {:d} and is 0".format(number, L))
