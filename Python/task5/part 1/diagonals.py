#!/usr/bin/python3

import numpy as np

def get_diagonal(array, offset=0):
    """get_diagonal: Method to get the main diagonal from matrix

    :param array: Matrix of integers
    :param offset: Integer which allows you to offset which diagonal you want to get e.g getting the diagonal above the main one
    """
    assert(offset <= len(array))
    assert(offset >= -len(array))
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

def get_all_diagonals(array, m):
    """get_all_diagonals: Gets all the diagonals in the matrix

    :param array: Matrix of intergers
    :param m: Integer representing the size wanted
    """
    diagonals = []
    for i in range(-(len(array) - 1), (len(array))):
        diagonal = get_diagonal(array, i)
        if len(diagonal) >= m:
            diagonals.append(diagonal)
    return diagonals

def smallest_sum_in_array(array, m):
    """smallest_sum_in_array: gets the smallest sum of m elements in the array

    :param array: List of itegers
    :param m: int representing the amount of elements
    """
    array.sort()
    array = array[:m]
    return sum(array)
