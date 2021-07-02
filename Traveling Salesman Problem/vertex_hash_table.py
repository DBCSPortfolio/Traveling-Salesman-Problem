''' Eamonn Black - #000825575 '''

'''
    This file creates a hash table to contain vertices, so as to easily access their
    address information for comparisons with package addresses.
'''


class VertexHashTable:
    # sets up hash table with number of locations in use
    def __init__(self, initial_capacity=27):
        self.table = []
        for i in range(1, initial_capacity + 1):
            self.table.append([])

    # inserts a vertex into a particular bucket in the hash table, based on the hash value of its label
    def insert(self, item):
        bucket = hash(int(item.get_label())) % len(self.table)
        bucket_list = self.table[bucket]

        bucket_list.append(item)

    # searches for a vertex in the hash table based on the key provided; returns vertex if found
    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        found_vertex = None
        for hashvertex in bucket_list:
            if int(hashvertex.get_label()) == key:
                found_vertex = hashvertex
            else:
                continue

        return found_vertex

    # removes a vertex from the hash table (not used in this project)
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        if key in bucket_list:
            bucket_list.remove(key)