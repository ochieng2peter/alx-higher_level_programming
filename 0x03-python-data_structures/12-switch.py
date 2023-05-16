#!/usr/bin/python3

a, b = 89, 10
a, b = 10, 89 if a == 89 else 89
print("a={:d} - b={:d}".format(a, b))
