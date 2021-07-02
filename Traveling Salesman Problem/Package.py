'''
    This file defines a Package object, which is used to hold information about
    a particular package. Attributes include ID, address, deadline, city, zip code,
    weight, and status.
'''

class Package:
    def __init__(self, id, address, deadline, city, zipcode, weight, status):
        self.id = int(id)
        self.address = address
        self.deadline = float(deadline)
        self.city = city
        self.zipcode = zipcode
        self.weight = int(weight)
        self.status = status # DELIVERED / ON TRUCK 1 / ON TRUCK 2 / ON TRUCK 3 /
                                # AVAILABLE TO 1 ONLY / AVAILABLE TO 2 ONLY / AVAILABLE TO 3 ONLY / AVAILABLE / UNAVAILABLE

    # prints a package's details
    def to_string(self):
        print(str(self.id) + "\n" +
              self.address + "\n" +
              str(self.deadline) + "\n" +
              self.city + "\n" +
              self.zipcode + "\n" +
              str(self.weight) + "\n" +
              self.status + "\n\n\n"
              )

    def get_id(self):
        return self.id

    def get_address(self):
        return self.address

    # for correcting package with incorrect address
    def set_address(self, address):
        self.address = address

    def get_deadline(self):
        return self.deadline

    def get_city(self):
        return self.city

    # for correcting package with incorrect address
    def set_city(self, city):
        self.city = city

    def get_zipcode(self):
        return self.zipcode

    # for correcting package with incorrect address
    def set_zipcode(self, zipcode):
        self.zipcode = zipcode

    def get_weight(self):
        return self.weight

    def get_status(self):
        return self.status

    # for setting status for packages when they become available for delivery/pickup, or when they are delivered
    def set_status(self, status):
        self.status = status
