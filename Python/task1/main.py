#!/usr/bin/python3

from factorials import *

testValues = [(6, 9), (20, 10000), (6, 27), (20, 1000000)]
for a, b in testValues:
	print(testIfDivides(a, b)[0])

################# Pseudo Code #################

# FACTORIAL(n)
#     IF n = 0
#         RETURN 1
#     ELSE
#         RETURN n * FACTORIAL(n - 1)

# TEST-IF-DEVIDES(a, b)
#     IF a! MOD b = 0
#         RETURN true
#     ELSE
#         RETURN false

################# Pseudo Code #################
