#!/usr/bin/python3
"""graph.py: Base graph class
"""

from node import Node


class Graph:
    """graph: Undirected unweighted graph class
    """
    def __init__(self, nodes):
        """__init__

        :param nodes: List of nodes to be added to the graph
        """
        assert isinstance(nodes, list)

        self.vertices = set()
        self.edges = {}

        for new_node in nodes:
            self.add_node(new_node)

    def is_connected(self):
        """is_connected: Function uses '_is_connected' to determine if graph is connected
        """
        visited = set()
        start = next(iter(self.vertices))

        def _is_connected(visited, start):
            """_is_connected

            :param visited: Set of visited nodes
            :param start: Node where we start if none is supplied the first one in 'vertices' will
            be used
            """
            visited.add(start)
            if len(visited) == len(self.vertices):
                return True
            for vertex in self.edges[start]:
                if vertex not in visited:
                    if _is_connected(visited, vertex):
                        return True
            return False

        return _is_connected(visited, start)

    def display(self):
        """display
        Displays the graphs values in a neat way on a per vertex basis
        """
        for vertex in self.vertices:
            print('{0}: {1}'.format(vertex, self.edges[vertex]))

    def add_node(self, target_node):
        """add_node

        :param node: Adds a node to the graph using the helper functions '_add_edge' and
        '_add_vertex'
        """
        assert isinstance(target_node, Node)
        self._add_vertex(target_node.value)
        for connection in target_node.connections:
            self._add_edge(target_node.value, connection)

    def remove_node(self, target_node):
        """remove_node

        :param node: Removes a node from the graph using the help functions '_remove_edge'
        and '_remove_vertex'
        """
        assert isinstance(target_node, Node)
        self._remove_vertex(target_node.value)
        self._remove_edge(target_node.value)

    def _remove_vertex(self, value):
        self.vertices.remove(value)

    def _remove_edge(self, value):
        del self.edges[value]
        for key in self.edges:
            self.edges[key].remove(value)

    def _add_vertex(self, value):
        self.vertices.add(value)

    def _add_edge(self, vertex_a, vertex_b):
        if vertex_a not in self.vertices:
            self._add_vertex(vertex_a)
        if vertex_b not in self.vertices:
            self._add_vertex(vertex_b)
        if vertex_a not in self.edges:
            self.edges[vertex_a] = set()
        self.edges[vertex_a].add(vertex_b)

        if vertex_b not in self.edges:
            self.edges[vertex_b] = set()
        self.edges[vertex_b].add(vertex_a)
