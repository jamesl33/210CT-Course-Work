#!/usr/bin/python3

import unittest
from weighted_graph import weighted_graph
from weighted_node import weighted_node

class UnitTest(unittest.TestCase):
    def test_add_node(self):
        n1 = weighted_node(1, [2], {(1, 2): 2})
        n2 = weighted_node(2, [1], {(2, 1): 2})
        n3 = weighted_node(3, [1, 2], {(3, 1): 2, (3, 2): 4})
        g = weighted_graph([n1, n2])
        g.add_node(n3)

        self.assertEqual(g.vertices, set({1, 2, 3}))
        self.assertEqual(g.edges, {1: set({2}), 2: set({1}), 3: set({1, 2})})
        self.assertEqual(g.weights, {(1, 2): 2, (2, 1): 2, (3, 1): 2, (3, 2): 4})

    def test_remove(self):
        n1 = weighted_node(1, [2], {(1, 2): 2})
        n2 = weighted_node(2, [1], {(2, 1): 2})
        g = weighted_graph([n1, n2])
        g.remove_node(n1)

        self.assertEqual(g.vertices, set({2}))
        self.assertEqual(g.edges, {2: set({})})
        self.assertEqual(g.weights, {})

    def test_get_indegrees(self):
        n0 = weighted_node(0, [], {})
        n1 = weighted_node(1, [], {})
        n2 = weighted_node(2, [3], {(2, 3): 1})
        n3 = weighted_node(3, [1], {(3, 1): 1})
        n4 = weighted_node(4, [0, 1], {(4, 0): 1, (4, 1): 1})
        n5 = weighted_node(5, [0, 2], {(5, 0): 1, (5, 2): 1})
        g = weighted_graph([n0, n1, n2, n3, n4, n5])

        self.assertEqual(g.vertices, set({0, 1, 2, 3, 4, 5}))
        self.assertEqual(g.edges, {2: set({3}), 3: set({1}), 4: set({0, 1}), 5: set({0, 2})})
        self.assertEqual(g.weights, {(2, 3): 1, (3, 1): 1, (4, 0): 1, (4, 1): 1, (5, 0): 1, (5, 2): 1})
        self.assertEqual(g._get_indegrees(), {0: 2, 1: 2, 2: 1, 3: 1, 4: 0, 5: 0})

    def test_topological_sort(self):
        n0 = weighted_node(5, [11], {(5, 11): 1})
        n1 = weighted_node(11, [2, 9, 10], {(11, 2): 1, (11, 9): 1, (11, 10): 1})
        n2 = weighted_node(2, [], {})
        n3 = weighted_node(7, [8, 11], {(7, 8): 1, (7, 11): 1})
        n4 = weighted_node(8, [9], {(8, 9): 1})
        n5 = weighted_node(9, [], {})
        n6 = weighted_node(3, [8, 10], {(3, 8): 1, (3, 10): 1})
        n7 = weighted_node(10, [], {})
        g = weighted_graph([n0, n1, n2, n3, n4, n5, n6, n7])
        self.assertEqual(g.topological_sort(), [7, 5, 11, 3, 10, 8, 9, 2])

    def test_topological_sort_error(self):
        n0 = weighted_node(1, [2], {(1, 2): 1})
        n1 = weighted_node(2, [1], {(2, 1): 1})
        g = weighted_graph([n0, n1])
        with self.assertRaises(TypeError):
            g.topological_sort()

    def test_shortest_path(self):
        n0 = weighted_node(0, [1, 4], {(0, 1): 1, (0, 4): 11})
        n1 = weighted_node(1, [2], {(1, 2): 2})
        n2 = weighted_node(2, [3], {(2, 3): 3})
        n3 = weighted_node(3, [], {})
        n4 = weighted_node(4, [5], {(4, 5): 14})
        n5 = weighted_node(5, [3], {(5, 3): 12})
        g = weighted_graph([n0, n1, n2, n3, n4, n5])
        self.assertEqual(g.shortest_path(0, 3), 6)

    def test_longest_path(self):
        n0 = weighted_node(0, [1, 4], {(0, 1): 1, (0, 4): 11})
        n1 = weighted_node(1, [2], {(1, 2): 2})
        n2 = weighted_node(2, [3], {(2, 3): 3})
        n3 = weighted_node(3, [], {})
        n4 = weighted_node(4, [5], {(4, 5): 14})
        n5 = weighted_node(5, [3], {(5, 3): 12})
        g = weighted_graph([n0, n1, n2, n3, n4, n5])
        self.assertEqual(g.longest_path(0, 3), 37)

    def test_shortest_path_error(self):
        n0 = weighted_node(0, [1, 4], {(0, 1): 1, (0, 4): 11})
        n1 = weighted_node(1, [2], {(1, 2): 2})
        g = weighted_graph([n0, n1])
        with self.assertRaises(ValueError):
            g.shortest_path(0, 2)

    def test_longest_path_error(self):
        n0 = weighted_node(0, [1, 4], {(0, 1): 1, (0, 4): 11})
        n1 = weighted_node(1, [2], {(1, 2): 2})
        g = weighted_graph([n0, n1])
        with self.assertRaises(ValueError):
            g.longest_path(0, 2)

if __name__ == '__main__':
    unittest.main()
