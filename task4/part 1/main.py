#!/usr/bin/python3
"""main.py: Boilerplate code to test set finding functions
"""

from set_finding import find_largest_set, create_array


def main():
    """main: Main driver code to ask user for input then use quick_sort
    """
    array = create_array(8, 8)
    number_set = find_largest_set(array)

    for index, number in enumerate(number_set):
        if not number:
            print('There are no sets of numbers in the matrix')
        print('{0}. Number/Color = {1}\n   Set = {2}\n'.format(index + 1,
                                                               array[number[0][0]][number[0][1]],
                                                               number))


main()
