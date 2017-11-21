#!/usr/bin/python3
"""weighted_node.py: File containing WeightedNode class
"""

from node import Node


class WeightedNode(Node):
    """WeightedNode class allowing for nodes to have a weight(distance to other nodes)
    """
    def __init__(self, value, connections, weights):
        """__init__

        :param value: Value of the node can only be a 'str' or 'int'
        :param connections: List of the nodes connections base of other nodes value e.g [1, 2, 4]
         or ['a', 'b', 'c']
        :param weights: Dictionary - Keys are tuples from this node to another connection
        """
        assert isinstance(weights, dict)
        assert len(weights) == len(connections)
        for connection in connections:
            assert (value, connection) in weights

        self.weights = weights
        Node.__init__(self, value, connections)
