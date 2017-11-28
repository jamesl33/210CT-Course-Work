#!/usr/bin/python3
""" binary_tree.py: File which has the class for a simple binary tree
"""


from node import Node


class BinaryTree:
    """BinaryTree: Binary tree class which can store several different datatypes
    and is used in the simple database
    """
    def __init__(self):
        self.root = None
        self.type = None

    def insert(self, new_node):
        """insert: Insert a new node into the binary tree

        :param new_node: Node which is going to be put into the tree
        """
        assert isinstance(new_node, Node)
        if self.root is None:
            self.type = type(new_node.value)
            self.root = new_node
            return

        current_node = self.root
        while current_node:
            if new_node.value < current_node.value:
                if current_node.left_node is None:
                    new_node.parent = current_node
                    current_node.left_node = new_node
                    break
                else:
                    current_node = current_node.left_node
            else:
                if current_node.right_node is None:
                    new_node.parent = current_node
                    current_node.right_node = new_node
                    break
                else:
                    current_node = current_node.right_node

    def remove(self, target_node):
        """remove: Remove a node from the tree... This is a problem function and is quite honestly
        hot garbage! And im fairly certain there is a rather catastrophic logic error 'somewhere'???

        :param target_node: Node which you want to remove from the tree
        """
        assert isinstance(target_node, Node)
        child_count = self._count_children(target_node)
        if child_count == 0:
            if self.root == target_node:
                self.root = None
            else:
                self._remove_leaf(target_node)
        elif child_count == 1:
            if self.root == target_node:
                if target_node.left_node is not None:
                    target_node.left_node.parent = None
                    self.root = target_node.left_node
                elif target_node.right_node is not None:
                    target_node.right_node.parent = None
                    self.root = target_node.right_node
            else:
                if target_node.left_node is not None:
                    parent = target_node.parent
                    target_node.left_node.parent = parent

                    if parent.left_node == target_node:
                        parent.left_node = target_node.left_node

                    if parent.right_node == target_node:
                        parent.right_node = target_node.left_node

                elif target_node.right_node is not None:
                    parent = target_node.parent
                    target_node.right_node.parent = parent

                    if parent.left_node == target_node:
                        parent.left_node = target_node.right_node

                    if parent.right_node == target_node:
                        parent.right_node = target_node.right_node
        elif child_count == 2:
            if self.root == target_node:
                if target_node.left_node is not None:
                    swap_target = self._max_left()
                elif target_node.right_node is not None:
                    swap_target = self._min_right()

                self._remove_leaf(swap_target)
                swap_target.parent = None
                swap_target.left_node = target_node.left_node
                swap_target.right_node = target_node.right_node
                self.root = swap_target

                if target_node.left_node is not None:
                    target_node.left_node.parent = swap_target
                if target_node.right_node is not None:
                    target_node.right_node.parent = swap_target
            else:
                if target_node < self.root:
                    swap_target = self._max_left()
                else:
                    swap_target = self._min_right()

                self._remove_leaf(swap_target)
                swap_target.parent = target_node.parent
                swap_target.left_node = target_node.left_node
                swap_target.right_node = target_node.right_node

                if target_node.left_node is not None:
                    target_node.left_node.parent = swap_target

                if target_node.right_node is not None:
                    target_node.right_node.parent = swap_target

                parent = target_node.parent
                if parent.left_node == target_node:
                    parent.left_node = swap_target

                if parent.right_node == target_node:
                    parent.right_node = swap_target

        target_node.left_node = None
        target_node.right_node = None
        target_node.parent = None

    def order(self, string=False, in_order=True, pre_order=False, post_order=False):
        """order: Get the binary tree in one of three orders

        :param string: Whether you want each node returned in string fromat or as a node object
        :param in_order: Return the tree values in order
        :param pre_order: Return the tree values in pre order
        :param post_order: Return the tree values in post order
        """
        if self.root is None:
            return list()

        if in_order:
            return self._in_order(string)
        elif pre_order:
            return self._pre_order(string)
        elif post_order:
            return self._post_order(string)

    def find(self, target):
        """find: Uses '_find' to traverse the tree to find 'target'

        :param target: Node which you want to find
        """
        def _find(target, current_node, contents):
            if current_node.left_node is not None:
                _find(target, current_node.left_node, contents)
            if current_node.value == target:
                contents.append(current_node)
            if current_node.right_node is not None:
                _find(target, current_node.right_node, contents)
            return contents

        return _find(target, self.root, [])

    def _in_order(self, string):
        def __in_order(string, current_node, contents):
            if current_node.left_node is not None:
                __in_order(string, current_node.left_node, contents)
            if string:
                contents.append(str(current_node))
            else:
                contents.append(current_node)
            if current_node.right_node is not None:
                __in_order(string, current_node.right_node, contents)
            return contents

        return __in_order(string, self.root, [])

    def _pre_order(self, string):
        def __pre_order(string, current_node, contents):
            if string:
                contents.append(str(current_node))
            else:
                contents.append(current_node)
            if current_node.left_node is not None:
                __pre_order(string, current_node.left_node, contents)
            if current_node.right_node is not None:
                __pre_order(string, current_node.right_node, contents)
            return contents

        return __pre_order(string, self.root, [])

    def _post_order(self, string):
        def __post_order(string, current_node, contents):
            if current_node.left_node is not None:
                __post_order(string, current_node.left_node, contents)
            if current_node.right_node is not None:
                __post_order(string, current_node.right_node, contents)
            if string:
                contents.append(str(current_node))
            else:
                contents.append(current_node)
            return contents

        return __post_order(string, self.root, [])

    def _max_left(self):
        """_max_left: Gets the node with the maximum value from the
        left side of the tree

        :return Node: Max from the left
        """
        current_node = self.root.left_node
        while current_node:
            if current_node.right_node is not None:
                current_node = current_node.right_node
            else:
                break
        return current_node

    def _min_right(self):
        """_min_right: Finds the minimum value from the right side of the tree

        :return Node: Min from right side of the tree
        """
        current_node = self.root.right_node
        while current_node:
            if current_node.left_node is not None:
                current_node = current_node.left_node
            else:
                break
        return current_node

    @classmethod
    def _count_children(cls, target_node):
        """_count_children: Counts how many children there is to any node

        :param target_node: Node which you want to find out how many children it has
        :return int: Value between 0 and 2 depending on how many children
        """
        assert isinstance(target_node, Node)
        count = 0
        if target_node.left_node is not None:
            count += 1
        if target_node.right_node is not None:
            count += 1
        return count

    @classmethod
    def _remove_leaf(cls, target_node):
        """_remove_leaf: Remove a node which has no children

        :param target_node: Node to be removed from the tree
        """
        assert isinstance(target_node, Node)
        parent = target_node.parent
        if parent.left_node == target_node:
            parent.left_node = None
        elif parent.right_node == target_node:
            parent.right_node = None

    def __str__(self):
        return str(self.order(True))
