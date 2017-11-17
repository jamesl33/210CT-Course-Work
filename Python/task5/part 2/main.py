#!/usr/bin/python3

import string, linked_list

with open('paragraph.txt') as file:
    linkedLists = {}
    words = file.read().split()
    for word in words:
        word = word.translate(str.maketrans('', '', string.punctuation))
        word = word.lower()

        newNode = linked_list.node(word)

        if len(word) not in linkedLists:
            linkedLists[len(word)] = linked_list.linked_list()
            linkedLists[len(word)].append(newNode)
        else:
            if not linkedLists[len(word)].isIn(word):
                linkedLists[len(word)].append(newNode)

    for i in linkedLists:
        linkedLists[i].sort()
        print('Words of length {0}: {1}'.format(i, linkedLists[i]))
