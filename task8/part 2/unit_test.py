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

    def test_wiki_ham_cycle(self):
        """test_wiki_ham_cycle: This is the graph taken from wikipedia
        <https://en.wikipedia.org/wiki/Hamiltonian_path> and is also in this folder as a png called
        'HamCycle.png'
        This is the function which is making the unit test take a while becuase this
        the Hamiltonian path problem is NP-Complete
        """
        node0 = Node(0, [1, 4, 6])
        node1 = Node(1, [0, 2, 7])
        node2 = Node(2, [1, 3, 8])
        node3 = Node(3, [2, 4, 9])
        node4 = Node(4, [0, 3, 5])
        node5 = Node(5, [4, 10, 11])
        node6 = Node(6, [0, 11, 12])
        node7 = Node(7, [1, 12, 13])
        node8 = Node(8, [2, 13, 14])
        node9 = Node(9, [3, 10, 14])
        node10 = Node(10, [5, 9, 15])
        node11 = Node(11, [5, 6, 19])
        node12 = Node(12, [6, 7, 18])
        node13 = Node(13, [7, 8, 18])
        node14 = Node(14, [8, 9, 16])
        node15 = Node(15, [10, 16, 19])
        node16 = Node(16, [14, 15, 17])
        node17 = Node(17, [13, 16, 18])
        node18 = Node(18, [12, 17, 19])
        node19 = Node(19, [11, 15, 18])
        graph = Graph([node0, node1, node2, node3, node4,
                       node5, node6, node7, node8, node9,
                       node10, node11, node12, node13, node14,
                       node15, node16, node17, node18, node19])

        cycles = graph.get_hamiltonian_cycles()

        for cycle in cycles:
            self.assertEqual(len(cycle), 21)

        for cycle in cycles:
            self.assertEqual(len(set(cycle)), 20)

        self.assertTrue([0, 4, 3, 2, 1, 7, 13, 8, 14, 9, 10, 5, 11, 19, 15, 16, 17, 18, 12, 6, 0]
                        in cycles)

    def test_wiki_no_ham_cycle(self):
        """test_wiki_no_ham_cycle: This is also a graph taken from wikipedia
        <https://en.wikipedia.org/wiki/Hamiltonian_path> and there is no
        Hamiltonian cycles in this graph. This graph is also in included in this
        folder as a png called 'NoHamCycle.png'
        """
        node0 = Node(0, [7, 8, 10, 9])
        node1 = Node(1, [5, 6, 7, 10])
        node2 = Node(2, [6, 7, 8])
        node3 = Node(3, [5, 6, 8, 9])
        node4 = Node(4, [5, 9, 10])
        node5 = Node(5, [1, 3, 4])
        node6 = Node(6, [1, 3, 2])
        node7 = Node(7, [0, 1, 2])
        node8 = Node(8, [0, 2, 3])
        node9 = Node(9, [0, 3, 4])
        node10 = Node(10, [0, 1, 4])
        graph = Graph([node0, node1, node2, node3, node4,
                       node5, node6, node7, node8, node9, node10])
        self.assertEqual(graph.get_hamiltonian_cycles(), [])

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
