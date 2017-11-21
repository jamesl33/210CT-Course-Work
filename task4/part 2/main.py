#!/usr/bin/python3
"""main.py: Code to use quick sort to get an input from the user and return that
indexes value from the sorted list
"""

import random
from sorting import quick_sort


def main():
    """ generate an array of length '10' sort it and as the user which element they would like """

    ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4]) # https://codegolf.stackexchange.com/questions/4707/outputting-ordinal-numbers-1st-2nd-3rd#answer-4712

    unsorted_array = []
    for i in range(10):
        unsorted_array.append(random.randint(1, 1000))
    sorted_array = quick_sort(unsorted_array)

    while True:
        try:
            element = int(input('Which element do you want to find? '))
            break
        except ValueError:
            print("Please enter a integer between 1 and {0}".format(len(sorted_array)))

    print("{0}".format(sorted_array))

    if element > len(sorted_array) // 2:
        print('The {0} largest element is {1}'.format(ordinal(element), sorted_array[element - 1]))
    else:
        print('The {0} smallest element is {1}'.format(ordinal(element), sorted_array[element - 1]))


main()
