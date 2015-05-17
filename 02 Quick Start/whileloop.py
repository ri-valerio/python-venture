#!/usr/bin/python3

# simple fibonacci series
# the sum of two elements defines the next set
a, b = 0, 1

while b < 50:
    print(b)
    a, b = b, a + b
    # it is not the same if the use the attribution below
    # a = b
    # b = a + b
