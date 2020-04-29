#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = abs(number) % 10

if x <= 0:
        x = x * -1

if x > 5:
        str = "greater than 5"
elif x == 0:
        str = "0"
else:
        str = "less than 6 and not 0"

print("Last digit of {:d} is {:d} and is {:s}".format(number, x, str))
