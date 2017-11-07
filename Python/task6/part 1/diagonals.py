#!/usr/bin/python3

import numpy as np

def get_diagonal(array, offset=0):
    if offset >= len(array) or offset <= -len(array):
        raise ValueError("Offset out of range")

    lst = []

    for i in range(len(array)):
        try:
            if offset > 0:
                lst.append(array[i + offset][i])
            else:
                lst.append(array[i][i + abs(offset)])
        except IndexError:
            pass
    return lst

def get_all_but_middle(array, n):
    diagonals = []
    for i in range(-(len(array) - 1), (len(array))):
        diagonal = get_diagonal(array, i)
        if len(diagonal) != len(array) and len(diagonal) == n:
            diagonals.append(diagonal)
    return diagonals

def smallest_sum_in_middle(array, n):
    diagonal = get_diagonal(array)
    diagonal.sort()
    diagonal = diagonal[:n]
    return sum(diagonal)
