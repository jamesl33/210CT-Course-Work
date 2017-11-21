#!/usr/bin/python3
"""node.py: Linked list nodes
"""

class Node:
    """Node: node class for the linked lists
    """
    def __init__(self, data, previous_node=None, next_node=None):
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node
