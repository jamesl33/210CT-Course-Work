#!/usr/bin/python3
"""set_finding.py: Collection of functions which allow you to find sets
of numbers in a matrix of integers
"""

import numpy as np

def check_if_set(array, pos_x, pos_y, visited=[]):
    """check_if_set: Recursive method to check if the position (x, y) is included in a set.

    :param array: Matrix in which we are checking for sets
    :param pos_x: Int representing x coord
    :param pos_y: Int representing y coord
    :param visited: List containing visited coords
    :returns list: List of visited coords
    """
    neighbours = check_neighbours(array, pos_x, pos_y)
    for pos_i, pos_j in neighbours:
        if (pos_i, pos_j) not in visited:
            visited.append((pos_i, pos_j))
            check_if_set(array, pos_i, pos_j, visited)
    return visited

def check_neighbours(array, pos_x, pos_y):
    """check_neighbours:  Returns a list of direct neighbors with the same color as pos (x, y)

    :param array: Matrix
    :param pos_x: Int representing x coord
    :param pos_y: Int representing y coord
    """
    neighbours = []
    if not (pos_x - 1) < 0:
        if array[pos_x - 1][pos_y] == array[pos_x][pos_y]:
            neighbours.append((pos_x - 1, pos_y))

    if not (pos_x + 1) > array.shape[0] - 1:
        if array[pos_x + 1][pos_y] == array[pos_x][pos_y]:
            neighbours.append((pos_x + 1, pos_y))

    if not (pos_y - 1) < 0:
        if array[pos_x][pos_y - 1] == array[pos_x][pos_y]:
            neighbours.append((pos_x, pos_y - 1))

    if not (pos_y + 1) > array.shape[1] - 1:
        if array[pos_x][pos_y + 1] == array[pos_x][pos_y]:
            neighbours.append((pos_x, pos_y + 1))

    return neighbours

def get_all_sets(array):
    """get_all_sets:  Method to get all sets of colors in the matrix.
    This includes empty sets which will are removed in "find_largest_set"

    :param array: Matrix which we are searching for sets of numbers
    """
    all_sets = []
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            all_sets.append(check_if_set(array, i, j, []))
    return all_sets

def find_largest_set(array):
    """find_largest_set: Uses list from "get_all_sets" and finds the largest set of numbers
    next to each other in the matrix if there is multiple sets which are the largest
    they will all be returned.

    :param array: Matrix which we are finding the largest set in
    :returns  list: A list of lists containing tuples of x y coordinates
    """
    sets = []
    current_largest_set = 0
    for lst in get_all_sets(array):
        if len(lst) > current_largest_set:
            sets = []
            lst.sort()
            if lst not in sets:
                sets.append(lst)
                current_largest_set = len(lst)
        elif len(lst) == current_largest_set:
            lst.sort()
            if lst not in sets:
                sets.append(lst)
    return sets

def create_array(size_x, size_y):
    """create_array: Helper function to create the array and print it. Needed due to the fact that
    the array is full or pseudo random data and we need to be able to see the array
    to know if the output is correct

    :param n: int width of array to be created
    :param m: int height of array to be created
    """
    array = np.random.random_integers(1, 9, size=(size_x, size_y))
    print("{0}\n".format(array))
    return array
