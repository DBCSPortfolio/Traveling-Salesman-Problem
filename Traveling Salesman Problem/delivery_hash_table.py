'''
    This file sets up a hash table into which information regarding package delivery times
    can be inserted and from which this information can be returned.
'''

NUM_PACKAGES = 40

class DeliveryHashTable:
    # sets up hash table capacity
    def __init__(self, initial_capacity=NUM_PACKAGES):
        self.table = []
        for i in range(1, initial_capacity + 1):
            self.table.append([])

    # inserts an object into a particular hash table bucket
    def insert(self, item):
        bucket = hash(item.get_id()) % len(self.table)
        bucket_list = self.table[bucket]

        bucket_list.append(item)

    # searches for an object based on a key provided, return the matching object if it exists
    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        found_packages = []
        for hashpackage in bucket_list:
            if hashpackage.get_id() == key:
                found_packages.append(hashpackage)
            else:
                continue

        if len(found_packages) == 0:
            return None
        else:
            return found_packages
