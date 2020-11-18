import osmnx as ox
from config import API
import os
import numpy as np
import pickle as p

class Map:
    def __init__(self):
        self.google_key = API
        self.graph = None
    
    def elevation(self, graph):
        graph = ox.add_node_elevations(graph, api_key=self.google_key)
        return Graph  

    def dist_nodes(self,lat1,long1,lat2,long2):
        radius=6371008.8 # Earth radius
        lat1, long1 = np.radians(lat1), np.radians(long1)
        lat2, long2 = np.radians(lat2),np.radians(long2)
        dlong,dlat = long2 - long1,lat2 - lat1
        temp1 = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlong / 2)**2
        temp2 = 2 * np.arctan2(np.sqrt(temp1), np.sqrt(1 - temp1))
        return radius * temp2

    def add_end_node(self, graph, end):
        end_node = graph.nodes[ox.get_nearest_node(graph, point=end)]
        lat_end, long_end = end_node["y"], end_node["x"]        
        for node,data in graph.nodes(data=True):
            lat_curr = graph.nodes[node]['y']
            long_curr = graph.nodes[node]['x']
            dist = self.dist_nodes(lat_end,long_end,lat_curr,long_curr)            
            data['dist_from_dest'] = dist
        return graph

    def get_graph(self, s, e):
        self.graph = ox.graph_from_point(s, distance=10000, network_type='walk')
        self.graph = self.elevation_graph(self.graph)                         
        p.dump(self.graph, open("map.p", "wb"))
        self.graph = self.add_end_node(self.graph, e)
        return self.graph