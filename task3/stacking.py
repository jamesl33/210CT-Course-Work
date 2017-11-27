#!/usr/bin/python3
"""stacking.py: Contains the functions to stack cubes according to rules
"""


def calc_height(stacked_list):
    """calc_height

    :param stacked_list: List of cubes
    :returns height: height of stacked cubes
    """
    assert isinstance(stacked_list, list)
    height = 0
    for cube in stacked_list:
        height += cube.edge_length
    return 'The maximum tower height is {0}'.format(height)


def widest_cube(cube_list, stacked_list):
    """widest_cube

    :param cube_list: List of cube objects
    :param stacked_list: List of current stacked cube objects
    """
    assert isinstance(cube_list, list)
    assert isinstance(stacked_list, list)
    current_widest_cube = None
    widest_edge = 0
    color = None
    if stacked_list:
        color = stacked_list[-1].color
    for cube in cube_list:
        if cube.edge_length > widest_edge and cube.color != color and cube not in stacked_list:
            widest_edge = cube.edge_length
            current_widest_cube = cube
    return current_widest_cube


def stack_cubes(cube_list):
    """stack_cubes

    :param cube_list: List of availble cube objects
    """
    assert isinstance(cube_list, list)
    stacked_list = []
    stacked_list.append(widest_cube(cube_list, stacked_list))
    while len(stacked_list) != len(cube_list):
        stacked_list.append(widest_cube(cube_list, stacked_list))
        if None in stacked_list:
            raise ValueError('You cannot stack these cubes according to the rules')
    return calc_height(stacked_list)
