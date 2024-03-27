#!/usr/bin/python3
'''A function that finds a peak in a list of unsorted integers.'''


def find_peak(list_of_integers):
    '''a function that finds a peak in a list of unsorted integers'''
    if(list_of_integers == []):
        return None
    list_of_integers = sorted(list_of_integers)
    return list_of_integers[-1]
