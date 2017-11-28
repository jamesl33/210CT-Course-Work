#!/usr/bin/python3
""" node.py: Contains the node class which is used in the simple database and binary trees
"""


class Node:
    """Node: Simple node class used in the binary trees
    """
    def __init__(self, value):
        self.value = value[0]
        self.owner = value[1]
        self.parent = None
        self.left_node = None
        self.right_node = None

    def __ne__(self, other):
        try:
            return self.value != other.value
        except AttributeError:
            return True

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __str__(self):
        return str(self.value)
