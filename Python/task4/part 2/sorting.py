#!/usr/bin/python3

def quick_sort(array):
    """quick_sort: Use the quick sort algorithm to sort 'array'

    :param array: List of integer, should work with strings
    :output array: Sorted version of 'array'
    """
    lessList, greaterList, equalList = [], [], []
    if len(array) > 1:
        pivot_point = array[-1]
        for item in array:
            if item == pivot_point:
                equalList.append(item)
            elif item < pivot_point:
                lessList.append(item)
            else:
                greaterList.append(item)
        return quick_sort(lessList) + equalList + quick_sort(greaterList)
    else:
        return array
