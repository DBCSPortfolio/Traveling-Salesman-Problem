''' Eamonn Black - #000825575 '''

'''
    This file defines the graph data structure that is used to store location
    vertices and define edge lengths (distances) amongst these vertices.
'''

DAY_START = 8.0

# Graph
class Graph:
    def __init__(self):
        self.adjacency_list = {}
        #self.vertex_list = []
        self.edge_weights = {}
        self.route_list = []
        self.current_time = DAY_START

    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []
        #self.vertex_list.append(new_vertex)

    # adds an edge from one vertex to another, in that specific direction
    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    # adds a bidirectional edge between two vertices
    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)

    # used to find distance between two vertices
    def find_edge_length(self, from_vertex, to_vertex):
        return self.edge_weights[(from_vertex, to_vertex)]
