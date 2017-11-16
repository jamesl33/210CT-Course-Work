#!/usr/bin/python3

import unittest
from node import node
from graph import graph

class UnitTest(unittest.TestCase):
    def setUp(self):
        n1 = node(1, [3])
        n2 = node(3, [1])

        nodeList = [n1, n2]
        self.g = graph(nodeList)

    def test_add_node(self):
        n = node(2, [1, 3])
        self.g.add_node(n)
        self.assertEqual(self.g.vertices, set([1, 2, 3]))
        self.assertEqual(self.g.edges, {1: set([2, 3]), 2: set([1, 3]), 3: set([1, 2])})

    def test_remove_node(self):
        n1 = node(1, [3])
        self.g.remove_node(n1)
        self.assertEqual(self.g.vertices, set([3]))
        self.assertEqual(self.g.edges, {3: set([])})

    def test_is_connected_false(self):
        n1 = node(1, [2])
        n2 = node(2, [1])
        n3 = node(3, [4])
        n4 = node(4, [3])
        g = graph([n1, n2, n3])
        self.assertFalse(g.is_connected())

    def test_is_connected_true(self):
        n1 = node(1, [2, 4])
        n2 = node(2, [4])
        n3 = node(3, [2, 1])
        n4 = node(4, [1, 2])
        g = graph([n1, n2, n3])
        self.assertTrue(g.is_connected())

if __name__ == '__main__':
    unittest.main()
