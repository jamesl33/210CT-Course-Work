#!/usr/bin/python3

class node:
    def __init__(self, data, previous_node=None, next_node=None):
        assert isinstance(data, str)
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node
