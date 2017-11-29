#!/usr/bin/python3
"""main.py: Code to use quick sort to get an input from the user and return that
indexes value from the sorted list
"""

import random
from sorting import quick_sort


def ordinal(num):
    """ordinal: Generate an ordinal number representation of 'num'

    :param num: Integer which you want the ordinal representation of
    """
    if num >= 10 and num <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(num % 10, 'th')
    return str(num) + suffix


def main():
    """ generate an array of length '10' sort it and as the user which element they would like """

    sorted_array = quick_sort([random.randint(1, 1000) for i in range(10)])

    while True:
        try:
            element = int(input('Which element do you want to find? '))
            break
        except ValueError:
            print("Please enter a integer between 1 and {0}".format(len(sorted_array)))

    print("{0}".format(sorted_array))

    try:
        if element > len(sorted_array) // 2:
            print('The {0} largest element is {1}'.format(ordinal(element),
                                                          sorted_array[element - 1]))
        else:
            print('The {0} smallest element is {1}'.format(ordinal(element),
                                                           sorted_array[element - 1]))
    except IndexError:
        raise IndexError('Index is not in list')


main()
