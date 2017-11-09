#!/usr/bin/python3

from set_finding import *
import unittest

class UnitTest(unittest.TestCase):
    def test_check_neighbours(self):
        # left
        array = np.zeros((4, 4), int)
        array[1][1] = 1
        array[1][0] = 1

        self.assertEqual(check_neighbours(array, 1, 1), [(1, 0)])

        # right
        array = np.zeros((4, 4), int)
        array[1][1] = 1
        array[1][2] = 1

        self.assertEqual(check_neighbours(array, 1, 1), [(1, 2)])

        # above
        array = np.zeros((4, 4), int)
        array[1][1] = 1
        array[0][1] = 1

        self.assertEqual(check_neighbours(array, 1, 1), [(0, 1)])

        # below
        array = np.zeros((4, 4), int)
        array[1][1] = 1
        array[2][1] = 1

        self.assertEqual(check_neighbours(array, 1, 1), [(2, 1)])

    def test_check_if_set(self):
        array = np.zeros((4, 4), int)
        array[1][1] = 1
        array[0][1] = 1
        array[2][1] = 1
        array[1][2] = 1
        array[1][0] = 1

        returnedValue = check_if_set(array, 1, 1)
        returnedValue.sort()

        correct = [(0, 1), (1, 1), (2, 1), (1, 0), (1, 2)]
        correct.sort()

        self.assertEqual(returnedValue, correct)

    def test_find_largest_set(self):
        array = np.zeros((4, 4), int)

        array[1][1] = 1
        array[0][1] = 1
        array[2][1] = 1
        array[1][2] = 1
        array[1][0] = 1

        self.assertEqual(find_largest_set(array), [[(0, 2), (0, 3), (1, 3), (2, 0), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]])

        array = np.zeros((4, 4), int)

        for i in range(array.shape[0]):
            for j in range(array.shape[1]):
                array[i][j] = 1

        self.assertEqual(find_largest_set(array), [[(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]])

if __name__ == '__main__':
    unittest.main()

################# Unit Test #################
