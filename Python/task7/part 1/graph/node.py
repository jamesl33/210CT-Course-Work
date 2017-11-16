#!/usr/bin/python3

class node:
    def __init__(self, value, connections):
        """__init__

        :param value: Value of the node e.g. string, int
        :param connections: List of the nodes connections base of other nodes value e.g [1, 2, 4] or ['a', 'b', 'c']
        """
        self.value = value
        self.connections = connections

    def __str__(self):
        return self.value
