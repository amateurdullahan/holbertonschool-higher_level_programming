#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = number % 10
if ld > 5:
    print("last digit of {:d} is {:d} \
    and is greater than 5".format(number, ld))
elif ld == 0:
    print("last digit of {:d} is {:d} and is 0".format(number, ld))
else:
    print("last digit of {:d} is {:d} \
    and is less than 6 and not 0".format(number, ld))
