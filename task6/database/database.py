#!/usr/bin/python3

import tree

class database:
    def __init__(self, students):
        self.data = {}

        for student in students:
            for value in student.data:
                new_node = tree.node((student.data[value], student))
                if value in self.data:
                    self.data[value].insert(new_node)
                else:
                    self.data[value] = tree.binary_tree()
                    self.data[value].insert(new_node)

    def convert_node_list(self, node_list):
        return [node.owner for node in node_list]

    def find(self, target, where):
        if where not in self.data:
            return
        if target == '*' or target == 'all':
            return self.data[where].order()

        assert self.data[where].type == type(target)
        return self.convert_node_list(self.data[where].find(target))

    def remove_by_id(self, target_id):
        for key in self.data:
            for node in self.data[key].order():
                if node.owner.data['unique_id'] == target_id:
                    self.data[key].remove(node)

    def update(self, target, where, content):
        if where == 'unique_id':
            raise ValueError('Cannot update the unique_id')
        assert self.data[where].type == type(content)
        update_list = self.find(target, where)
        for student in update_list:
            student.data[where] = content

    def list(self, where):
        return self.data[where].order(True)
