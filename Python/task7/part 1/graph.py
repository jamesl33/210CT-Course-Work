#!/usr/bin/python3

from node import node

class graph:
    def __init__(self, nodes):
        """__init__

        :param nodes: List of nodes to be added to the graph
        """
        assert(isinstance(nodes, list))

        self.vertices = set()
        self.edges = {}

        for newNode in nodes:
            self.add_node(newNode)

    def is_connected(self):
        visited = set()
        start = next(iter(self.vertices))

        def _is_connected(visited, start):
            """_is_connected

            :param visited: Set of visited nodes
            :param start: Node where we start if none is supplied the first one in 'vertices' will be used
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

    def add_node(self, targetNode):
        """add_node

        :param node: Adds a node to the graph using the helper functions '_add_edge' and '_add_vertex'
        """
        assert(isinstance(targetNode, node))
        self._add_vertex(targetNode.value)
        for connection in targetNode.connections:
            self._add_edge(targetNode.value, connection)

    def remove_node(self, targetNode):
        """remove_node

        :param node: Removes a node from the graph using the help functions '_remove_edge' and '_remove_vertex'
        """
        assert(isinstance(targetNode, node))
        self._remove_vertex(targetNode.value)
        self._remove_edge(targetNode.value)

    def _remove_vertex(self, value):
        self.vertices.remove(value)

    def _remove_edge(self, value):
        del(self.edges[value])
        for key in self.edges:
            self.edges[key].remove(value)

    def _add_vertex(self, value):
        self.vertices.add(value)

    def _add_edge(self, vertexA, vertexB):
        if vertexA not in self.edges:
            self.edges[vertexA] = set()
        self.edges[vertexA].add(vertexB)

        if vertexB not in self.edges:
            self.edges[vertexB] = set()
        self.edges[vertexB].add(vertexA)

