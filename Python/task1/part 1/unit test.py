#!/usr/bin/python3

import unittest
from factorials import test_divides

class UnitTest(unittest.TestCase):
    """UnitTest"""
    def test_correct(self):
        """test_correct: Test known correct values taken from the labsheet
        """
        known_correct_values = [(6, 9), (20, 10000)]
        for num_a, num_b in known_correct_values:
            self.assertTrue(test_divides(num_a, num_b)[1])

    def test_false(self):
        """test_false: Test known wrong values taken from the labsheet
        """
        known_wrong_values = [(6, 27), (20, 1000000)]
        for num_a, num_b in known_wrong_values:
            self.assertFalse(test_divides(num_a, num_b)[1])

if __name__ == '__main__':
    unittest.main()
