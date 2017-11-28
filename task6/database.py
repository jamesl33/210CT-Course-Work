#!/usr/bin/python3
""" database.py: Simple database class
"""


from binary_tree import BinaryTree
from node import Node


class Database:
    """Database: Very limited database class using binary trees to store
    date however irl I belive you would use B+ Trees and because they fan out more
    which is what is used in database software such as 'SQLite3' and filesystems
    """
    def __init__(self, students):
        """__init__

        :param students: List of studets to be added to the database
        """
        self.data = {}

        for student in students:
            for value in student.data:
                new_node = Node((student.data[value], student))
                if value in self.data:
                    self.data[value].insert(new_node)
                else:
                    self.data[value] = BinaryTree()
                    self.data[value].insert(new_node)

    def convert_node_list(self, node_list):
        """convert_node_list: Convert a list of nodes into a list of their owners

        :param node_list: List to change
        """
        return [node.owner for node in node_list]

    def find(self, target, where):
        """find: Search the database. Has simmilar structure as 'SQLite3'

        :param target: What you want to find e.g '1', 'John'
        :param where: Where you want to search e.g 'unique_id', 'name'
        """
        if where not in self.data:
            return
        if target == '*' or target == 'all':
            return self.data[where].order()

        assert self.data[where].type == type(target)
        return self.convert_node_list(self.data[where].find(target))

    def remove_by_id(self, target_id):
        """remove_by_id: Remove something from the database by id

        :param target_id: Id of the student you want to remove
        """
        for key in self.data:
            for node in self.data[key].order():
                if node.owner.data['unique_id'] == target_id:
                    self.data[key].remove(node)

    def update(self, target, where, content):
        """update: Update the records of a student in the database

        :param target: What you want to find from the database
        :param where: Where you want to search
        :param content: What you want to replace is with
        """
        if where == 'unique_id':
            raise ValueError('Cannot update the unique_id')
        assert self.data[where].type == type(content)
        update_list = self.find(target, where)
        for student in update_list:
            student.data[where] = content

    def list(self, where):
        """list: Like 'select *' in 'SQLite3' in the way that is display
        all records from 'where'

        :param where: Where you want to show the records for
        """
        return self.data[where].order(True)
