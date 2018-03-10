from linkedlist import LinkedList
#add hastable 

class Set(object):

    def __init__(self, elements = None):
        init_size = 4
        self.size = 0
        self.buckets = [LinkedList() for i in range(init_size)]

    def __str__(self):
        """ Return a formatted string representation is this set """
        
    def __repr__(self):

    def _bucket_index(self, element):
        """Return the bucket index where the given key would be stored."""
        return hash(element) % len(self.buckets)

    def load_factor(self):
        return  self.size/len(self.buckets)

    def size(self):
        #property that tracks the number of elements in constant time
        num_elements = []
        for element in self.buckets:
            num_elements.append(element)
        return len(num_elements)

    def contains(self, element):
        #returns a bolean whether element is in this set
        index = self._bucket_index(element)
        bucket = self.buckets[index]

        entry = bucket.find(lambda element_value: element_value[0] == element)
        return entry is not None #entry is something, TRUE, double negation

    def add(self, element):
        #add element to this set, if not present already
        #find the bucket the given element belongs in 
        '''
        index = self._bucket_index(element)
        bucket = self.buckets[index]

        entry = bucket.find(lambda element_value: element_value[0] == element)
        if entry is not None: #this means it found it
            return 
        '''
        #OR OR OR OR OR
        #Correct
        if self.contains(element): #
        #Wrong way, this will ever ever execute, it is always false
        #if element.contains() is None:
            return
        index = self._bucket_index(element)
        bucket = self.buckets[index]
        bucket.append(element) #made another element that is not actually the array of link list

        #self.size +=1
        #Be careful, you either ogt a size property or a dynamic 

    def remove(self, element):
        #remove element from this set if present
        #This is none if the element is not present
        
        #Right way, because contains live in set class
        if self.contains(element) is None:
            return 
        #Not right
        if element.contains() is None:
            return

        index = self._bucket_index(element)
        bucket = self.buckets[index]

        entry = bucket.find(lambda element_value: element_value[0] == element)

        if entry is not None:  # Found
            # Remove the key-value entry from the bucket
            bucket.delete(entry)
            self.size -= 1
        else:  # Not found
            raise KeyError('Element not found: {}'.format(element))
        

    def union(other_set):
        #return a new set that is the union of this set and other_set

        #must get the union 

    def intersection(other_set):
        #return a new set that is the intersection of this set and other_set
        #good comment says why not what

    def difference(other_set):
        #return a new set that is the difference of this set and other_set

    def is_subset(other_set):
        #

    def test_set():
        st = Set(3)
