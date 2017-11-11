#!/usr/bin/python3

from binary_tree import binary_tree
from node import node

class database:
    def __init__(self, students):
        self.data = {}

        for student in students:
            for value in student.data:
                newNode = node((student.data[value], student))
                if value in self.data:
                    self.data[value].insert(newNode)
                else:
                    self.data[value] = binary_tree()
                    self.data[value].insert(newNode)

    def find(self, target, where):
        if where not in self.data:
            return
        if target == '*' or target == 'all':
            return self.data[where].order()

        assert(self.data[where].type == type(target))
        return self.data[where].find(target)

    def update(self, target, where, content):
        if where == 'uniqueId':
            raise ValueError('Cannot update the uniqueId')
        assert(self.data[where].type == type(content))
        updateList = self.find(target, where)
        for student in updateList:
            student.data[where] = content

    def list(self, where):
        return self.data[where].order()
