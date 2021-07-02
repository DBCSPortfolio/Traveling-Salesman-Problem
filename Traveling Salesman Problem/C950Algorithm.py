'''
    This file contains the main algorithm for generating possible trucks,
    finding routes for these trucks, and officially delivering all packages.
'''

from C950 import *
from Truck import Truck
import random
from delivery_info import DeliveryInfo
from delivery_hash_table import DeliveryHashTable

# constant values used for calculations, etc.
MAX_VALUE = 15
DAY_START = 8.0
DAY_END = 17.0
TRUCK_SPEED = 18.0
TRUCK_CAPACITY = 16
NUM_PACKAGES = 40
NUM_LOCATIONS = 27

class C950Algorithm:

    def __init__(self):
        self.running_finalized_distance = 0.0
        self.temp_distance = 0.0
        self.current_time = DAY_START
        self.temp_time = DAY_START
        self.temp = C950()
        self.status_list = []
        self.status_list_flag = False
        self.delivery_hash_table = DeliveryHashTable()
        self.packages_left = NUM_PACKAGES
        self.first_time_flag = False
        self.second_time_flag = False



    # used to randomly select any leftover available packages for a truck that isn't full
    def generate_random(self, range):
        return random.randrange(range)

    # used as a reference for existing package statuses if a potential truck instance is scrapped
    def generate_status_list(self):
        for b in range(1, NUM_PACKAGES + 1):
            self.status_list.append(self.temp.package_hash_table.search(b).get_status())

    # resets package statuses if a potential truck instance is scrapped
    def reset_status_list(self):
        for c in range(0, NUM_PACKAGES):
            self.temp.package_hash_table.search(c + 1).set_status(self.status_list[c])


    # generates a truck object and loads it with packages, based on package statuses and truck capacity
    def generate_temp_truck(self, truck_id, start_time):
        # generates status list if it hasn't already been created
        if self.status_list_flag == False:
            self.status_list_flag = True
            self.generate_status_list()
        temp_truck = Truck(truck_id, start_time, 0) # creation of individual truck instance
        # runs through all packages, evaluating for status and availability
        for i in range(1, NUM_PACKAGES + 1):
            package = self.temp.package_hash_table.search(i)
            if temp_truck.num_packages == TRUCK_CAPACITY:
                break  # truck is full
            if truck_id == 1:
                # loads packages 13, 14, 15, 16, 19, and 20 at once, since they have to be together on one truck
                if (i == 19 and self.temp.package_hash_table.search(19).get_status() != "Delivered"
                        and temp_truck.num_packages <= 10):
                    package_13 = self.temp.package_hash_table.search(13)
                    package_14 = self.temp.package_hash_table.search(14)
                    package_15 = self.temp.package_hash_table.search(15)
                    package_16 = self.temp.package_hash_table.search(16)
                    package_19 = self.temp.package_hash_table.search(19)
                    package_20 = self.temp.package_hash_table.search(20)
                    package_13.set_status("On Truck 1")
                    temp_truck.add_package(package_13)
                    package_14.set_status("On Truck 1")
                    temp_truck.add_package(package_14)
                    package_15.set_status("On Truck 1")
                    temp_truck.add_package(package_15)
                    package_16.set_status("On Truck 1")
                    temp_truck.add_package(package_16)
                    package_19.set_status("On Truck 1")
                    temp_truck.add_package(package_19)
                    package_20.set_status("On Truck 1")
                    temp_truck.add_package(package_20)
                    continue
                elif i == 20:
                    continue # it will have already been loaded or passed over by the time the loop gets to 20
                # takes everything with a set deadline that's available to this truck number
                elif (package.deadline < DAY_END and package.status != "Delivered" and package.status != "Unavailable"
                        and package.status != "Available to 2 only" and package.status != "Available to 3 only"
                        and package.status != "On Truck 2" and package.status != "On Truck 3"):
                    if (i == 13 or i == 14 or i == 15 or i == 16):
                        continue # these will be handled with package #19
                    else:
                        self.temp.package_hash_table.search(i).set_status("On Truck 1")
                        temp_truck.add_package(package)
                # takes everything only available to the truck in question
                elif package.status == "Available to 1 only":
                    if (i == 13 or i == 14 or i == 15 or i == 16):
                        continue # these will be handled with package #19
                    else:
                        self.temp.package_hash_table.search(i).set_status("On Truck 1") # package is now on truck
                        temp_truck.add_package(package) # loads package onto truck if it meets criteria
            elif truck_id == 2:
                # loads packages 13, 14, 15, 16, 19, and 20 at once, since they have to be together on one truck
                if (i == 19 and self.temp.package_hash_table.search(19).get_status() != "Delivered"
                        and temp_truck.num_packages <= 10):
                    package_13 = self.temp.package_hash_table.search(13)
                    package_14 = self.temp.package_hash_table.search(14)
                    package_15 = self.temp.package_hash_table.search(15)
                    package_16 = self.temp.package_hash_table.search(16)
                    package_19 = self.temp.package_hash_table.search(19)
                    package_20 = self.temp.package_hash_table.search(20)
                    package_13.set_status("On Truck 2")
                    temp_truck.add_package(package_13)
                    package_14.set_status("On Truck 2")
                    temp_truck.add_package(package_14)
                    package_15.set_status("On Truck 2")
                    temp_truck.add_package(package_15)
                    package_16.set_status("On Truck 2")
                    temp_truck.add_package(package_16)
                    package_19.set_status("On Truck 2")
                    temp_truck.add_package(package_19)
                    package_20.set_status("On Truck 2")
                    temp_truck.add_package(package_20)
                    continue
                elif i == 20:
                    continue # it will have already been loaded or passed over by the time the loop gets to 20
                # takes everything with a set deadline that's available to this truck number
                elif (package.deadline < DAY_END and package.status != "Delivered" and package.status != "Unavailable"
                      and package.status != "Available to 1 only" and package.status != "Available to 3 only"
                      and package.status != "On Truck 1" and package.status != "On Truck 3"):
                    if (i == 13 or i == 14 or i == 15 or i == 16):
                        continue # these will be handled with package #19
                    else:
                        self.temp.package_hash_table.search(i).set_status("On Truck 2")
                        temp_truck.add_package(package)
                # takes everything only available to the truck in question
                elif package.status == "Available to 2 only":
                    if (i == 13 or i == 14 or i == 15 or i == 16):
                        continue # these will be handled with package #19
                    else:
                        self.temp.package_hash_table.search(i).set_status("On Truck 2") # package is now on truck
                        temp_truck.add_package(package) # loads package onto truck if it meets criteria
            elif truck_id == 3:
                # loads packages 13, 14, 15, 16, 19, and 20 at once, since they have to be together on one truck
                if (i == 19 and self.temp.package_hash_table.search(19).get_status() != "Delivered" and temp_truck.num_packages <= 10):
                    package_13 = self.temp.package_hash_table.search(13)
                    package_14 = self.temp.package_hash_table.search(14)
                    package_15 = self.temp.package_hash_table.search(15)
                    package_16 = self.temp.package_hash_table.search(16)
                    package_19 = self.temp.package_hash_table.search(19)
                    package_20 = self.temp.package_hash_table.search(20)
                    package_13.set_status("On Truck 3")
                    temp_truck.add_package(package_13)
                    package_14.set_status("On Truck 3")
                    temp_truck.add_package(package_14)
                    package_15.set_status("On Truck 3")
                    temp_truck.add_package(package_15)
                    package_16.set_status("On Truck 3")
                    temp_truck.add_package(package_16)
                    package_19.set_status("On Truck 3")
                    temp_truck.add_package(package_19)
                    package_20.set_status("On Truck 3")
                    temp_truck.add_package(package_20)
                    continue
                elif i == 20:
                    continue # it will have already been loaded or passed over by the time the loop gets to 20
                # takes everything with a set deadline that's available to this truck number
                elif (package.deadline < DAY_END and package.status != "Delivered" and package.status != "Unavailable"
                        and package.status != "Available to 1 only" and package.status != "Available to 2 only"
                        and package.status != "On Truck 1" and package.status != "On Truck 2"):
                    if (i == 13 or i == 14 or i == 15 or i == 16):
                        continue # these will be handled with package #19
                    else:
                        self.temp.package_hash_table.search(i).set_status("On Truck 3")
                        temp_truck.add_package(package)
                # takes everything only available to the truck in question
                elif package.status == "Available to 3 only":
                    if (i == 13 or i == 14 or i == 15 or i == 16):
                        continue # these will be handled with package #19
                    else:
                        self.temp.package_hash_table.search(i).set_status("On Truck 3") # package is now on truck
                        temp_truck.add_package(package) # loads package onto truck if it meets criteria
        available_list = []
        # filters packages down to list of only ones that have a status of "Available"
        for z in range(1, NUM_PACKAGES + 1):
            if self.temp.package_hash_table.search(z).get_status() == "Available":
                available_list.append(z)
        while (temp_truck.num_packages < TRUCK_CAPACITY and len(available_list) > 0):
            # in order to create multiple options for one truck at a given time, randomly selected packages are added
            temp_pack_num = self.generate_random(len(available_list))
            temp_pack = self.temp.package_hash_table.search(available_list[temp_pack_num])
            if truck_id == 1:
                temp_pack.set_status("On Truck 1")
                temp_truck.add_package(temp_pack)
                available_list.remove(available_list[temp_pack_num])
            elif truck_id == 2:
                temp_pack.set_status("On Truck 2")
                temp_truck.add_package(temp_pack)
                available_list.remove(available_list[temp_pack_num])
            elif truck_id == 3:
                temp_pack.set_status("On Truck 3")
                temp_truck.add_package(temp_pack)
                available_list.remove(available_list[temp_pack_num])
        return temp_truck



    # graph traversal - continually finds the nearest delivery location for a truck until all packages are delivered
    def find_nearest_neighbor(self, truck: Truck):
        current_location = self.temp.vertex_hash_table.search(1)  # starting location = hub
        # set only relevant vertices to False ("unvisited")
        for i in range (1, NUM_LOCATIONS + 1):
            temp_vertex = self.temp.vertex_hash_table.search(i)
            for package in truck.package_list:
                if temp_vertex.get_address() == self.temp.package_hash_table.search(package).get_address():
                    temp_vertex.set_visit_status(False)
        # loops until all packages on a truck instance are delivered
        while len(truck.package_list) > 0:
            # placeholder values for shortest distance and its associated vertex
            current_shortest_edge_length = 5000000
            current_shortest_edge_vertex = None
            # loops through all graph locations to find location shortest distance from the current location
            for j in range (1, NUM_LOCATIONS + 1):
                temp_location = self.temp.vertex_hash_table.search(j)
                if temp_location.get_visit_status():  # if true ("visited," so not relevant for the current truck)
                    continue
                else:
                    # finds edge length between truck's location and current vertex
                    test_edge_length = self.temp.location_graph.find_edge_length(current_location, temp_location)
                    # if the edge is shorter than the current leader, replace it and its associated vertex identifier
                    if test_edge_length <= current_shortest_edge_length:
                        current_shortest_edge_length = test_edge_length
                        current_shortest_edge_vertex = int(temp_location.get_label())
            deliver_list = [] # list of packages delivered, in the order they were delivered
            # "delivers" package to the location the shortest distance away from the current location
            for package in truck.package_list:
                temp_package = self.temp.package_hash_table.search(package)
                if self.temp.vertex_hash_table.search(current_shortest_edge_vertex).get_address() == temp_package.get_address():
                    # adds delivery time for a package to the current truck's list of delivery times
                    truck.delivery_times.append(DeliveryInfo(package, (truck.get_warehouse_time() + (current_shortest_edge_length / TRUCK_SPEED)), "Delivered"))
                    temp_package.set_status("Delivered")
                    deliver_list.append(package)
            # removes delivered package from the truck's list of packages
            for item in deliver_list:
                truck.package_list.remove(item)
            # sets new "current location" and sets corresponding vertex to "visited"
            current_location = self.temp.vertex_hash_table.search(current_shortest_edge_vertex)
            current_location.set_visit_status(True)
            # updates distance traveled and current time
            self.temp_distance = self.temp_distance + current_shortest_edge_length
            truck.set_warehouse_time(truck.get_warehouse_time() + (current_shortest_edge_length / TRUCK_SPEED))
        # travels back to package hub and updates distance traveled and current time
        back_to_hub = self.temp.location_graph.find_edge_length(current_location, self.temp.vertex_hash_table.search(1))
        self.temp_distance = self.temp_distance + back_to_hub
        truck.set_warehouse_time(truck.get_warehouse_time() + (back_to_hub / TRUCK_SPEED))
        self.reset_status_list() # resets packages' original statuses, in case current truck instance is scrapped
        return self.temp_distance

    # generates 5 separate trucks for a particular truck number, then chooses the one with the lowest distance
    def select_best_truck(self, truck_id, start_time):
        number_of_trucks = 5
        temp_truck_list = []
        current_lowest_distance = 5000000  # find a replacement for this if possible.
        current_best_truck = None # stores truck with lowest distance among the five generated
        for truck in range(number_of_trucks):
            temp_truck = self.generate_temp_truck(truck_id, start_time)
            temp_truck_list.append(temp_truck) # not really needed

            # runs package delivery algorithm on each truck, updating when a new "lowest distance" truck has been found
            self.temp_distance = self.find_nearest_neighbor(temp_truck)
            if self.temp_distance < current_lowest_distance:
                current_lowest_distance = self.temp_distance
                current_best_truck = temp_truck
            self.temp_distance = 0.0

        # updates official delivery times for all packages that were on the winning truck instance
        for package in current_best_truck.delivery_times:
            self.delivery_hash_table.insert(DeliveryInfo(package.get_id(), start_time, "On Truck " + str(truck_id)))
            self.delivery_hash_table.insert(package)
        # sets all delivered packages to "Delivered" status, and updates the official status list to match
        for package in current_best_truck.delivery_times:
            self.temp.package_hash_table.search(package.get_id()).set_status("Delivered")
            self.status_list[package.get_id() - 1] = "Delivered"
            self.packages_left = self.packages_left - 1 # updates (decrements) total number of packages left to deliver
        current_best_truck.set_current_instance_distance(current_lowest_distance)
        # updates official total distance
        self.running_finalized_distance = self.running_finalized_distance + current_lowest_distance
        return current_best_truck # returns best truck object of the 5 generated

    # updates statuses of all packages that are "Unavailable" at the start of the day, along with truck departure time
    def update_current_time(self, time):
        new_time = time
        if self.first_time_flag == False:
            self.first_time_flag = True
            if new_time < 9.0833:
                new_time = 9.1 # to differentiate available/on truck status, plus to somehow account for load time
            if self.temp.package_hash_table.search(6).status == "Unavailable":
                self.temp.package_hash_table.search(6).set_status("Available")
                self.status_list[5] = "Available"
                self.delivery_hash_table.insert(DeliveryInfo(6, 9.0833, "Available"))
            if self.temp.package_hash_table.search(25).status == "Unavailable":
                self.temp.package_hash_table.search(25).set_status("Available")
                self.status_list[24] = "Available"
                self.delivery_hash_table.insert(DeliveryInfo(25, 9.0833, "Available"))
            if self.temp.package_hash_table.search(28).status == "Unavailable":
                self.temp.package_hash_table.search(28).set_status("Available")
                self.status_list[27] = "Available"
                self.delivery_hash_table.insert(DeliveryInfo(28, 9.0833, "Available"))
            if self.temp.package_hash_table.search(32).status == "Unavailable":
                self.temp.package_hash_table.search(32).set_status("Available")
                self.status_list[31] = "Available"
                self.delivery_hash_table.insert(DeliveryInfo(32, 9.0833, "Available"))
        elif self.second_time_flag == False:
            self.second_time_flag = True
            if new_time < 10.3333:
                new_time = 10.4 # to differentiate available/on truck status, plus to somehow account for load time
            if self.temp.package_hash_table.search(9).status == "Unavailable":
                self.temp.package_hash_table.search(9).set_address("410 S State St")
                self.temp.package_hash_table.search(9).set_city("Salt Lake City")
                self.temp.package_hash_table.search(9).set_zipcode("84111")
                self.temp.package_hash_table.search(9).set_status("Available")
                self.status_list[8] = "Available"
                self.delivery_hash_table.insert(DeliveryInfo(9, 10.3333, "Available"))
        return new_time


    # runs the full algorithm, finding a total distance required for delivering all 40 packages
    def find_working_route(self):
        for y in range (1, NUM_PACKAGES + 1):
            temp_info = DeliveryInfo(y, DAY_START, (self.temp.package_hash_table.search(y).get_status()))
            self.delivery_hash_table.insert(temp_info)
        truck_one = self.select_best_truck(1, DAY_START)
        truck_two = self.select_best_truck(2, DAY_START)
        truck_three = self.select_best_truck(3, DAY_START)
        print("Truck 1 Distance: " + str(round(truck_one.get_current_instance_distance(), 2)))
        print("Truck 2 Distance: " + str(round(truck_two.get_current_instance_distance(), 2)))
        print("Truck 3 Distance: " + str(round(truck_three.get_current_instance_distance(), 2)))
        while self.packages_left > 0:
            current_time_1 = truck_one.get_warehouse_time()
            current_time_2 = truck_two.get_warehouse_time()
            current_time_3 = truck_three.get_warehouse_time()
            new_time_1 = current_time_1
            new_time_2 = current_time_2
            new_time_3 = current_time_3

            # finds which truck is first to return to the hub while all 3 are out in the field, then loads it again
            if (current_time_1 <= current_time_2):
                if (current_time_1 <= current_time_3):
                    # if 1 is the lowest
                    new_time_1 = self.update_current_time(current_time_1)
                    truck_one = self.select_best_truck(1, new_time_1)
                    print("Truck 1 Distance: " + str(round(truck_one.get_current_instance_distance(), 2)))
                else:
                    new_time_3 = self.update_current_time(current_time_3)
                    truck_three = self.select_best_truck(3, new_time_3)
                    print("Truck 3 Distance: " + str(round(truck_three.get_current_instance_distance(), 2)))
            elif (current_time_2 <= current_time_3):
                # if 2 is the lowest
                new_time_2 = self.update_current_time(current_time_2)
                truck_two = self.select_best_truck(2, new_time_2)
                print("Truck 2 Distance: " + str(round(truck_two.get_current_instance_distance(), 2)))
            else:
                # if 3 is the lowest
                new_time_3 = self.update_current_time(current_time_3)
                truck_three = self.select_best_truck(3, new_time_3)
                print("Truck 3 Distance: " + str(round(truck_three.get_current_instance_distance(), 2)))

        print("\nFINAL DISTANCE: " + str(round((self.running_finalized_distance), 2)) + " miles\n")


    def find_status_at_time(self, package, time):
        # assumes a valid time between 8:00 (AM) and 5:00 (PM) is entered - very naive assumption though
        if package != "SHOWALL" and (int(package) < 1 or int(package) > 40):
            print("\nError: invalid package number entered.\n")
        if time != "ALLTIMES":
            minutes = int(time[-2:])
            int_minutes = minutes / 60.0
            hours = int(time.split(':')[0])
            time_number = hours + int_minutes
        if package != "SHOWALL" and time != "ALLTIMES":
            package_details = (self.temp.package_hash_table.search(int(package)).get_address() + ", " +
                  str(self.temp.package_hash_table.search(int(package)).get_deadline()) + ", " +
                  self.temp.package_hash_table.search(int(package)).get_city() + ", " +
                  self.temp.package_hash_table.search(int(package)).get_zipcode() + ", " +
                  str(self.temp.package_hash_table.search(int(package)).get_weight()))
            # THIS HAS TO BE ADDED TO ALL BRANCHES, NOT JUST TWO OF THEM
            # CHECK ALL OF THESE AGAIN PRIOR TO SUBMITTING
            print("\n")
            sought_package = self.delivery_hash_table.search(int(package))
            correct_status = None
            for entry in sought_package:
                if time_number >= entry.get_status_time():
                    correct_status = entry
            print(str(correct_status.get_id()) + ", " + package_details + ", " + correct_status.get_status() + " -- updated at " + correct_status.get_converted_time())
            print("\n")
        elif package == "SHOWALL" and time != "ALLTIMES":
            print("\n")
            for x in range(1, NUM_PACKAGES + 1):
                package_details = (self.temp.package_hash_table.search(x).get_address() + ", " +
                                   str(self.temp.package_hash_table.search(x).get_deadline()) + ", " +
                                   self.temp.package_hash_table.search(x).get_city() + ", " +
                                   self.temp.package_hash_table.search(x).get_zipcode() + ", " +
                                   str(self.temp.package_hash_table.search(x).get_weight()))
                temp_list = self.delivery_hash_table.search(x)
                correct_status = None
                for entry in temp_list:
                    if time_number >= entry.get_status_time():
                        correct_status = entry
                print(str(correct_status.get_id()) + ", " + package_details + ", " + correct_status.get_status() + " -- updated at " + correct_status.get_converted_time())
            print("\n")
        elif package != "SHOWALL" and time == "ALLTIMES":
            package_details = (self.temp.package_hash_table.search(int(package)).get_address() + ", " +
                               str(self.temp.package_hash_table.search(int(package)).get_deadline()) + ", " +
                               self.temp.package_hash_table.search(int(package)).get_city() + ", " +
                               self.temp.package_hash_table.search(int(package)).get_zipcode() + ", " +
                               str(self.temp.package_hash_table.search(int(package)).get_weight()))

            print("\n")
            sought_package = self.delivery_hash_table.search(int(package))
            for entry in sought_package:
                print((str(entry.get_id()) + ", " + package_details + ", " + entry.get_status() + " -- updated at " + entry.get_converted_time()))
            print("\n")
        elif package == "SHOWALL" and time == "ALLTIMES":
            print("\n")
            for x in range(1, NUM_PACKAGES + 1):
                package_details = (self.temp.package_hash_table.search(x).get_address() + ", " +
                                   str(self.temp.package_hash_table.search(x).get_deadline()) + ", " +
                                   self.temp.package_hash_table.search(x).get_city() + ", " +
                                   self.temp.package_hash_table.search(x).get_zipcode() + ", " +
                                   str(self.temp.package_hash_table.search(x).get_weight()))
                temp_list = self.delivery_hash_table.search(x)
                for entry in temp_list:
                    print(str(entry.get_id()) + ", " + package_details + ", " + entry.get_status() + " -- updated at " + entry.get_converted_time())
            print("\n")


# MAKE SURE TO LINK THIS TO REST OF PACKAGE ATTRIBUTES SO ALL DETAILS ARE PRINTED, PER SPECS
# MAKE SURE TO FIX FOR TIMES FROM 1:00 - 5:00





def main():
    instance2 = C950Algorithm()
    instance2.find_working_route()

    while True:
        package_num = input("To search for one package, please enter a package number between 1 and 40.\n"
              + "To show all packages, type \"SHOWALL\". Type \"Exit\" to quit at any time.    ")
        if package_num.upper() == "EXIT":
            break
        time = input("To select a time, please type in a time in the format HH:MM between 8:00 (AM) and\n"
                     + "5:00 (PM). To show all timestamps for the package(s) you selected, type \"ALLTIMES\". Type \"Exit\" to quit at any time.    ")
        if time.upper() == "EXIT":
            break
        instance2.find_status_at_time(package_num, time)
    print("Thank you for using our package delivery tracking system.")


if __name__ == '__main__':
    main()
