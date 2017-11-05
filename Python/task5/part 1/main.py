#!/usr/bin/python3

from set_finding import *

array = create_array(8, 8)
numberSet = find_largest_set(array) # gets the list of number sets in the matrix (create array arguments are interchangeable)

for i in range(len(numberSet)):
    if len(numberSet[i]) == 0:
        print("There are no sets of numbers in this matrix")
    print("{0}. Number/Color = {1}\n   Set = {2}\n".format(i + 1, array[numberSet[i][0][0]][numberSet[i][0][1]], numberSet[i]))
