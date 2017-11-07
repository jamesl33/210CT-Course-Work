#!/usr/bin/python3

from diagonals import *
import unittest

class UnitTest(unittest.TestCase):
    def test_smallest_sum_in_middle(self):
        array = np.zeros((4, 4), int)
        for i in range(len(array)):
            for j in range(len(array)):
                array[i][j] = 1

        array[0][0] = 0
        array[1][1] = 0
        array[2][2] = 0
        array[3][3] = 0

        self.assertEqual(smallest_sum_in_middle(array, 2), 0)

    def test_complete(self):
        array = np.zeros((4, 4), int)
        diagonals = get_all_but_middle(array, 2)

        for i in range(len(diagonals)):
            diagonals[i] = sum(diagonals[i])

        diagonals.append(smallest_sum_in_middle(array, 2))

        self.assertEqual(min(diagonals), 0)

if __name__ == '__main__':
    unittest.main()
