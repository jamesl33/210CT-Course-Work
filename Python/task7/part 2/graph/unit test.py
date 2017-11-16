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
        self.assertEqual(g.edges, {1: set({2, 3}), 2: set({1, 3}), 3: set({1, 2})})
        self.assertEqual(g.weights, {(1, 2): 2, (2, 1): 2, (3, 1): 2, (3, 2): 4})

    def test_remove(self):
        n1 = weighted_node(1, [2], {(1, 2): 2})
        n2 = weighted_node(2, [1], {(2, 1): 2})
        g = weighted_graph([n1, n2])
        g.remove_node(n1)

        self.assertEqual(g.vertices, set({2}))
        self.assertEqual(g.edges, {2: set({})})
        self.assertEqual(g.weights, {})

if __name__ == '__main__':
    unittest.main()
