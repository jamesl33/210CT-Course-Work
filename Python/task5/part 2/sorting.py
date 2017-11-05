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
