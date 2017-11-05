#!/usr/bin/python3

import numpy as np

def create_array(n):

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

def sum_n_in_list(lst, n):
    total = 0
    for num in lst:
        if num == n:
            total += num
    return total

def find_smallest_in_list(lst):
    newLst = []
    for i in lst:
        if i != 0:
            newLst.append(i)
    lst = newLst

    try:
        smallest = lst[0]
    except IndexError:
        print("This is not the value your looking for... (Value doesnt appear to be in any diagonals)")
        exit()

    for num in lst:
        if num < smallest:
            smallest = num
    return smallest

def main(n, m):
    diagonals = []
    array = np.random.random_integers(1, 9, size=(n, n))
    print(array, "\n")

    for i in range(-(len(array) - 1), (len(array))):
        diagonals.append(get_diagonal(array, i))

    sumInDiagonals = []

    for diagonal in diagonals:
        sumInDiagonals.append(sum_n_in_list(diagonal, m))

    print("Sum of m in each diagonal {0}".format(sumInDiagonals))
    print("The smallest sum of {0} in any diagonal is {1}".format(m, find_smallest_in_list(sumInDiagonals)))

main(4, 2)
