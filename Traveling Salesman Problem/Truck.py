'''
    This file creates Truck objects, which contain packages and can load and deliver them
    based on the program's main algorithm. Truck objects also store current distance
    traveled on a particular run, as well as the current time at which the truck arrives at
    its current location.
'''

TRUCK_CAPACITY = 16
DAY_START = 8.0
DAY_END = 17.0

class Truck:
    def __init__(self, truck_id, start_time, num_packages=0):
        self.id = truck_id
        self.num_packages = num_packages
        self.package_list = []
        self.next_deadline = DAY_END
        self.delivery_times = []
        self.current_instance_distance = 0.0
        self.time_back_at_warehouse = start_time

    # loads a Package object onto the truck
    def add_package(self, package):
        if (len(self.package_list) < TRUCK_CAPACITY):
            package_id = package.get_id()
            self.package_list.append(package_id)
        self.num_packages = self.num_packages + 1

    # removes package from the current truck (and "delivers" it to a location)
    def deliver_package(self, package):
        if (len(self.package_list) > 0):
            package_id = package.get_id()
            self.package_list.remove(package_id)
        self.num_packages = self.num_packages - 1

    def get_id(self):
        return self.id

    def get_num_packages(self):
        return self.num_packages

    # returns list of packages currently on truck
    def get_package_list(self):
        list = ""
        for package in self.package_list:
            list = list + str(package) + "\n"
        return list

    def get_next_deadline(self):
        return self.next_deadline

    # returns distance the current truck has traveled on its particular route for one run
    def get_current_instance_distance(self):
        return self.current_instance_distance

    # sets/updates total distance traveled by a truck on one run
    def set_current_instance_distance(self, distance):
        self.current_instance_distance = distance

    # returns current time (used to track what time a truck is at a certain location)
    def get_warehouse_time(self):
        return self.time_back_at_warehouse

    # sets time a truck departs from the hub
    def set_warehouse_time(self, time):
        self.time_back_at_warehouse = time
