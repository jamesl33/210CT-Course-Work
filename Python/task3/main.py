#!/usr/bin/python3

from cube import cube
from stacking import *

cube1 = cube('red', 5)
cube2 = cube('red', 6)
cube3 = cube('blue', 5)
cubeList = [cube1, cube2, cube3]
print(stack_cubes(cubeList))
