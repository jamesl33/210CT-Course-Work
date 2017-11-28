#!/usr/bin/python3


class binary_tree:
    def __init__(self):
        self.root = None
        self.type = None

    def __str__(self):
        return str(self.order(True))

    def max_left(self):
        current_node = self.root.left_node
        while current_node:
            if current_node.right_node is not None:
                current_node = current_node.right_node
            else:
                break
        return current_node

    def min_right(self):
        current_node = self.root.right_node
        while current_node:
            if current_node.left_node is not None:
                current_node = current_node.left_node
            else:
                break
        return current_node

    def insert(self, new_node):
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

    def count_children(self, target_node):
        count = 0
        if target_node.left_node is not None:
            count += 1
        if target_node.right_node is not None:
            count += 1
        return count

    def remove_leaf(self, target_node):
        parent = target_node.parent
        if parent.left_node == target_node:
            parent.left_node = None
        elif parent.right_node == target_node:
            parent.right_node = None

    def remove(self, target_node):
        childCount = self.count_children(target_node)
        if childCount == 0:
            if self.root == target_node:
                self.root = None
            else:
                self.remove_leaf(target_node)
        elif childCount == 1:
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
        elif childCount == 2:
            if self.root == target_node:
                if target_node.left_node is not None:
                    swap_target = self.max_left()
                elif target_node.right_node is not None:
                    swap_target = self.min_right()

                self.remove_leaf(swap_target)
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
                    swap_target = self.max_left()
                else:
                    swap_target = self.min_right()

                self.remove_leaf(swap_target)
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

    def order(self, string=False, in_order=True, pre_order=False, post_order=False, current_node=None, contents=None):
        if current_node is None:
            if self.root is None:
                return list()
            current_node = self.root
            contents = []
        if pre_order:
            if string:
                contents.append(str(current_node))
            else:
                contents.append(current_node)
        if current_node.left_node is not None:
            self.order(string, in_order, pre_order, post_order, current_node.left_node, contents)
        if in_order:
            if string:
                contents.append(str(current_node))
            else:
                contents.append(current_node)
        if current_node.right_node is not None:
            self.order(string, in_order, pre_order, post_order, current_node.right_node, contents)
        if post_order:
            if string:
                contents.append(str(current_node))
            else:
                contents.append(current_node)
        return contents

    def find(self, target, current_node=None, contents=None):
        if current_node is None:
            current_node = self.root
            contents = []
        if current_node.left_node is not None:
            self.find(target, current_node.left_node, contents)
        if current_node.value == target:
            contents.append(current_node)
        if current_node.right_node is not None:
            self.find(target, current_node.right_node, contents)
        return contents
