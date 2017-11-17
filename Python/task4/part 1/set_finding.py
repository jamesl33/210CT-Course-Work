#!/usr/bin/python3

import numpy as np

def check_if_set(array, x, y, visited=[]):
    """check_if_set: Recursive method to check if the position (x, y) is included in a set. Returns empty list if there isn't a set of numbers

    :param array: Matrix in which we are checking for sets
    :param x: Int representing x coord
    :param y: Int representing y coord
    :param visited: List containing visited coords
    """
    neighbours = check_neighbours(array, x, y)
    for i, j in neighbours:
        if (i, j) not in visited:
            visited.append((i, j))
            check_if_set(array, i, j, visited)
    return visited

def check_neighbours(array, x, y):
    """check_neighbours:  Returns a list of direct neighbors with the same color as pos (x, y)

    :param array: Matrix
    :param x: Int representing x coord
    :param y: Int representing y coord
    """
    neighbours = []
    if not (x - 1) < 0:
        if array[x - 1][y] == array[x][y]:
            neighbours.append((x - 1, y))

    if not (x + 1) > array.shape[0] - 1:
        if array[x + 1][y] == array[x][y]:
            neighbours.append((x + 1, y))

    if not (y - 1) < 0:
        if array[x][y - 1] == array[x][y]:
            neighbours.append((x, y - 1))

    if not (y + 1) > array.shape[1] - 1:
        if array[x][y + 1] == array[x][y]:
            neighbours.append((x, y + 1))

    return neighbours

def get_all_sets(array):
    """get_all_sets:  Method to get all sets of colors in the matrix. This includes empty sets which will are removed in "find_largest_set"

    :param array: Matrix which we are searching for sets of numbers
    """
    allSets = []
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            allSets.append(check_if_set(array, i, j, []))
    return allSets

def find_largest_set(array):
    """find_largest_set: Uses list from "get_all_sets" and finds the largest set of numbers next to each other in the matrix
    if there is multiple sets which are the largest they will all be returned. Returns a list of lists containing tuples of x y coordinates

    :param array: Matrix which we are finding the largest set in
    """
    sets = []
    currentLargestSet = 0
    for lst in get_all_sets(array):
        if len(lst) > currentLargestSet:
            sets = []
            lst.sort()
            if lst not in sets:
                sets.append(lst)
                currentLargestSet = len(lst)
        elif len(lst) == currentLargestSet:
            lst.sort()
            if lst not in sets:
                sets.append(lst)
    return sets

def create_array(n, m):
    """create_array: Helper function to create the array and print it. Needed due to the fact that the array is full or pseudo random data
    and we need to be able to see the array to know if the output is correct

    :param n: int width of array to be created
    :param m: int height of array to be created
    """
    array = np.random.random_integers(1, 9, size=(n, m))
    print("{0}\n".format(array))
    return array
