#!/usr/bin/python3

import unittest
from linked_list import *

class UnitTest(unittest.TestCase):
    def test_append(self):
        node1 = node('test')
        lst = linked_list()
        lst.append(node1)
        self.assertTrue(len(lst) == 1)

    def test_pop(self):
        node1 = node('test')
        lst = linked_list()
        lst.append(node1)
        lst.pop()
        self.assertTrue(len(lst) == 0)

    def test__swap(self):
        node1 = node('test')
        node2 = node('anotherTest')
        lst = linked_list()
        lst.append(node1)
        lst.append(node2)
        lst._swap(node1, node2)

        currentNode = lst.first_node
        while currentNode:
            self.assertTrue(currentNode.data == node1.data or node2.data)
            currentNode = currentNode.next_node

    def test_remove(self):
        node1 = node('test')
        node2 = node('anotherTest')
        lst = linked_list()
        lst.append(node1)
        lst.append(node2)
        lst.remove(node1)

        currentNode = lst.first_node
        while currentNode:
            self.assertTrue(currentNode.data == node2.data)
            currentNode = currentNode.next_node

if __name__ == '__main__':
    unittest.main()
