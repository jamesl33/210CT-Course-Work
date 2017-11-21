#!/usr/bin/python3
"""unit_test.py: Testing to make sure that the functions from
diagonals.py is working correctly
"""

import unittest
from diagonals import get_all_diagonals, smallest_sum_in_array, get_diagonal


class UnitTest(unittest.TestCase):
    """UnitTest"""
    def test_get_diagonal(self):
        """test_get_diagonal: Make sure test_get_diagonal is working correctly
        """
        array = [[3, 1, 5, 6, 9], [2, 4, 1, 9, 7], [3, 5, 2, 8, 10], [4, 2, 1, 6, 8],
                 [1, 4, 7, 9, 1]]
        self.assertEqual(get_diagonal(array), [3, 4, 2, 6, 1])

    def test_sum_in_array(self):
        """test_sum_in_array: Make sure sum_in_array function is working correctly
        """
        array = [1, 123, 312, 3, 223, 1, 323, 4, 123, 1, 23, 1]
        self.assertEqual(smallest_sum_in_array(array, 4), 4)

    def test_labsheet(self):
        """test_labsheet: Test values given on the labsheet
        """
        array = [[3, 1, 5, 6, 9], [2, 4, 1, 9, 7], [3, 5, 2, 8, 10], [4, 2, 1, 6, 8],
                 [1, 4, 7, 9, 1]]

        diagonals = get_all_diagonals(array, 4)

        for i in range(len(diagonals)):
            diagonals[i] = smallest_sum_in_array(diagonals[i], 4)

        diagonals = min(diagonals)

        self.assertEqual(diagonals, 10)


if __name__ == '__main__':
    unittest.main()
