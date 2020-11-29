import time
import osmnx as ox
import networkx as nx
from dijkstra import Dijkstra
from astar import AStar
import utils

class ShortestPath():

    def __init__(self, Graph, x=0.0, elevation_type="maximize"):
        self.Graph = Graph
        self.x = x
        self.elevation_type = elevation_type
        self.start_node = None
        self.end_node = None
        self.best = [[], 0.0, float('-inf'), 0.0]
        self.shortest_dist = None

    def get_shortest_distance(self, start_point, end_point, x, elevation_type = "minimize"):
        Graph = self.Graph
        self.x  = x/100
        self.elevation_type = elevation_type
        self.start_node = None
        self.end_node = None

        self.start_node, distance1 = ox.get_nearest_node(Graph, point=start_point, return_dist = True)
        self.end_node, distance2 = ox.get_nearest_node(Graph, point=end_point, return_dist = True)

        self.shortest_route = nx.shortest_path(Graph, source = self.start_node, target = self.end_node, weight = 'length')
        self.shortest_dist  = sum(ox.utils_graph.get_route_edge_attributes(Graph, self.shortest_route, 'length'))
        
        self.shortest_latitude_longitude = [[Graph.nodes[node]['x'],Graph.nodes[node]['y']] for node in self.shortest_route] 
        
        self.shortest_path_data = [self.shortest_latitude_longitude, self.shortest_dist, \
                            utils.get_elevation(Graph, self.shortest_route, "elevation_gain"), utils.get_elevation(Graph, self.shortest_route, "elevation_drop")]

        if(x == 0):
            return self.shortest_path_data, self.shortest_path_data
        
        set_best_path(elevation_type)

        start = time.time()
        d = Dijkstra(Graph)
        d.dijkstra()
        end = time.time()
        dijkstra_path = self.best

        set_best_path(elevation_type)
        
        start = time.time()
        a = AStar(Graph)
        a.a_star()
        end = time.time()
        a_star_path = self.best

        if self.elevation_type == "minimize": 
            self.best = get_best_minimize(dijkstra_path, a_star_path) 
        else: 
            self.best = get_best_maximize(dijkstra_path, a_star_path)
        
        if (self.elevation_type == "minimize"):
            min = True if self.best[3] == float('-inf') else False
        else: 
            max = True if self.best[2] == float('-inf') else False
        
        if min or max: return shortest_path_data, [[], 0.0, 0, 0]

        self.best[0] = [[Graph.nodes[node]['x'],Graph.nodes[node]['y']] for node in self.best[0]]

        if (self.elevation_type == "minimize"):
            min = True if self.best[2] > shortest_path_data[2] else False
        else: 
            min = True if self.best[2] < shortest_path_data[2] else False
        
        if min or max: self.best = shortest_path_data

        return shortest_path_data, self.best

    
    def set_best_path(self, elevation_type):
        if elevation_type == "minimize": 
            self.best = [[], 0.0, float('inf'), float('-inf')]
        else:
            self.best = [[], 0.0, float('-inf'), float('-inf')]
    
    def get_best_maximize(self, dijkstra_path, a_star_path):
        return a_star_path if (dijkstra_path[2] != a_star_path[2] or dijkstra_path[1] > a_star_path[1]) and (dijkstra_path[2] < a_star_path[2]) else dijkstra_path
        
    def get_best_minimize(self, dijkstra_path, a_star_path):
        return a_star_path if (dijkstra_path[2] != a_star_path[2] or dijkstra_path[1] > a_star_path[1]) and (dijkstra_path[2] > a_star_path[2]) else dijkstra_path
