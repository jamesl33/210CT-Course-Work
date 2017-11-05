#!/usr/bin/python3

import numpy as np

def create_array(n):
    array = np.random.random_integers(1, 9, size=(n, n))
    return array

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

def get_diagonals_of_length(array, n):
    arrayVarients = [array, np.fliplr(array), np.fliplr(np.flipud(array)), np.flipud(array)]
    lst = []

    for varient in arrayVarients:
        for i in range(len(array)):
            x = get_diagonal(varient, i)
            if len(x) == n:
                lst.append(x)
    return lst

def get_smallest_diagonal(diagonals):
    lst = []
    for diagonal in diagonals:
        lst.append(sum(diagonal))

    currentLargest = lst[0]
    for value in lst:
        if value < currentLargest:
            currentLargest = value
    return currentLargest

def main(arraySize, diagonalSize):
    array = create_array(arraySize)
    print("{0}\n".format(array))
    diagonals = get_diagonals_of_length(array, diagonalSize)
    print("Diagonals of length {0}: {1}\n".format(diagonalSize, diagonals))
    print("The smallest sum of the diagonals of length {0} is {1}".format(diagonalSize, get_smallest_diagonal(diagonals)))

arraySize = 8
diagonalSize = 6
main(arraySize, diagonalSize)
