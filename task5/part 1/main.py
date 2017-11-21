#!/usr/bin/python3
"""main.py: File contains the function to generate a random matrix and find the smallest
sum of integers in the diagonals
"""

import numpy as np
from diagonals import get_all_diagonals, smallest_sum_in_array

def main():
    """main"""
    array_size = 8
    diagonal_size = 4
    assert array_size > diagonal_size

    array = np.random.random_integers(1, 9, size=(array_size, array_size))
    diagonals = get_all_diagonals(array, diagonal_size)

    for i in range(len(diagonals)):
        diagonals[i] = smallest_sum_in_array(diagonals[i], diagonal_size)

    print(array)
    print('Answer: {0}'.format(min(diagonals)))

main()
