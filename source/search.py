#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):

    for index, value in enumerate(array):
        if item == value:
            return index


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    #index position of the item in the array
    if index == len(array):             #This happens when the value was not found in the
        return
    value = array[index]
    if value == item:
        return index
    return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)

#import math 
def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    first_index = 0
    last_index = len(array)-1
    #this will iterate until it becomes continuous
    while first_index + 1 < last_index:
        half = int(last_index +first_index / 2)
         #half point in the array
        if item == array[0:half]: # the item in the array at this index are the same
            return half         # its done, found it
        if item < array[0:half]:          # the item
            last_index = half
        if item > array[0:half]:
            first_index = half



    #we care about where we start to look into
    #ALWAYS ON A SORTED ARRAY

    #find first index_value, index 0, second find last index_value, index len(array)
    #The array is check in halves and halves until it becomes 0


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
    '''
    first_index = 0
    last_index = len(array)-1

    if item is not 
    '''