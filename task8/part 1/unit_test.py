#!/usr/bin/python3
""" unit_test.py: Unit testing for levenshtein string distance function
"""


import unittest
from string_converter import levenshtein


class UnitTest(unittest.TestCase):
    """UnitTest: Unit testing class for testing that levenshtein is working as expexted
    """
    def test_known_values(self):
        """test_known_values: Test values for vanilla string distance (levenshtein distance)
        """
        self.assertEqual(levenshtein('abc', 'abcd'), 1)
        self.assertEqual(levenshtein('abd', 'ab'), 1)
        self.assertEqual(levenshtein('abd', 'abc'), 1)
        self.assertEqual(levenshtein('kitten', 'sitting'), 3)
        self.assertEqual(levenshtein('hill', 'hello'), 2)

    def test_afaik_correct_values(self):
        """test_afaik_correct_values: This function does work for calculating the string
        distance but i'm not 100% sure when the weights are changed
        """
        self.assertEqual(levenshtein('abc', 'abcd', 3, 4, 5), 4)
        self.assertEqual(levenshtein('abd', 'ab', 3, 4, 5), 3)
        self.assertEqual(levenshtein('abd', 'abc', 3, 4, 5), 5)
        self.assertEqual(levenshtein('kitten', 'sitting', 3, 4, 5), 13)
        self.assertEqual(levenshtein('hill', 'hello', 3, 4, 5), 9)


if __name__ == '__main__':
    unittest.main()
