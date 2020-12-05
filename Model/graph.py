import osmnx as ox
from config import API
import os
import numpy as np
import pickle as p

'''
Class for the graph of the map that the user wants to check the maximum elevation gain on.
'''
class Map:
    def __init__(self):
        self.google_key = API
        self.graph = None

    def elevation(self, graph):
        graph = ox.add_node_elevations(graph, api_key=self.google_key)
        return graph  

    '''
    Adds a node to the graph.
    Return: The graph with the added new node.
    '''
    def add_end_node(self, graph, end):
        end_node = graph.nodes[ox.get_nearest_node(graph, point=end)]
        lat_end, long_end = end_node["y"], end_node["x"]        
        for node,data in graph.nodes(data=True):
            lat_curr = graph.nodes[node]['y']
            long_curr = graph.nodes[node]['x']
            dist = self.dist_nodes(lat_end,long_end,lat_curr,long_curr)            
            data['dist_from_dest'] = dist
        return graph

    '''
    Calculates the distance between any two points on the graph.
    Return: The distance between two points.
    '''
    def dist_nodes(self, lat1, long1, lat2, long2):
        radius=6371008.8
        lat1, long1 = np.radians(lat1), np.radians(long1)
        lat2, long2 = np.radians(lat2),np.radians(long2)
        dist_long, dist_lat = long2 - long1, lat2 - lat1
        a = np.sin(dist_lat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dist_long / 2)**2
        b = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
        return radius * b

    '''
    Getter method for the graph on which the user wants to check the elevation gain.
    Return: The graph on which to check the elevation gain.
    '''
    def get_graph(self, s, e):
        self.graph = ox.graph_from_point(s, dist=10000, network_type='walk')
        self.graph = self.elevation(self.graph)                         
        p.dump(self.graph, open("map.p", "wb"))
        self.graph = self.add_end_node(self.graph, e)
        return self.graph

# g = Map()
# s = [42.3868, -72.5301]
# e = [42.22560, -72.31122]
# g.get_graph(s,e)
# print(g)