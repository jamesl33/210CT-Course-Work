#!/usr/bin/python3
"""unit_test.py: Testing to make sure that the unweighted undirected graph class
functions are working
"""

import unittest
from node import Node
from graph import Graph

class UnitTest(unittest.TestCase):
    """UnitTest"""

    def test_add_node(self):
        """test_add_node: Testing adding a new node to the graph
        """
        node_1 = Node(2, [1, 3])
        graph = Graph([])
        self.assertEqual(graph.vertices, set({}))
        self.assertEqual(graph.edges, {})
        graph.add_node(node_1)
        self.assertEqual(graph.vertices, set({1, 2, 3}))
        self.assertEqual(graph.edges, {1: set({2}), 2: set({1, 3}), 3: set({2})})

    def test_remove_node(self):
        """test_remove_node: Testing removing of an old node
        """
        node_1 = Node(1, [3])
        graph = Graph([node_1])
        graph.remove_node(node_1)
        self.assertEqual(graph.vertices, set({3}))
        self.assertEqual(graph.edges, {3: set({})})

    def test_is_connected_false(self):
        """test_is_connected_false: Test that is_connected works to find out if a
        graph is not connected
        """
        node_1 = Node(1, [2])
        node_2 = Node(2, [1])
        node_3 = Node(3, [4])
        node_4 = Node(4, [3])
        graph = Graph([node_1, node_2, node_3, node_4])
        self.assertFalse(graph.is_connected())

    def test_is_connected_true(self):
        """test_is_connected_true: Test that is_connected works to find out if a
        graph is connected
        """
        node_1 = Node(1, [2, 4])
        node_2 = Node(2, [4])
        node_3 = Node(3, [2, 1])
        graph = Graph([node_1, node_2, node_3])
        self.assertTrue(graph.is_connected())

if __name__ == '__main__':
    unittest.main()
