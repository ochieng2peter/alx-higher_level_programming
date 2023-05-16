#!/usr/bin/python3

a, b = 89, 10
a, b = b ^ (a ^ b), a ^ b ^ (a ^ b)
print("a={:d} - b={:d}".format(a, b))
