#!/usr/bin/python3

import random
from sorting import quick_sort

ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4]) # https://codegolf.stackexchange.com/questions/4707/outputting-ordinal-numbers-1st-2nd-3rd#answer-4712

def main():
    """ generate an array of length '10' sort it and as the user which element they would like """
    unsortedArray = []
    for i in range(10):
        unsortedArray.append(random.randint(1, 1000))
    sortedArray = quick_sort(unsortedArray)

    while True:
        try:
            element = int(input('Which element do you want to find? '))
            break
        except ValueError:
            print("Please enter a integer between 1 and {0}".format(len(sortedArray)))

    print("\n{0}".format(sortedArray))

    if element > len(sortedArray) // 2:
        print('The {0} largest element is {1}'.format(ordinal(element), sortedArray[element - 1]))
    else:
        print('The {0} smallest element is {1}'.format(ordinal(element), sortedArray[element - 1]))

main()
