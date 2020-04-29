#!/usr/bin/python3
def pow(a, b):
    sum = 0
    while b > 0:
        sum = a * a
        b = b - 1
    return sum
