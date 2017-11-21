#!/usr/bin/python3
"""unit_test: File which contains the unit testing to make sure that
functions from stacking.py work as intended
"""

import unittest
from cube import Cube
from stacking import calc_height, stack_cubes, widest_cube


class UnitTest(unittest.TestCase):
    """UnitTest"""
    def test_calc_height(self):
        """test_calc_height: Testing calculate_height function"""
        cube1 = Cube('red', 6)
        cube2 = Cube('blue', 5)
        stacked_list = [cube1, cube2]
        self.assertEqual(calc_height(stacked_list), 'The maximum tower height is 11')

    def test_failure(self):
        """test_failure: Make sure a ValueError is raised if you cannot stack the cubes"""
        cube1 = Cube('red', 5)
        cube2 = Cube('red', 5)
        cube_list = [cube1, cube2]
        with self.assertRaises(ValueError):
            stack_cubes(cube_list)

    def test_widest_cube(self):
        """test_widest_cube: Test function to find the next widest cube
        """
        cube1 = Cube('red', 5)
        cube2 = Cube('blue', 3)
        cube3 = Cube('red', 5)
        cube4 = Cube('green', 6)
        cube5 = Cube('purple', 7)
        cube6 = Cube('red', 2)
        cube_list = [cube1, cube2, cube3, cube4, cube5, cube6]
        stacked_list = [cube5]
        self.assertEqual(widest_cube(cube_list, stacked_list), cube4)


if __name__ == '__main__':
    unittest.main()
