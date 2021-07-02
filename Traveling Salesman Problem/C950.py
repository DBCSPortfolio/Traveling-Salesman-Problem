''' Eamonn Black - #000825575 '''

'''
    This file reads in package/location/address information and sets up
    data structures necessary for the program's algorithm to function.
'''


import csv
from package_hash_table import PackageHashTable
from vertex_hash_table import *
from Graph import *
from Package import *
from Vertex import *


class C950():
    def __init__(self):

        # sets up graph and vertices
        self.location_graph = Graph()

        self.vertex_list = []
        self.vertex_list.append(Vertex("1"))
        self.vertex_list.append(Vertex("2"))
        self.vertex_list.append(Vertex("3"))
        self.vertex_list.append(Vertex("4"))
        self.vertex_list.append(Vertex("5"))
        self.vertex_list.append(Vertex("6"))
        self.vertex_list.append(Vertex("7"))
        self.vertex_list.append(Vertex("8"))
        self.vertex_list.append(Vertex("9"))
        self.vertex_list.append(Vertex("10"))
        self.vertex_list.append(Vertex("11"))
        self.vertex_list.append(Vertex("12"))
        self.vertex_list.append(Vertex("13"))
        self.vertex_list.append(Vertex("14"))
        self.vertex_list.append(Vertex("15"))
        self.vertex_list.append(Vertex("16"))
        self.vertex_list.append(Vertex("17"))
        self.vertex_list.append(Vertex("18"))
        self.vertex_list.append(Vertex("19"))
        self.vertex_list.append(Vertex("20"))
        self.vertex_list.append(Vertex("21"))
        self.vertex_list.append(Vertex("22"))
        self.vertex_list.append(Vertex("23"))
        self.vertex_list.append(Vertex("24"))
        self.vertex_list.append(Vertex("25"))
        self.vertex_list.append(Vertex("26"))
        self.vertex_list.append(Vertex("27"))


        # reads in info in addressinfo.csv file, adds address information to each location vertex
        with open('addressinfo.csv', newline='') as csvfile:
            self.addressreader = csv.reader(csvfile)
            for row in self.addressreader:
                self.vertex_list[int(row[0]) - 1].set_address(row[1])


        self.vertex_hash_table = VertexHashTable()

        # add vertices to hash table, then graph
        for vertex in self.vertex_list:
            self.vertex_hash_table.insert(vertex)
            self.location_graph.add_vertex(vertex)

        # reads in info in locationinfo.csv file, adds weighted edges to location Graph
        with open('locationinfo.csv', newline='') as csvfile2:
            self.locationreader = csv.reader(csvfile2)
            for row in self.locationreader:
                self.location_graph.add_undirected_edge(
                    self.vertex_list[int(row[0]) - 1], self.vertex_list[int(row[1]) - 1], float(row[2]))


        # create new package hash table and empty list
        self.package_hash_table = PackageHashTable()
        self.package_list = []

        # reads in info in packageinfo.csv file, adds Package objects to empty list
        with open('packageinfo.csv', newline='') as csvfile3:
            self.packagereader = csv.reader(csvfile3)
            for row in self.packagereader:
                self.package_list.append(Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

        # inserts each Package object in the package list into the hash table
        for item in self.package_list:
            self.package_hash_table.insert(item)