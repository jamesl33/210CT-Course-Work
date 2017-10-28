#!/usr/bin/python3

def quick_sort(array):
    """ Use the quick sort algorithm to sort 'array'
    input:
        list: list of integers
    output:
        list: list of sorted integers created using the input list 'array'
    """

    lessList, greaterList, equalList = [], [], []
    if len(array) > 1:
        pivot_point = array[-1]

        for item in array:
            if item == pivot_point:
                equalList.append(item) # catch the item in the list which is the pivot point
            elif item < pivot_point:
                lessList.append(item) # create a list which has all elements less than the pivot point in
            else:
                greaterList.append(item) # create a list which has all elements greater than the pivot point in

        return quick_sort(lessList) + equalList + quick_sort(greaterList) # recursive call using the three lists created
    else:
        return array

import unittest

class UnitTest(unittest.TestCase):
    def test_quick__sort(self):
        unsortedList = [1,5,2,6,8,5,234,5645,234,6,4,756,234,2,3,4,656,7,234]
        self.assertEqual(quick_sort(unsortedList), [1, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7, 8, 234, 234, 234, 234, 656, 756, 5645])

        unsortedList = [5, 3, 2, 72, 5, 7, 23]
        self.assertEqual(quick_sort(unsortedList), [2, 3, 5, 5, 7, 23, 72])

        unsortedList = [1,2,3,4,5,6,7,8,9]
        self.assertEqual(quick_sort(unsortedList), [1,2,3,4,5,6,7,8,9])

if __name__ == '__main__':
    unittest.main()
