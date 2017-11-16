#!/usr/bin/python3

from math import inf
from graph import graph
from weighted_node import weighted_node

class weighted_graph(graph):
    def __init__(self, nodes):
        """__init__

        :param nodes: List of nodes to be added to the graph
        :param weights: Dictionary containing the weights between nodes
        """
        self.weights = {}
        graph.__init__(self, nodes)

    def add_node(self, node):
        assert(isinstance(node, weighted_node))
        self._add_vertex(node.value)
        self._add_weights(node.weights)
        for connection in node.connections:
            self._add_edge(node.value, connection)

    def remove_node(self, node):
        assert(isinstance(node, weighted_node))
        self._remove_vertex(node.value)
        self._remove_edge(node.value)
        self._remove_weights(node.weights)

    def _add_weights(self, weights):
        for weight in weights:
            self.weights[weight] = weights[weight]

    def _remove_weights(self, weights):
        for weight in list(self.weights):
            del(self.weights[weight])

