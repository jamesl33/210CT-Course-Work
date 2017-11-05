#!/usr/bin/python3

from cube import cube
from stacking import *
import unittest

class UnitTest(unittest.TestCase):
    def test_calc_height(self):
        cube1 = cube('red', 6)
        cube2 = cube('blue', 5)
        stackedList = [cube1, cube2]
        self.assertEqual(calc_height(stackedList), 'The maximum tower height is 11')

    def test_failure(self):
        cube1 = cube('red', 5)
        cube2 = cube('red', 5)
        cubeList = [cube1, cube2]
        self.assertEqual(stack_cubes(cubeList), 'You cannot stack these cubes according to the rules')

    def test_widest_cube(self):
        cube1 = cube('red', 5)
        cube2 = cube('blue', 3)
        cube3 = cube('red', 5)
        cube4 = cube('green', 6)
        cube5 = cube('purple', 7)
        cube6 = cube('red', 2)
        cubeList = [cube1, cube2, cube3, cube4, cube5, cube6]

        stackedList = [cube5]

        self.assertEqual(widest_cube(cubeList, stackedList), cube4)

if __name__ == '__main__':
    unittest.main()
