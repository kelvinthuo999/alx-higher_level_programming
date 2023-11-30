#!/usr/bin/python3
"""
   This function finds a peak in a list of unsorted integers.
"""

def find_peak(numbr):
    '''
        Finds the peak in a list of numbers.
    '''
    length = len(numbr)

    if length == 0:
        return None
    if length == 1:
        return numbr[0]

    low, high = 0, length - 1

    while low < high:
        mid = (low + high) // 2

        if numbr[mid] > numbr[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return numbr[low]
