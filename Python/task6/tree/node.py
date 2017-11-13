#!/usr/bin/python3

class node:
    def __init__(self, value):
        self.value = value[0]
        self.owner = value[1]
        self.parent = None
        self.leftNode = None
        self.rightNode = None

    def __eq__(self, other):
        if other == None:
            return False
        assert isinstance(other, node)
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other

    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        return str(self.value)
