'''
    This file defines a vertex object, which is used to designate locations and
    store address information. Vertex objects are linked in this project with
    the use of the Graph object
'''

class Vertex:
    def __init__(self, label):
        self.label = label
        self.address = ''
        self.visited = True

    def get_label(self):
        return self.label

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    # returns True for "visited", False for "unvisited"
    def get_visit_status(self):
        return self.visited

    # allows for a vertex's visit status to be changed/set
    def set_visit_status(self, status):
        self.visited = status
