#!/usr/bin/python3
"""sorting.py: Simple implimentation of the quick sort algorithm
"""


def quick_sort(array):
    """quick_sort: Use the quick sort algorithm to sort 'array'

    :param array: List of integer, should work with strings
    :output array: Sorted version of 'array'
    """
    less_list, greater_list, equal_list = [], [], []
    if len(array) > 1:
        pivot_point = array[-1]
        for item in array:
            if item == pivot_point:
                equal_list.append(item)
            elif item < pivot_point:
                less_list.append(item)
            else:
                greater_list.append(item)
        return quick_sort(less_list) + equal_list + quick_sort(greater_list)
    return array
