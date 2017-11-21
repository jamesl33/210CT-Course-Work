#!/usr/bin/python3
"""unit_test.py: Make sure that the LinkedList class is working correctly
"""

import unittest
import linked_list

class UnitTest(unittest.TestCase):
    """UnitTest"""
    def test_append(self):
        """test_append: Test appending to a linked list
        """
        node1 = linked_list.Node('test')
        lst = linked_list.LinkedList()
        lst.append(node1)
        self.assertTrue(len(lst) == 1)

    def test_pop(self):
        """test_pop: Test removing a node from the end of the linked list and returning it
        """
        node1 = linked_list.Node('test')
        lst = linked_list.LinkedList()
        lst.append(node1)
        lst.pop()
        self.assertTrue(len(lst) == 0)

    def test_swap(self):
        """test_swap: test swapping two nodes values
        """
        node1 = linked_list.Node('test')
        node2 = linked_list.Node('anotherTest')
        lst = linked_list.LinkedList()
        lst.append(node1)
        lst.append(node2)
        lst._swap(node1, node2)

        current_node = lst.first_node
        while current_node:
            self.assertTrue(current_node.data == node1.data or node2.data)
            current_node = current_node.next_node

    def test_remove(self):
        """test_remove: Test removing a node by is reference
        """
        node1 = linked_list.Node('test')
        node2 = linked_list.Node('anotherTest')
        lst = linked_list.LinkedList()
        lst.append(node1)
        lst.append(node2)
        lst.remove(node1)

        current_node = lst.first_node
        while current_node:
            self.assertTrue(current_node.data == node2.data)
            current_node = current_node.next_node

if __name__ == '__main__':
    unittest.main()
