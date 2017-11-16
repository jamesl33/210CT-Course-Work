#!/usr/bin/python3

from node import node

class weighted_node(node):
    def __init__(self, value, connections, weights):
        """__init__

        :param value: Value of the node can only be a 'str' or 'int'
        :param connections: List of the nodes connections base of other nodes value e.g [1, 2, 4] or ['a', 'b', 'c']
        :param weights: Dictionary - Keys are tuples from this node to another connection
        """
        assert(isinstance(weights, dict))
        assert(len(weights) == len(connections))
        for c in connections:
            assert((value, c) in weights)

        self.weights = weights
        node.__init__(self, value, connections)

