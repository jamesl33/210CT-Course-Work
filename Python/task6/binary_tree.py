#!/usr/bin/python3

class binary_tree:
    def __init__(self):
        self.size = 0
        self.root = None

    def __str__(self):
        return str(self.order())

    def __len__(self):
        return self.size

    def minimum(self):
        ''' helper function to get the minimum value from the tree '''
        currentNode = self.root
        while currentNode:
            if currentNode.leftNode != None:
                currentNode = currentNode.leftNode
            else:
                break
        return currentNode

    def maximum(self):
        ''' helper function to get the maximum value from the tree '''
        currentNode = self.root
        while currentNode:
            if currentNode.rightNode != None:
                currentNode = currentNode.rightNode
            else:
                break
        return currentNode

    def insert(self, newNode):
        ''' inserts a node into the binary tree '''
        if self.root == None:
            self.type = type(newNode.value)
            self.root = newNode
            self.size += 1
            return

        currentNode = self.root
        while currentNode:
            if newNode.value < currentNode.value:
                if currentNode.leftNode == None:
                    newNode.parentNode = currentNode
                    currentNode.leftNode = newNode
                    self.size += 1
                    break
                else:
                    currentNode = currentNode.leftNode
            else:
                if currentNode.rightNode == None:
                    newNode.parentNode = currentNode
                    currentNode.rightNode = newNode
                    self.size += 1
                    break
                else:
                    currentNode = currentNode.rightNode

    def remove_leaf(self, targetNode):
        ''' function to remove leaf node by address '''
        parent = targetNode.parentNode
        if parent.leftNode == targetNode:
            parent.leftNode = None
        else:
            parent.rightNode = None

    def count_children(self, targetNode):
        ''' function returns number of children a node has '''
        count = 0
        if targetNode.leftNode != None:
            count += 1
        elif targetNode.rightNode != None:
            count += 1
        return count

    def swap(self, nodeA, nodeB):
        tmpValue = nodeA.value
        tmpOwner = nodeA.owner
        nodeA.value = nodeB.value
        nodeA.owner = nodeB.owner
        nodeB.value = tmpValue
        nodeB.owner = tmpOwner

    def remove(self, targetId):
        ''' function to delete a node by the id '''
        pass

    def order(self, inOrder=True, preOrder=False, postOrder=False, currentNode=None, contents=None):
        ''' returns a python list with the contents of the binary tree in either pre/post/in order '''
        if currentNode == None:
            currentNode = self.root
            contents = []
        if preOrder:
            contents.append(str(currentNode))
        if currentNode.leftNode != None:
            self.order(inOrder, preOrder, postOrder, currentNode.leftNode, contents)
        if inOrder:
            contents.append(str(currentNode))
        if currentNode.rightNode != None:
            self.order(inOrder, preOrder, postOrder, currentNode.rightNode, contents)
        if postOrder:
            contents.append(str(currentNode))
        return contents

    def find(self, target, currentNode=None, contents=None):
        ''' returns a python list of students which match the target '''
        if currentNode == None:
            currentNode = self.root
            contents = []
        if currentNode.leftNode != None:
            self.find(target, currentNode.leftNode, contents)

        if currentNode.value == target:
            contents.append(currentNode.owner)

        if currentNode.rightNode != None:
            self.find(target, currentNode.rightNode, contents)
        return contents
