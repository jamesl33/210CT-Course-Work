#!/usr/bin/python3

from factorials import test_divides

def main():
    """main: Driver code to show that factorial and divides functions work
    """
    test_values = [(6, 9), (20, 10000), (6, 27), (20, 1000000)]
    for num_a, num_b in test_values:
        print(test_divides(num_a, num_b)[0])

main()

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
