#!/usr/bin/python3
"""unit_test.py: Testing the 'weighted_graph' and 'weighted_node' classes
"""

import unittest
from weighted_graph import WeightedGraph
from weighted_node import WeightedNode


class UnitTest(unittest.TestCase):
    """UnitTest"""
    def test_add_node(self):
        """test_add_node: Test adding a new node
        """
        node_1 = WeightedNode(1, [2], {(1, 2): 2})
        node_2 = WeightedNode(2, [1], {(2, 1): 2})
        node_3 = WeightedNode(3, [1, 2], {(3, 1): 2, (3, 2): 4})
        graph = WeightedGraph([node_1, node_2])
        graph.add_node(node_3)

        self.assertEqual(graph.vertices, set({1, 2, 3}))
        self.assertEqual(graph.edges, {1: set({2}), 2: set({1}), 3: set({1, 2})})
        self.assertEqual(graph.weights, {(1, 2): 2, (2, 1): 2, (3, 1): 2, (3, 2): 4})

    def test_remove(self):
        """test_remove: Test removing a node
        """
        node_1 = WeightedNode(1, [2], {(1, 2): 2})
        node_2 = WeightedNode(2, [1], {(2, 1): 2})
        graph = WeightedGraph([node_1, node_2])
        graph.remove_node(node_1)

        self.assertEqual(graph.vertices, set({2}))
        self.assertEqual(graph.edges, {2: set({})})
        self.assertEqual(graph.weights, {})

    def test_topological_sort(self):
        """test_topological_sort: There is a picture in this folder showing the visual
        representation of this graph. Testing generating a topologically sorted list
        of graph vertices
        """
        node_0 = WeightedNode(5, [11], {(5, 11): 1})
        node_1 = WeightedNode(11, [2, 9, 10], {(11, 2): 1, (11, 9): 1, (11, 10): 1})
        node_2 = WeightedNode(2, [], {})
        node_3 = WeightedNode(7, [8, 11], {(7, 8): 1, (7, 11): 1})
        node_4 = WeightedNode(8, [9], {(8, 9): 1})
        node_5 = WeightedNode(9, [], {})
        node_6 = WeightedNode(3, [8, 10], {(3, 8): 1, (3, 10): 1})
        node_7 = WeightedNode(10, [], {})
        graph = WeightedGraph([node_0, node_1, node_2, node_3, node_4, node_5, node_6, node_7])
        self.assertEqual(graph.topological_sort(), [7, 5, 11, 3, 10, 8, 9, 2])

    def test_topological_sort_error(self):
        """test_topological_sort_error: Make sure that 'topological_sort' raises the correct error
        """
        node_0 = WeightedNode(1, [2], {(1, 2): 1})
        node_1 = WeightedNode(2, [1], {(2, 1): 1})
        graph = WeightedGraph([node_0, node_1])
        with self.assertRaises(TypeError):
            graph.topological_sort()

    def test_shortest_path(self):
        """test_shortest_path: Test that the shortest math is correctly generated using
        the '_dijkstra' function
        """
        node_0 = WeightedNode(0, [1, 4], {(0, 1): 1, (0, 4): 11})
        node_1 = WeightedNode(1, [2], {(1, 2): 2})
        node_2 = WeightedNode(2, [3], {(2, 3): 3})
        node_3 = WeightedNode(3, [], {})
        node_4 = WeightedNode(4, [5], {(4, 5): 14})
        node_5 = WeightedNode(5, [3], {(5, 3): 12})
        graph = WeightedGraph([node_0, node_1, node_2, node_3, node_4, node_5])
        self.assertEqual(graph.shortest_path(0, 3), 'Path: [0, 1, 2, 3]\nDistance traveled: 6')

        node_0 = WeightedNode(5, [11, 9], {(5, 11): 4, (5, 9): 1})
        node_1 = WeightedNode(11, [2, 9, 10], {(11, 2): 6, (11, 9): 2, (11, 10): 9})
        node_2 = WeightedNode(2, [5], {(2, 5): 2})
        node_3 = WeightedNode(7, [8, 11], {(7, 8): 2, (7, 11): 5})
        node_4 = WeightedNode(8, [9], {(8, 9): 5})
        node_5 = WeightedNode(9, [2], {(9, 2): 4})
        node_6 = WeightedNode(3, [8, 10], {(3, 8): 2, (3, 10): 7})
        node_7 = WeightedNode(10, [9], {(10, 9): 4})
        graph = WeightedGraph([node_0, node_1, node_2, node_3, node_4, node_5, node_6, node_7])
        self.assertEqual(graph.shortest_path(5, 9), 'Path: [5, 9]\nDistance traveled: 1')

    def test_longest_path(self):
        """test_longest_path: Test that the longest path is correctly generated using
        the '_belmon_ford' function
        """
        node_0 = WeightedNode(0, [1, 4], {(0, 1): 1, (0, 4): 11})
        node_1 = WeightedNode(1, [2], {(1, 2): 2})
        node_2 = WeightedNode(2, [3], {(2, 3): 3})
        node_3 = WeightedNode(3, [], {})
        node_4 = WeightedNode(4, [5], {(4, 5): 14})
        node_5 = WeightedNode(5, [3], {(5, 3): 12})
        graph = WeightedGraph([node_0, node_1, node_2, node_3, node_4, node_5])
        self.assertEqual(graph.longest_path(0, 3), 'Path: [0, 4, 5, 3]\nDistance traveled: 37')


if __name__ == '__main__':
    unittest.main()
