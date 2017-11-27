#!/usr/bin/python3
""" string_converter.py: Is the file which contains the functions to convert
one string to another as cheaply as possible following a simple set of rules
"""


def levenshtein(source, target, del_cost=1, ins_cost=1, sub_cost=1):
    """levenshtein: Function to find out the distance between two strings

    :param source: The string which you want to change
    :param target: The target for which you want to make string into
    :param del_cost:
    :param ins_cost:
    :param sub_cost:
    """
    if not target:
        return len(source)
    previous_row = range(len(target) + 1)
    for source_index, source_character in enumerate(source):
        current_row = [source_index + 1]
        for target_index, target_character in enumerate(target):
            if source_character != target_character:
                substitution_cost = sub_cost
            else:
                substitution_cost = 0
            possible_deletions = previous_row[target_index + 1] + del_cost
            possible_insertions = current_row[target_index] + ins_cost
            possible_substitutions = previous_row[target_index] + substitution_cost
            current_row.append(min(possible_insertions,
                                   possible_deletions,
                                   possible_substitutions))
        previous_row = current_row
    return previous_row.pop()
