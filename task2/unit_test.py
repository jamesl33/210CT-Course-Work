#!/usr/bin/python3
"""unit_test.py: Unit testing for the Queen class
"""

import unittest
from queen import Queen

class UnitTest(unittest.TestCase):
    """UnitTest: Unit testing for the 8 queens problem solver
    """
    def test_correct(self):
        """test_correct: Test generated values from solver and make sure that they
        are in the 'known_correct_values' list"""
        known_correct_values = [[0, 4, 7, 5, 2, 6, 1, 3],
                                [1, 3, 5, 7, 2, 0, 6, 4],
                                [2, 0, 6, 4, 7, 1, 3, 5],
                                [3, 0, 4, 7, 1, 6, 2, 5],
                                [4, 0, 3, 5, 7, 1, 6, 2],
                                [5, 0, 4, 1, 7, 2, 6, 3],
                                [6, 0, 2, 7, 5, 3, 1, 4],
                                [7, 1, 3, 0, 6, 4, 2, 5]]

        for i in range(8):
            solver = Queen(8)
            self.assertTrue(solver.place_queen(i) in known_correct_values)

    def test_is_safe(self):
        """test_is_safe: Test to make sure that is_safe function works
        """
        solver = Queen(8)
        solver.board_state = [0]
        self.assertFalse(solver.is_safe(0, 1))
        self.assertFalse(solver.is_safe(1, 0))
        self.assertFalse(solver.is_safe(1, 1))
        self.assertTrue(solver.is_safe(2, 1))
        self.assertTrue(solver.is_safe(1, 2))

if __name__ == '__main__':
    unittest.main()
