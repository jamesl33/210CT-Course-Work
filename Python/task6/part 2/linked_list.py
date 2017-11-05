#!/usr/bin/python3

from node import node

class linked_list:
    def __init__(self, new_node=None):
        if new_node != None:
            assert isinstance(new_node, node)
        self.first_node = new_node
        self.last_node = new_node

    def push(self, new_node):
        if self.first_node == None and self.last_node == None:
            self.first_node = new_node
            self.last_node = new_node
        else:
            new_node.next_node = self.first_node
            new_node.previous_node = None
            self.first_node.previous_node = new_node
            self.first_node = new_node

    def pop(self):
        node = self.last_node
        self.remove(node)
        return node

    def append(self, new_node):
        if self.first_node == None and self.last_node == None:
            self.first_node = new_node
            self.last_node = new_node
        else:
            new_node.next_node = None
            new_node.previous_node = self.last_node
            self.last_node.next_node = new_node
            self.last_node = new_node

    def remove(self, node):
        if node == self.first_node:
            self.first_node = node.next_node
        elif node == self.last_node:
            self.last_node = node.previous_node
            self.last_node.next_node = None
        else:
            next_node = node.next_node
            previous_node = node.previous_node
            next_node.previous_node = previous_node
            previous_node.next_node = next_node

    def size(self):
        node = self.first_node
        count = 0
        while node:
            count += 1
            node = node.next_node
        return count

    def swap(self, a, b):
        tmpData = b.data
        b.data = a.data
        a.data = tmpData

    def sort(self):
        currentNode = self.first_node
        Sorted = False

        while not Sorted:
            Sorted = True
            while currentNode:
                if currentNode.next_node != None and currentNode.data > currentNode.next_node.data:
                    self.swap(currentNode, currentNode.next_node)
                    Sorted = False
                currentNode = currentNode.next_node
            currentNode = self.first_node

    def insert(self, newNode, index): # Zero indexed
        if index < 0 or index > self.size():
            raise IndexError('List index out of range')

        if index == 0:
            self.push(newNode)
            return

        node = self.first_node

        count = 1
        while node:
            if node.next_node == None:
                self.append(newNode)
                break

            if count == index:
                newNode.previous_node = node
                newNode.next_node = node.next_node
                node.next_node = newNode
                break

            count += 1
            node = node.next_node

    def reverse_display(self):
        contents = '['
        next_node = self.last_node
        while next_node:
            if next_node.previous_node == None:
                contents += '{0}]'.format(str(next_node.data))
            else:
                contents += '{0}, '.format(str(next_node.data))
            next_node = next_node.previous_node
        return contents

    def __str__(self):
        contents = '['
        next_node = self.first_node
        while next_node:
            if next_node.next_node == None:
                contents += '{0}]'.format(str(next_node.data))
            else:
                contents += '{0}, '.format(str(next_node.data))
            next_node = next_node.next_node
        return contents
