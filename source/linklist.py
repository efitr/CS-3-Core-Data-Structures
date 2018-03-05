from node import Node

class LinkedList(object):
    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        self.size = 0

    if iterable is not None:
        for item in iterable:
            self.append(item)

    def __str__(self):
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))
    
    def __repr__(self):
        return 'LinkedList({!r})'.format(self.items())

#++++++++++++++++++++++List of all items in linked list++++++++++++++++++++++
    ''' Runtime:  ''' 
    def items(self):
        result = []
        node = self.head

        while node is not None:
            result.append(node.data)
            node = node.next

        return result

    def is_empty(self):
        return self.head is None

    def lenght(self):
        node_count = 0
        node = self.head

        while node is not None:
            node_count += 1
            node = node.next 
        
        return node_count

    def get_at_index(self, index):
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))

        node = self.head
        for iterator in range(index):
            node = node.next
            data = node.data
        return data

    def insert_at_index(self, index, item):
        if not (0 <= index <= self.size):
            raise ValueError('List index out of range: {}'.format(index))

        new_node = Node(item)

        if index == 0:
            self.prepend(item)
        
        if index == self.size:
            self.append(item)
        
        if 0 < index < self.size:
            node = self.head
            before_node = None

            for iterator in range(index):
                before_node = node
                node = node.next
            
            before_node.next = new_node
            new_node.next = node
            self.size += 1

    def prepend(self,item):
        new_node = Node(item)
        if self.is_empty():
            self.tail = new_node
        else:
            new_node.next = self.head
        
        self.head = new_node
    
    def find(self, quality):
        node = self.head
        while node is not None:
            if quality(node.data):
                return node.data
            
            node = node.next
        return None
    
    def replace(self, old_item, new_item):
        #change the item
        #new_

    def delete(self, item):
        node = self.head
        previous = None
        found = False 

        while not found and node is not None:

            if node.data == item:
                found = True
            else:
                previous = node
                node = node.next
        
        if found:
            if node is not self.head and node is not self.tail:
                previous.next = node.next
                node.next = None
            
            if node is self.head:
                self.head = node.next
                node.next = None
            
            if node is self.tail:
                if previous is not None:
                    previous.next = None
                self.tail = previous
        
        else:
            raise ValueError('Item not found: {}'.format(item))

def test_linked_list():
    ll = LinkedList()
    print(ll)

        print('Appending items:')
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))

    print('Getting items by index:')
    for index in range(ll.size):
        item = ll.get_at_index(index)
        print('get_at_index({}): {!r}'.format(index, item))

    print('Deleting items:')
    ll.delete('B')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('A')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()

