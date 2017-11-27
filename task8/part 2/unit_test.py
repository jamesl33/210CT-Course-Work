#!/usr/bin/python3
""" unit_test.py: Testing for finding hamiltonian cycles
"""

import unittest
from graph import Graph
from node import Node
from weighted_graph import WeightedGraph
from weighted_node import WeightedNode


class UnitTest(unittest.TestCase):
    """UnitTest: There is no setup for this class
    """
    def test_known_no_hamiltonian(self):
        """test_known_no_hamiltonian: Test a graph which doesn't have a hamiltonian cycle
        """
        node0 = Node(0, [1, 3])
        node1 = Node(1, [0, 3, 4, 2])
        node2 = Node(2, [1, 4])
        node3 = Node(3, [0, 1])
        node4 = Node(4, [1, 2])
        graph = Graph([node0, node1, node2, node3, node4])
        self.assertEqual(graph.get_hamiltonian_cycles(), [])

    def test_known_hamiltonian_cycles(self):
        """test_known_hamiltonian_cycles: Test an unweighted undirected graph which has
        hamiltonian cycles
        """
        node0 = Node(0, [1, 3])
        node1 = Node(1, [0, 3, 4, 2])
        node2 = Node(2, [1, 4])
        node3 = Node(3, [0, 1, 4])
        node4 = Node(4, [1, 2, 3])
        graph = Graph([node0, node1, node2, node3, node4])
        self.assertEqual(graph.get_hamiltonian_cycles(), [[0, 3, 4, 2, 1, 0],
                                                          [0, 1, 2, 4, 3, 0],
                                                          [1, 2, 4, 3, 0, 1],
                                                          [1, 0, 3, 4, 2, 1],
                                                          [2, 4, 3, 0, 1, 2],
                                                          [2, 1, 0, 3, 4, 2],
                                                          [3, 4, 2, 1, 0, 3],
                                                          [3, 0, 1, 2, 4, 3],
                                                          [4, 3, 0, 1, 2, 4],
                                                          [4, 2, 1, 0, 3, 4]])

    def test_no_weighted_hamiltonian(self):
        """test_known_no_hamiltonian_weighted: Test a weighted directed graph with no
        hamiltonian cycles
        """
        node0 = WeightedNode(0, [1, 3], {(0, 1): 4, (0, 3): 5})
        node1 = WeightedNode(1, [0, 3, 4, 2], {(1, 0): 2, (1, 3): 3, (1, 4): 6, (1, 2): 1})
        node2 = WeightedNode(2, [1, 4], {(2, 1): 2, (2, 4): 5})
        node3 = WeightedNode(3, [0, 1], {(3, 0): 2, (3, 1): 5})
        node4 = WeightedNode(4, [1, 2], {(4, 1): 3, (4, 2): 5})
        graph = WeightedGraph([node0, node1, node2, node3, node4])
        self.assertEqual(graph.get_hamiltonian_cycles(), [])

    def test_known_weighted_hamiltonian(self):
        """test_known_weighted_hamiltonian_cycles: Weighted directed graph which is known
        to have hamiltonian cycles
        """
        node0 = WeightedNode(0, [1, 3], {(0, 1): 4, (0, 3): 3})
        node1 = WeightedNode(1, [0, 3, 4, 2], {(1, 0): 3, (1, 3): 4, (1, 4): 4, (1, 2): 3})
        node2 = WeightedNode(2, [1, 4], {(2, 1): 1, (2, 4): 3})
        node3 = WeightedNode(3, [0, 1, 4], {(3, 0): 5, (3, 1): 3, (3, 4): 6})
        node4 = WeightedNode(4, [1, 2, 3], {(4, 1): 2, (4, 2): 6, (4, 3): 7})
        graph = WeightedGraph([node0, node1, node2, node3, node4])
        self.assertEqual(graph.get_hamiltonian_cycles(), [[0, 3, 4, 2, 1, 0],
                                                          [0, 1, 2, 4, 3, 0],
                                                          [1, 2, 4, 3, 0, 1],
                                                          [1, 0, 3, 4, 2, 1],
                                                          [2, 4, 3, 0, 1, 2],
                                                          [2, 1, 0, 3, 4, 2],
                                                          [3, 4, 2, 1, 0, 3],
                                                          [3, 0, 1, 2, 4, 3],
                                                          [4, 3, 0, 1, 2, 4],
                                                          [4, 2, 1, 0, 3, 4]])

    def test_get_shortest_hamiltonian(self):
        """test_get_shortest_hamiltonian: Test finding the short hamiltonian path
        or paths in a directed weighted graph
        """
        node0 = WeightedNode(0, [1, 3], {(0, 1): 4, (0, 3): 3})
        node1 = WeightedNode(1, [0, 3, 4, 2], {(1, 0): 3, (1, 3): 4, (1, 4): 4, (1, 2): 3})
        node2 = WeightedNode(2, [1, 4], {(2, 1): 1, (2, 4): 3})
        node3 = WeightedNode(3, [0, 1, 4], {(3, 0): 5, (3, 1): 3, (3, 4): 6})
        node4 = WeightedNode(4, [1, 2, 3], {(4, 1): 2, (4, 2): 6, (4, 3): 7})
        graph = WeightedGraph([node0, node1, node2, node3, node4])
        self.assertEqual(graph.get_shortest_hamiltonian_cycle(), [([0, 3, 4, 2, 1, 0], 19),
                                                                  ([1, 0, 3, 4, 2, 1], 19),
                                                                  ([2, 1, 0, 3, 4, 2], 19),
                                                                  ([3, 4, 2, 1, 0, 3], 19),
                                                                  ([4, 2, 1, 0, 3, 4], 19)])


if __name__ == '__main__':
    unittest.main()
