#!/usr/bin/python3
"""cube.py: Class file which contains the Cube class this class is used in conjunction with
stacking.py to stack cubes according to a set of rules
"""

class Cube:
    """cube: represents a cube but could easy be replaced by a dictionary, which would also be
    much faster"""
    def __init__(self, color, edge_length):
        self.color = color
        self.edge_length = edge_length
