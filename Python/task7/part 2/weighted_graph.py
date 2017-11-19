#!/usr/bin/python3

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

    def longest_path(self, start, end):
        """longest_path: Function which uses '_shortest_distances_from' to find the longest path from node 'start' to node 'end'
        it does this by inverting the path weights using '_invert_weights'.

        :param start: Integer value of the node which you want to start at
        :param end: Integer value of the node which you want to end at
        """
        if start not in self.vertices or end not in self.vertices:
            raise ValueError('Start or End node not in graph')

        def _invert_weights():
            for weight in self.weights:
                self.weights[weight] = self.weights[weight] * -1

        _invert_weights()
        longestPath = self._shortest_distances_from(start)[end]
        _invert_weights()
        if longestPath == None:
            raise ValueError('There is not path from {0} to {1}'.format(start, end))
        return longestPath * -1

    def shortest_path(self, start, end):
        """shortest_path: Function which uses '_shortest_distances_from' to find the shortest path from node 'start' to node 'end'

        :param start: Integer value of the node which you want to start at
        :param end: Integer value of the node which you want to end at
        """
        if start not in self.vertices or end not in self.vertices:
            raise ValueError('Start or End node not in graph')
        path = self._shortest_distances_from(start)[end]
        if path == None:
            raise ValueError('There is not path from {0} to {1}'.format(start, end))
        return path

    def _shortest_distances_from(self, start):
        """_shortest_distances_from: Generates a dictionary with the distance to each node from 'start'

        :param start: Integer value representing the starting node
        """
        distances = {}
        for vertex in self.vertices:
            distances[vertex] = None
        distances[start] = 0
        for vertex in self.topological_sort():
            if distances[vertex] != None:
                if vertex in self.edges:
                    for neighbour in self.edges[vertex]:
                        newDist = distances[vertex] + self.weights[(vertex, neighbour)]
                        if distances[neighbour] == None:
                            distances[neighbour] = newDist
                        else:
                            distances[neighbour] = min(distances[neighbour], newDist)
        return distances

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

