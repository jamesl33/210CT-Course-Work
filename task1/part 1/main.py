#!/usr/bin/python3
"""main.py: contains the dirver code the show the working functions from
'factorials.py'
"""

from factorials import test_divides

def main():
    """main: Driver code to show that factorial and divides functions work
    """
    test_values = [(6, 9), (20, 10000), (6, 27), (20, 1000000)]
    for num_a, num_b in test_values:
        print(test_divides(num_a, num_b)[0])

main()
