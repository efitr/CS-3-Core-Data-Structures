
class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def __rps__(self):
        return 'Node({!r})'.format(self.data)
