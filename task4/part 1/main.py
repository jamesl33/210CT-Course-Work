#!/usr/bin/python3
"""main.py: Boilerplate code to test set finding functions
"""

from set_finding import find_largest_set, create_array


def main():
    """main: Main driver code to ask user for input then use quick_sort
    """
    array = create_array(8, 8)
    number_set = find_largest_set(array)

    for i in range(len(number_set)):
        if not number_set[i]:
            print("There are no sets of numbers in this matrix")
        print("{0}. Number/Color = {1}\n   Set = {2}\n".format(i + 1, array[number_set[i][0][0]]
                                                               [number_set[i][0][1]], number_set[i]))


main()
