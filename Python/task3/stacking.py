#!/usr/bin/python3

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
