#!/usr/bin/python3

import unittest
from factorials import *

class UnitTest(unittest.TestCase):
    def test_correct(self):
        known_correct_values = [(6, 9), (20, 10000)]
        for a, b in known_correct_values:
            self.assertTrue(testIfDivides(a, b)[1])

    def test_false(self):
        known_wrong_values = [(6, 27), (20, 1000000)]
        for a, b in known_wrong_values:
            self.assertFalse(testIfDivides(a,b)[1])

if __name__ == '__main__':
    unittest.main()
