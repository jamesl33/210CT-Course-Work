#!/usr/bin/python3
"""unit_test.py: File contains all the unit testing to make sure that the functions
in 'set_finding.py' are correct
"""

import unittest
import numpy as np
from set_finding import check_neighbours, check_if_set, find_largest_set


class UnitTest(unittest.TestCase):
    """UnitTest"""
    def test_check_neighbours(self):
        """test_check_neighbours: Test case the neightbour checking function
        """
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
        """test_check_if_set: Testing check_if_set function is working correctly
        """
        array = np.zeros((4, 4), int)
        array[1][1] = 1
        array[0][1] = 1
        array[2][1] = 1
        array[1][2] = 1
        array[1][0] = 1

        returned_value = check_if_set(array, 1, 1)
        returned_value.sort()

        correct = [(0, 1), (1, 1), (2, 1), (1, 0), (1, 2)]
        correct.sort()

        self.assertEqual(returned_value, correct)

    def test_find_largest_set(self):
        """test_find_largest_set: Test main function which should return any sets of numbers in
        a matrix
        """
        array = np.zeros((4, 4), int)

        array[1][1] = 1
        array[0][1] = 1
        array[2][1] = 1
        array[1][2] = 1
        array[1][0] = 1

        self.assertEqual(find_largest_set(array), [[(0, 2), (0, 3), (1, 3), (2, 0), (2, 2),
                                                    (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]])

        array = np.zeros((4, 4), int)

        for i in range(array.shape[0]):
            for j in range(array.shape[1]):
                array[i][j] = 1

        self.assertEqual(find_largest_set(array), [[(0, 0), (0, 1), (0, 2), (0, 3), (1, 0),
                                                    (1, 1), (1, 2), (1, 3), (2, 0), (2, 1),
                                                    (2, 2), (2, 3), (3, 0), (3, 1), (3, 2),
                                                    (3, 3)]])


if __name__ == '__main__':
    unittest.main()
