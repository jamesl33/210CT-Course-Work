#!/usr/bin/python3
"""unit_test.py: Unit testing to make sure that quick sort has been implimented properly
"""

import unittest
from sorting import quick_sort

class UnitTest(unittest.TestCase):
    """UnitTest"""
    def test_quick__sort(self):
        """test_quick__sort: Make sure that i have implimented quick_sort properly
        """
        unsorted_list = [1, 5, 2, 6, 8, 5, 234, 5645, 234, 6, 4, 756, 234, 2, 3, 4, 656, 7, 234]
        self.assertEqual(quick_sort(unsorted_list), [1, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7, 8, 234, 234, \
                                                     234, 234, 656, 756, 5645])

        unsorted_list = [5, 3, 2, 72, 5, 7, 23]
        self.assertEqual(quick_sort(unsorted_list), [2, 3, 5, 5, 7, 23, 72])

        unsorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(quick_sort(unsorted_list), [1, 2, 3, 4, 5, 6, 7, 8, 9])

if __name__ == '__main__':
    unittest.main()
