#!/usr/bin/python3
"""node.py: Linked list nodes
"""

class Node:
    """Node: node class for the linked lists
    """
    def __init__(self, data, previous_node=None, next_node=None):
        assert isinstance(data, str)
        assert isinstance(previous_node, Node) or previous_node is None
        assert isinstance(next_node, Node) or next_node is None
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node
