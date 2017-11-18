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
        """add_node

        :param node: Overridden 'add_node' function to include adding of 'weights'
        """
        assert(isinstance(node, weighted_node))
        self._add_vertex(node.value)
        self._add_weights(node.weights)
        for connection in node.connections:
            self._add_edge(node.value, connection)

    def remove_node(self, node):
        """remove_node

        :param node: Overridden 'remove_node' function to include removal of 'weights'
        """
        assert(isinstance(node, weighted_node))
        self._remove_vertex(node.value)
        self._remove_edge(node.value)
        self._remove_weights(node.weights)

    def topological_sort(self):
        """topological_sort: Function to topologically sort a graph
        https://en.wikipedia.org/wiki/Topological_sorting

        :returns: List representing the graph nodes in topologically sorted order
        """
        stack = []
        visited = set()
        topologicalOrder = []

        def _visit(node):
            if node in visited:
                return
            if node in stack:
                raise TypeError('Graph contains a cycle')
            stack.append(node)
            if node in self.edges:
                for neighbour in self.edges[node]:
                    _visit(neighbour)
            stack.pop()
            topologicalOrder.insert(0, node)
            visited.add(node)

        while visited != self.vertices:
            for node in self.vertices:
                _visit(node)
        return topologicalOrder

    def _get_indegrees(self):
        """_get_indegrees: Function which returns indegrees of all vertices

        :return dict
        """
        indegrees = {}
        for n in self.vertices:
            indegrees[n] = 0
        for vertex in self.vertices:
            if vertex in self.edges:
                for neighbour in self.edges[vertex]:
                    indegrees[neighbour] += 1
        return indegrees

    def _add_edge(self, vertexA, vertexB):
        if vertexA not in self.edges:
            self.edges[vertexA] = set()
        self.edges[vertexA].add(vertexB)

    def _add_weights(self, weights):
        for weight in weights:
            self.weights[weight] = weights[weight]

    def _remove_weights(self, weights):
        for weight in list(self.weights):
            del(self.weights[weight])

