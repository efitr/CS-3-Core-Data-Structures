

from hashtable import Hashtable 

#You dont really care about retriving, its all about checking for menbership
#
class Set(object):

    def __init__(self, elements = None):
        #Or maybe should I create a HashTable with some value
        #iterate through every element of the HashTable
        #
        
        #Do I set the buckets?
            #Since the elements are keys, it seems like it
        self.elements = Hashtable.size    

    def __str__(self):
        """ Return a formatted string representation is this set """

    def __repr__(self):


    def size(self):
        #property that tracks the number of elements in constant time
        num_elements = []
        for element in Hashtable.buckets:
            for key in Hashtable.buckets.keys:
                num_elements.append(key)
        return num_elements

    @property #decorator to keep track of all the things, instead of calling the function you can just use it has a property
    def contains(element):
        #returns a bolean whether element is in this set

    def add(element):
        #add element to this set, if not present already

    def remove(element):
        #remove element from this set if present

    def union(other_set):
        #return a new set that is the union of this set and other_set

    def intersection(other_set):
        #return a new set that is the intersection of this set and other_set
        #good comment says why not what

    def difference(other_set):
        #return a new set that is the difference of this set and other_set

    def is_subset(other_set):
        #

    def test_set():
        st = Set(3)
