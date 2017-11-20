#!/usr/bin/python3

class Node:
    def __init__(self, value, connections):
        """__init__

        :param value: Value of the node can only be a 'str' or 'int'
        :param connections: List of the nodes connections base of other nodes value e.g [1, 2, 4] or
        ['a', 'b', 'c']
        """
        assert isinstance(value, (int, str))
        assert isinstance(connections, list)
        self.value = value
        self.connections = connections
