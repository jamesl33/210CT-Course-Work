#!/usr/bin/python3

from cube import cube

def calc_height(stackedList):
	height = 0
	for cube in stackedList:
		height += cube.get_edge_length()
	return 'The maximum tower height is {0}'.format(height)

def widest_cube(cubeList, stackedList):
	widestEdge = 0
	widestCube = None

	color = None
	if len(stackedList) != 0:
		color = stackedList[-1].get_color()

	for cube in cubeList:
		if cube.get_edge_length() > widestEdge and cube.get_color() != color and cube not in stackedList:
			widestEdge = cube.get_edge_length()
			widestCube = cube
	return widestCube

def stack_cubes(cubeList):
	stackedList = []
	stackedList.append(widest_cube(cubeList, stackedList))

	while len(stackedList) != len(cubeList):
		stackedList.append(widest_cube(cubeList, stackedList))

		if None in stackedList:
			return 'You cannot stack these cubes according to the rules'

	return calc_height(stackedList)

################# Pseudo Code #################



################# Pseudo Code #################

################# Labsheet Main ################# Comment out code inside of 'Labsheet Main' when running unit test

# Create cubes from the labsheet
cube1 = cube('red', 5)
cube2 = cube('red', 6)
cube3 = cube('blue', 5)
cubeList = [cube1, cube2, cube3]
# Computer answer and print it
print(stack_cubes(cubeList))

################# Labsheet Main #################

################# Unit Test ################# Uncomment code inside of 'Unit Test' when unit testing

# import unittest
#
# class UnitTest(unittest.TestCase):
#     def test_calc_height(self):
#         cube1 = cube('red', 6)
#         cube2 = cube('blue', 5)
#         stackedList = [cube1, cube2]
#         self.assertEqual(calc_height(stackedList), 'The maximum tower height is 11')
#
#     def test_failure(self):
#         cube1 = cube('red', 5)
#         cube2 = cube('red', 5)
#         cubeList = [cube1, cube2]
#         self.assertEqual(stack_cubes(cubeList), 'You cannot stack these cubes according to the rules')
#
#     def test_widest_cube(self):
#         cube1 = cube('red', 5)
#         cube2 = cube('blue', 3)
#         cube3 = cube('red', 5)
#         cube4 = cube('green', 6)
#         cube5 = cube('purple', 7)
#         cube6 = cube('red', 2)
#         cubeList = [cube1, cube2, cube3, cube4, cube5, cube6]
#
#         stackedList = [cube5]
#
#         self.assertEqual(widest_cube(cubeList, stackedList), cube4)
#
# if __name__ == '__main__':
#     unittest.main()

################# Unit Test #################
