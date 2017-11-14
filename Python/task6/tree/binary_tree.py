#!/usr/bin/python3
import sys

class binary_tree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.order(True))

    def max_left(self):
        currentNode = self.root.leftNode
        while currentNode:
            if currentNode.rightNode != None:
                currentNode = currentNode.rightNode
            else:
                break
        return currentNode

    def min_right(self):
        currentNode = self.root.rightNode
        while currentNode:
            if currentNode.leftNode != None:
                currentNode = currentNode.leftNode
            else:
                break
        return currentNode

    def insert(self, newNode):
        ''' inserts a node into the binary tree '''
        if self.root == None:
            self.type = type(newNode.value)
            self.root = newNode
            return

        currentNode = self.root
        while currentNode:
            if newNode.value < currentNode.value:
                if currentNode.leftNode == None:
                    newNode.parent = currentNode
                    currentNode.leftNode = newNode
                    break
                else:
                    currentNode = currentNode.leftNode
            else:
                if currentNode.rightNode == None:
                    newNode.parent = currentNode
                    currentNode.rightNode = newNode
                    break
                else:
                    currentNode = currentNode.rightNode

    def count_children(self, targetNode):
        ''' function returns number of children a node has '''
        count = 0
        if targetNode.leftNode != None:
            count += 1
        if targetNode.rightNode != None:
            count += 1
        return count

    def remove_leaf(self, targetNode):
        parent = targetNode.parent
        if parent.leftNode == targetNode:
            parent.leftNode = None
        elif parent.rightNode == targetNode:
            parent.rightNode = None

    def remove(self, targetNode):
        ''' function to delete a node by the id '''
        childCount = self.count_children(targetNode)
        if self.root == targetNode:
            if childCount == 0:
                self.root = None
            elif childCount == 1:
                if targetNode.leftNode != None:
                    targetNode.leftNode.parent = None
                    self.root = targetNode.leftNode
                elif targetNode.rightNode != None:
                    targetNode.rightNode.parent = None
                    self.root = targetNode.rightNode
            elif childCount == 2:
                if targetNode.leftNode != None:
                    swapTarget = self.max_left()
                elif targetNode.rightNode != None:
                    swapTarget = self.min_right()

                self.remove_leaf(swapTarget)
                swapTarget.parent = None
                swapTarget.leftNode = targetNode.leftNode
                swapTarget.rightNode = targetNode.rightNode
                self.root = swapTarget

                if targetNode.leftNode != None:
                    targetNode.leftNode.parent = swapTarget
                if targetNode.rightNode != None:
                    targetNode.rightNode.parent = swapTarget
        else:
            if childCount == 0:
                self.remove_leaf(targetNode)
            elif childCount == 1:
                if targetNode.leftNode != None:
                    parent = targetNode.parent
                    targetNode.leftNode.parent = parent

                    if parent.leftNode == targetNode:
                        parent.leftNode = targetNode.leftNode

                    if parent.rightNode == targetNode:
                        parent.rightNode = targetNode.leftNode

                elif targetNode.rightNode != None:
                    parent = targetNode.parent
                    targetNode.rightNode.parent = parent

                    if parent.leftNode == targetNode:
                        parent.leftNode = targetNode.rightNode

                    if parent.rightNode == targetNode:
                        parent.rightNode = targetNode.rightNode
            elif childCount == 2:
                if targetNode < self.root:
                    swapTarget = self.max_left()
                else:
                    swapTarget = self.min_right()

                self.remove_leaf(swapTarget)
                swapTarget.parent = targetNode.parent
                swapTarget.leftNode = targetNode.leftNode
                swapTarget.rightNode = targetNode.rightNode

                if targetNode.leftNode != None:
                    targetNode.leftNode.parent = swapTarget

                if targetNode.rightNode != None:
                    targetNode.rightNode.parent = swapTarget

                parent = targetNode.parent
                if parent.leftNode == targetNode:
                    parent.leftNode = swapTarget

                if parent.rightNode == targetNode:
                    parent.rightNode = swapTarget

        targetNode.leftNode = None
        targetNode.rightNode = None
        targetNode.parent = None

    def order(self, string=False, inOrder=True, preOrder=False, postOrder=False, currentNode=None, contents=None):
        ''' returns a python list with the contents of the binary tree in either pre/post/in order '''
        if currentNode == None:
            if self.root == None:
                return list()
            currentNode = self.root
            contents = []
        if preOrder:
            if string:
                contents.append(str(currentNode))
            else:
                contents.append(currentNode)
        if currentNode.leftNode != None:
            self.order(string, inOrder, preOrder, postOrder, currentNode.leftNode, contents)
        if inOrder:
            if string:
                contents.append(str(currentNode))
            else:
                contents.append(currentNode)
        if currentNode.rightNode != None:
            self.order(string, inOrder, preOrder, postOrder, currentNode.rightNode, contents)
        if postOrder:
            if string:
                contents.append(str(currentNode))
            else:
                contents.append(currentNode)
        return contents

    def find(self, target, currentNode=None, contents=None):
        ''' returns a python list of students which match the target '''
        if currentNode == None:
            currentNode = self.root
            contents = []
        if currentNode.leftNode != None:
            self.find(target, currentNode.leftNode, contents)
        if currentNode.value == target:
            contents.append(currentNode)
        if currentNode.rightNode != None:
            self.find(target, currentNode.rightNode, contents)
        return contents
