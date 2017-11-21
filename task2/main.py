#!/usr/bin/python3
"""main.py: Holds the boilerplate code to show that this code solves
the 8 queens problem
"""

from queen import Queen


def main():
    """main: Code to show the 8 queens problem being solved
    """
    for i in range(8):
        solver = Queen(8)
        print("Solution {0} - {1}".format(i + 1, solver.place_queen(i)))


main()
