#!/usr/bin/python3

import math
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
        """longest_path: Uses _belmon_ford to calculate longest path by negating weights

        :param start: Integer representing the start node
        :param end: Integer representing the end node
        """
        def _invert():
            for weight in self.weights:
                self.weights[weight] = self.weights[weight] * -1
        _invert()
        distance, path = self._belmon_ford(start, end)
        _invert()
        if math.isinf(distance):
            raise ValueError('There is no path from {0} to {1}'.format(start, end))
        return 'Path: {0}\nDistance traveled: {1}'.format(path, distance * -1)

    def shortest_path(self, start, end):
        """shortest_path: Use _dijkstra to calculate shortest path

        :param start: Integer representing the start node
        :param end: Integer representing the end node
        """
        distance, path = self._dijkstra(start, end)
        if math.isinf(distance):
            raise ValueError('There is no path from {0} to {1}'.format(start, end))
        return 'Path: {0}\nDistance traveled: {1}'.format(path, distance)

    def _belmon_ford(self, start, end):
        """_belmon_ford: Use Belmon ford to calculate the longest path. This is needed because Dijkstra's
        weights must be non-negative

        :param start: Integer representing the start node
        :param end: Integer representing the end node
        :return Tuple: Tuple (shortest distance, sorted path)
        """
        assert(start in self.vertices and end in self.vertices)
        distances = dict.fromkeys(list(self.vertices), math.inf)
        predecessors = dict.fromkeys(list(self.vertices), None)
        distances[start] = 0
        for i in range(len(self.vertices)):
            for vertex in self.vertices:
                if vertex in self.edges:
                    for neighbour in self.edges[vertex]:
                        if distances[neighbour] > distances[vertex] + self.weights[(vertex, neighbour)]:
                            distances[neighbour] = distances[vertex] + self.weights[(vertex, neighbour)]
                            predecessors[neighbour] = vertex
        for vertex in self.vertices:
            if vertex in self.edges:
                for neighbour in self.edges:
                    try:
                        if distances[neighbour] > distances[vertex] + self.weights[(vertex, neighbour)]:
                            raise TypeError('This graph contains a negative cycle')
                    except KeyError:
                        pass

        return distances[end], self._short_path(predecessors, end)

    def _dijkstra(self, start, end):
        """_dijkstra: Use dijkstra algorithm to get the shortest path

        :param start: Integer representing the start node
        :param end: Integer representing the end node
        :return Tuple: Tuple (shortest distance, sorted path)
        """
        assert(start in self.vertices and end in self.vertices)
        visited = set()
        distances = dict.fromkeys(list(self.vertices), math.inf)
        path = dict.fromkeys(list(self.vertices), None)
        distances[start] = 0
        while visited != self.vertices:
            vertex = min(set(distances.keys()) - visited)
            if vertex in self.edges:
                for neighbour in self.edges[vertex]:
                    testPath = distances[vertex] + self.weights[(vertex, neighbour)]
                    if testPath < distances[neighbour]:
                        distances[neighbour] = testPath
                        path[neighbour] = vertex
            visited.add(vertex)

        return distances[end], self._short_path(path, end)

    def _short_path(self, path, end):
        """_short_path

        :param path: Dictionary created above
        :param end: Integer representing the end node
        :return List: Shortest path
        """
        shortPath = []
        node = end
        while path[node] != None:
            shortPath.insert(0, node)
            node = path[node]
        shortPath.insert(0, node)
        return shortPath

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

