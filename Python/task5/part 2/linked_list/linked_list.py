#!/usr/bin/python3

class linked_list:
    def __init__(self):
        self.size = 0
        self.first_node = None
        self.last_node = None

    def push(self, new_node):
        """push: Put 'new_node' at the front of the linked list

        :param new_node: Node object
        """
        if self.first_node == None and self.last_node == None:
            self.first_node = new_node
            self.last_node = new_node
        else:
            new_node.next_node = self.first_node
            new_node.previous_node = None
            self.first_node.previous_node = new_node
            self.first_node = new_node
        self.size += 1

    def pop(self):
        """pop: Returns the node from the back of the linked list and removes it

        :returns node: Node from the back of the list
        """
        node = self.last_node
        self.remove(node)
        return node

    def isIn(self, word):
        """isIn: Checks if word is in list

        :param word: string
        """
        currentNode = self.first_node
        while currentNode:
            if currentNode.data == word:
                return True
            currentNode = currentNode.next_node
        return False

    def append(self, new_node):
        """append: Add a new node to the end of the linked list

        :param new_node: Node which you want to append to the list
        """
        if self.first_node == None and self.last_node == None:
            self.first_node = new_node
            self.last_node = new_node
        else:
            new_node.next_node = None
            new_node.previous_node = self.last_node
            self.last_node.next_node = new_node
            self.last_node = new_node
        self.size += 1

    def remove(self, node):
        """remove: Remove a node from the linked list

        :param node: Node to be removed from the linked list
        """
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
        self.size -= 1

    def sort(self):
        """sort: Sorts the linked list
        """
        currentNode = self.first_node
        Sorted = False

        while not Sorted:
            Sorted = True
            while currentNode:
                if currentNode.next_node != None and currentNode.data > currentNode.next_node.data:
                    self._swap(currentNode, currentNode.next_node)
                    Sorted = False
                currentNode = currentNode.next_node
            currentNode = self.first_node

    def _swap(self, a, b):
        """_swap: Swaps the data of two elements in the linked list

        :param a:
        :param b:
        """
        tmpData = b.data
        b.data = a.data
        a.data = tmpData

    def __len__(self):
        return self.size

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
