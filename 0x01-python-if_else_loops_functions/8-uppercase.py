#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        x = ord(letter)
        if  x >= 97 and x <= 122:
            x = x - 32
        print("{:c}".format(x), end='')
    print()
