#!/usr/bin/python3

from linked_list import linked_list
from node import node
import string

with open('paragraph.txt') as file:
    linkedLists = {}
    words = file.read().split()
    for word in words:
        # In this case we are not worried about punctuation and capital letters
        word = word.translate(str.maketrans('', '', string.punctuation))
        word = word.lower()

        newNode = node(word)

        if len(word) not in linkedLists:
            linkedLists[len(word)] = linked_list()
            linkedLists[len(word)].append(newNode)
        else:
            linkedLists[len(word)].append(newNode)

    for i in linkedLists:
        linkedLists[i].sort()
        print('Words of length {0}: {1}'.format(i, linkedLists[i]))
