'''
    This file sets up a hash table to contain packages for efficient querying.
'''


NUM_PACKAGES = 40

class PackageHashTable:
    def __init__(self, initial_capacity=NUM_PACKAGES):
        self.table = []
        for i in range(1, initial_capacity + 1):
            self.table.append([])

    # inserts a package object into a hash table bucket, based on the package id and its corresponding hash value
    def insert(self, item):
        bucket = hash(item.get_id()) % len(self.table)
        bucket_list = self.table[bucket]

        bucket_list.append(item)

    # searches for a package in the hash table and returns the package if found
    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        found_package = None
        for hashpackage in bucket_list:
            if hashpackage.get_id() == key:
                found_package = hashpackage
            else:
                continue

        return found_package

    # removes a package from the hash table entirely (not used in this project)
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        if key in bucket_list:
            bucket_list.remove(key)
