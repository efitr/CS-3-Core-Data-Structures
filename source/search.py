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
    if index == len(array):
        return None  # item was not found in the array
    if array[index] == item:
        return index  # item was found at index
    return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    first_index = 0
    last_index = len(array)-1
    #this will iterate until it becomes continuous
    if item == array[first_index]:
        return first_index
    if item == array[last_index]:
        return last_index

    while first_index <= last_index:
        half = int((last_index + first_index) / 2)
        # print('half: {}'.format(half))
         #half point in the array
        if item == array[half]: # item is equal to element in position half at the array
            return half         # if it is return the position
        #This is comparing a string against a list
        if item > array[half]:
            first_index = half + 1  # ignore left half

        #it must check smaller than it
        if item < array[half]:  
            last_index = half - 1  # ignore right half
    # print('while loop ended. first: {}, last: {}'.format(first_index, last_index))
    
   

def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
