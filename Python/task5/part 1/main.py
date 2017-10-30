#!/usr/bin/python3

import numpy as np

def check_if_set(array, x, y, visited=[]):
    """ Recursive method to check if the position (x, y) is included in a set. Returns empty list if there isn't a set of numbers """
    neighbours = check_neighbours(array, x, y)
    for i, j in neighbours:
        if (i, j) not in visited:
            visited.append((i, j))
            check_if_set(array, i, j, visited)
    return visited

def check_neighbours(array, x, y):
    """ Returns a list of direct neighbors with the same color as pos (x, y) """
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
    """ Method to get all sets of colors in the matrix. This includes empty sets which will are removed in "find_largest_set" """
    allSets = []
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            allSets.append(check_if_set(array, i, j, []))
    return allSets

def find_largest_set(array):
    """ Uses list from "get_all_sets" and finds the largest set of numbers next to each other in the matrix
    if there is multiple sets which are the largest they will all be returned. Returns a list of lists containing tuples of x y coordinates """
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
    """ Helper function to create the array and print it. Needed due to the fact that the array is full or pseudo random data
    and we need to be able to see the array to know if the output is correct """
    array = np.random.random_integers(1, 9, size=(n, m))
    print("{0}\n".format(array))
    return array

################# Labsheet Main ################# Comment out code inside of 'Labsheet Main' when running unit test

array = create_array(8, 8)
numberSet = find_largest_set(array) # gets the list of number sets in the matrix (create array arguments are interchangeable)

for i in range(len(numberSet)):
    if len(numberSet[i]) == 0:
        print("There are no sets of numbers in this matrix")
    print("{0}. Number/Color = {1}\n   Set = {2}\n".format(i + 1, array[numberSet[i][0][0]][numberSet[i][0][1]], numberSet[i]))

################# Labsheet Main #################

################# Unit Test ################# Uncomment code inside of 'Unit Test' when unit testing

# import unittest

# class UnitTest(unittest.TestCase):
#     def test_check_neighbours(self):
#         # left
#         array = np.zeros((4, 4), int)
#         array[1][1] = 1
#         array[1][0] = 1

#         self.assertEqual(check_neighbours(array, 1, 1), [(1, 0)])

#         # right
#         array = np.zeros((4, 4), int)
#         array[1][1] = 1
#         array[1][2] = 1

#         self.assertEqual(check_neighbours(array, 1, 1), [(1, 2)])

#         # above
#         array = np.zeros((4, 4), int)
#         array[1][1] = 1
#         array[0][1] = 1

#         self.assertEqual(check_neighbours(array, 1, 1), [(0, 1)])

#         # below
#         array = np.zeros((4, 4), int)
#         array[1][1] = 1
#         array[2][1] = 1

#         self.assertEqual(check_neighbours(array, 1, 1), [(2, 1)])

#     def test_check_if_set(self):
#         array = np.zeros((4, 4), int)
#         array[1][1] = 1
#         array[0][1] = 1
#         array[2][1] = 1
#         array[1][2] = 1
#         array[1][0] = 1

#         returnedValue = check_if_set(array, 1, 1)
#         returnedValue.sort()

#         correct = [(0, 1), (1, 1), (2, 1), (1, 0), (1, 2)]
#         correct.sort()

#         self.assertEqual(returnedValue, correct)

#     def test_find_largest_set(self):
#         array = np.zeros((4, 4), int)

#         array[1][1] = 1
#         array[0][1] = 1
#         array[2][1] = 1
#         array[1][2] = 1
#         array[1][0] = 1

#         self.assertEqual(find_largest_set(array), [[(0, 2), (0, 3), (1, 3), (2, 0), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]])

#         array = np.zeros((4, 4), int)

#         for i in range(array.shape[0]):
#             for j in range(array.shape[1]):
#                 array[i][j] = 1

#         self.assertEqual(find_largest_set(array), [[(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]])

# if __name__ == '__main__':
#     unittest.main()

################# Unit Test #################
