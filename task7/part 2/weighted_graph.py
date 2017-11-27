#!/usr/bin/python3
"""weighted_graph.py: 'weighted_graph' class which allows for pathfinding
"""

import math
from graph import Graph
from weighted_node import WeightedNode


class WeightedGraph(Graph):
    """weighted_graph: Directed acyclic graph class which inherits from Graph class
    """

    def __init__(self, nodes):
        """__init__

        :param nodes: List of nodes to be added to the graph
        """
        self.weights = {}
        Graph.__init__(self, nodes)

    def add_node(self, target_node):
        """add_node

        :param target_node: Overridden 'add_node' function to include adding of 'weights'
        """
        assert isinstance(target_node, WeightedNode)
        self._add_vertex(target_node.value)
        self._add_weights(target_node.weights)
        for connection in target_node.connections:
            self._add_edge(target_node.value, connection)

    def remove_node(self, target_node):
        """remove_node

        :param target_node: Overridden 'remove_node' function to include removal of 'weights'
        """
        assert isinstance(target_node, WeightedNode)
        self._remove_vertex(target_node.value)
        self._remove_edge(target_node.value)
        self._remove_weights(target_node.value, target_node.weights)

    def topological_sort(self):
        """topological_sort: Function to topologically sort a graph
        https://en.wikipedia.org/wiki/Topological_sorting

        :returns: List representing the graph nodes in topologically sorted order
        """
        stack = []
        visited = set()
        top_order = []

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
            top_order.insert(0, node)
            visited.add(node)

        while visited != self.vertices:
            for node in self.vertices:
                _visit(node)
        return top_order

    def longest_path(self, start, end):
        """longest_path: Uses _belmon_ford to calculate longest path by negating weights

        :param start: Integer representing the start node
        :param end: Integer representing the end node
        """
        assert isinstance(start, int)
        assert isinstance(end, int)

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
        assert isinstance(start, int)
        assert isinstance(end, int)
        distance, path = self._dijkstra(start, end)
        if math.isinf(distance):
            raise ValueError('There is no path from {0} to {1}'.format(start, end))
        return 'Path: {0}\nDistance traveled: {1}'.format(path, distance)

    def get_shortest_hamiltonian_cycle(self):
        """get_shortest_hamiltonian_cycle: Find the shortest hamiltonian cycle in a graph

        :return list: list containing the shortest hamiltonian path if there is multiple of
        the same length they are all returned
        """
        cycles = self.get_hamiltonian_cycles()

        def _path_cost(path):
            cost = 0
            for index, vertex in enumerate(path):
                try:
                    cost += self.weights[(vertex, path[index + 1])]
                except IndexError:
                    pass
            return path, cost

        costs = []
        for cycle in cycles:
            costs.append(_path_cost(cycle))

        minimum = math.inf
        minimum_cycle = []
        for cycle in costs:
            if cycle[1] < minimum:
                minimum = cycle[1]
                minimum_cycle.append(cycle)

            elif cycle[1] == minimum:
                minimum_cycle.append(cycle)

        return minimum_cycle

    def _belmon_ford(self, start, end):
        """_belmon_ford: Use Belmon ford to calculate the longest path. This is needed because
        Dijkstra's weights must be non-negative

        :param start: Integer representing the start node
        :param end: Integer representing the end node
        :return Tuple: Tuple (shortest distance, sorted path)
        """
        for i in range(len(self.vertices)):
            assert start in self.vertices and end in self.vertices
            distances = dict.fromkeys(self.vertices, math.inf)
            predecessors = dict.fromkeys(self.vertices, None)
            distances[start] = 0

            for vertex in self.vertices and self.edges:
                for neighbour in self.edges[vertex]:
                    if distances[neighbour] > distances[vertex] + self.weights[(vertex, neighbour)]:
                        distances[neighbour] = distances[vertex] + self.weights[(vertex, neighbour)]
                        predecessors[neighbour] = vertex

            for vertex in self.vertices and self.edges:
                for neighbour in self.edges:
                    if (vertex, neighbour) in self.weights:
                        if distances[neighbour] > distances[vertex] + \
                                self.weights[(vertex, neighbour)]:
                            raise TypeError('This graph contains a negative cycle')
            return distances[end], self._short_path(predecessors, end)

    def _dijkstra(self, start, end):
        """_dijkstra: Use dijkstra algorithm to get the shortest path

        :param start: Integer representing the start node
        :param end: Integer representing the end node
        :return Tuple: Tuple (shortest distance, sorted path)
        """
        assert start in self.vertices and end in self.vertices
        visited = set()
        distances = dict.fromkeys(list(self.vertices), math.inf)
        path = dict.fromkeys(list(self.vertices), None)
        distances[start] = 0
        while visited != self.vertices:
            vertex = min(set(distances.keys()) - visited)
            if vertex in self.edges:
                for neighbour in self.edges[vertex]:
                    test_path = distances[vertex] + self.weights[(vertex, neighbour)]
                    if test_path < distances[neighbour]:
                        distances[neighbour] = test_path
                        path[neighbour] = vertex
            visited.add(vertex)
        return distances[end], self._short_path(path, end)

    def _add_edge(self, vertex_a, vertex_b):
        if vertex_a not in self.edges:
            self.edges[vertex_a] = set()
        self.edges[vertex_a].add(vertex_b)

    def _add_weights(self, weights):
        for weight in weights:
            self.weights[weight] = weights[weight]

    def _remove_weights(self, value, weights):
        for weight in list(weights):
            del self.weights[weight]
        for weight in list(self.weights):
            if value in weight:
                del self.weights[weight]

    @classmethod
    def _short_path(cls, path, end):
        """_short_path

        :param path: Dictionary created above
        :param end: Integer representing the end node
        :return List: Shortest path
        """
        short_path = []
        node = end
        while path[node] is not None:
            short_path.insert(0, node)
            node = path[node]
        short_path.insert(0, node)
        return short_path
