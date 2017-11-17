#!/usr/bin/python3

def calc_height(stackedList):
    """calc_height

    :param stackedList: List of cubes
    :returns height: height of stacked cubes
    """
    height = 0
    for cube in stackedList:
        height += cube.edgeLength
    return 'The maximum tower height is {0}'.format(height)

def widest_cube(cubeList, stackedList):
    """widest_cube

    :param cubeList: List of cube objects
    :param stackedList: List of current stacked cube objects
    """
    widestEdge = 0
    widestCube = None
    color = None
    if len(stackedList) != 0:
        color = stackedList[-1].color
    for cube in cubeList:
        if cube.edgeLength > widestEdge and cube.color != color and cube not in stackedList:
            widestEdge = cube.edgeLength
            widestCube = cube
    return widestCube

def stack_cubes(cubeList):
    """stack_cubes

    :param cubeList: List of availble cube objects
    """
    stackedList = []
    stackedList.append(widest_cube(cubeList, stackedList))
    while len(stackedList) != len(cubeList):
        stackedList.append(widest_cube(cubeList, stackedList))
        if None in stackedList:
            return 'You cannot stack these cubes according to the rules'
    return calc_height(stackedList)
