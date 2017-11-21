#!/usr/bin/python3

class node:
    def __init__(self, value):
        self.value = value[0]
        self.owner = value[1]
        self.parent = None
        self.leftNode = None
        self.rightNode = None

    def __ne__(self, other):
        try:
            return self.value != other.value
        except AttributeError:
            return True

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __str__(self):
        return str(self.value)
