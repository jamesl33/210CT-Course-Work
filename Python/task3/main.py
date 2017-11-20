#!/usr/bin/python3

from cube import Cube
from stacking import stack_cubes

def main():
    """main: Driver function to make sure code is running correctly """
    cube1 = Cube('red', 5)
    cube2 = Cube('red', 6)
    cube3 = Cube('blue', 5)
    cube_list = [cube1, cube2, cube3]
    print(stack_cubes(cube_list))

main()
