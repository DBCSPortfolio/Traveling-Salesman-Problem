''' Eamonn Black - #000825575 '''


'''
    This file includes a definition and functions for DeliveryInfo objects.
    A DeliveryInfo object holds a package number as well as a specific time
    at which the package was delivered.
'''

# "FOR INSERTION/LOOKUP FUNCTION: set values of hash keys to be arrays of length 6." This should already work as is? Double-check though!
from Package import *

class DeliveryInfo:
    def __init__(self, id, status_time, status):
        self.id = id
        self.status_time = status_time
        self.status = status

    def get_id(self):
        return self.id

    def get_status_time(self):
        return self.status_time

    def get_status(self):
        return self.status

    # converts float time value to a string-formatted time value
    def convert_status_time(self):
        hours = self.status_time // 1
        minutes = round((self.status_time % 1) * .60, 2)
        full_time = str(hours + minutes)
        new_time = full_time.replace(".", ":")
        if (len(new_time) - 1) - new_time.find(":") == 1:
            new_time = new_time + "0"
        return new_time

    def get_converted_time(self):
        return self.convert_status_time()

    def to_string(self):
        return (str(self.id) + ", " + self.get_status() + ", " + self.convert_status_time())