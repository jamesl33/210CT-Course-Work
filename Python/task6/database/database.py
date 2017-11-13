#!/usr/bin/python3

import tree

class database:
    def __init__(self, students):
        self.data = {}

        for student in students:
            for value in student.data:
                newNode = tree.node((student.data[value], student))
                if value in self.data:
                    self.data[value].insert(newNode)
                else:
                    self.data[value] = tree.binary_tree()
                    self.data[value].insert(newNode)

    def convert_node_list(self, nodeList):
        studentList = []
        for i in nodeList:
            studentList.append(i.owner)
        return studentList

    def find(self, target, where):
        if where not in self.data:
            return
        if target == '*' or target == 'all':
            return self.data[where].order()

        assert(self.data[where].type == type(target))
        return self.convert_node_list(self.data[where].find(target))

    def update(self, target, where, content):
        if where == 'uniqueId':
            raise ValueError('Cannot update the uniqueId')
        assert(self.data[where].type == type(content))
        updateList = self.find(target, where)
        for student in updateList:
            student.data[where] = content

    def list(self, where):
        return self.data[where].order()
