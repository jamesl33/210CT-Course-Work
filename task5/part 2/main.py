#!/usr/bin/python3
"""main.py: Read a file and create linked lists of word size containing no repeating words
"""

import string
import linked_list


def main():
    """main: Opens up a text file and creates linked lists of words
    """
    with open('paragraph.txt') as file:
        linked_lists = {}
        words = file.read().split()
        for word in words:
            word = word.translate(str.maketrans('', '', string.punctuation))
            word = word.lower()

            new_node = linked_list.Node(word)

            if len(word) not in linked_lists:
                linked_lists[len(word)] = linked_list.LinkedList()
                linked_lists[len(word)].append(new_node)
            else:
                if not linked_lists[len(word)].is_in(word):
                    linked_lists[len(word)].append(new_node)

        for i in linked_lists:
            linked_lists[i].sort()
            print('Words of length {0}: {1}'.format(i, linked_lists[i]))


main()
