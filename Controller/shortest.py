import time
import osmnx as ox
import networkx as nx
from dijkstra import Dijkstra
from astar import AStar
import utils

'''
Class for the Shortest path in the graph.
'''
class ShortestPath():

    def __init__(self, Graph, x=0.0, elevation_type="maximize"):
        self.Graph = Graph
        self.x = x
        self.elevation_type = elevation_type
        self.start_node = None
        self.end_node = None
        self.best = [[], 0.0, float('-inf'), 0.0]
        self.shortest_dist = None

    '''
    Returns the shortest distance between two points.
    Params:
        start_point: The start point.
        end_point: The end point.
    '''
    # find the shortest distance between the source and destination using the specified elevation
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


        # If x is 0 (no interest in elevation), return the found shortest path
        if(x == 0):
            return self.shortest_path_data, self.shortest_path_data
        
        self.set_best_path(elevation_type)

        # Find computational time for Dijkstra
        start = time.time()
        d = Dijkstra(Graph, self.start_node, self.end_node, self.shortest_dist)
        d.dijkstra()
        end = time.time()
        
        # Output the time for Dijkstra and log it
        print("Dijkstra Time:")
        print(end - start)

        # Set the path for Dijkstra
        dijkstra_path = self.best

        # self.set_best_path(elevation_type)
        
        # # Find computation time for A-star
        # start = time.time()
        # a = AStar(Graph, self.start_node, self.end_node, self.shortest_dist)
        # a.a_star()
        # end = time.time()

        # # Output the time for AStar and log it
        # print("AStar Time:")
        # print(end - start)

        # # # Set the path for A*
        # a_star_path = a.best
        # print(a_star_path[1])
        # print(a_star_path[2])
        # print(a_star_path[3])
        
        # # update path based on elevation type
        # if self.elevation_type == "minimize": 
        #     self.best = self.get_best_minimize(dijkstra_path, a_star_path) 
        # else: 
        #     self.best = self.get_best_maximize(dijkstra_path, a_star_path)
        
        # if (self.elevation_type == "minimize"):
        #     min = True if self.best[3] == float('-inf') else False
        # else: 
        #     max = True if self.best[2] == float('-inf') else False
        
        # if min or max: return self.shortest_path_data, [[], 0.0, 0, 0]

        # self.best[0] = [[Graph.nodes[node]['x'],Graph.nodes[node]['y']] for node in self.best[0]]

        # if (self.elevation_type == "minimize"):
        #     min = True if self.best[2] > self.shortest_path_data[2] else False
        # else: 
        #     min = True if self.best[2] < self.shortest_path_data[2] else False
        
        # if min or max: self.best = self.shortest_path_data

        return self.shortest_path_data, self.best


    '''
    Sets the best path according to maximizing or minimizing elevation gain.
    Params:
        elevation_type: The type according to which the path is required: to maximize or minimize elevation gain.
    '''
    def set_best_path(self, elevation_type):
        # initialize the best variables accoring to required elevation type
        if elevation_type == "minimize": 
            self.best = [[], 0.0, float('inf'), float('-inf')]
        else:
            self.best = [[], 0.0, float('-inf'), float('-inf')]

    '''
    Returns the path that maximizes elevation gain.
    Params:
        dijkstra_path: Path with the Dijkstra algorithm.
        a_star_path: Path with the A* algorithm.
    '''
    def get_best_maximize(self, dijkstra_path, a_star_path):
        # Find the better function among A-star and Dijkstra when maximizing
        return a_star_path if (dijkstra_path[2] != a_star_path[2] or dijkstra_path[1] > a_star_path[1]) and (dijkstra_path[2] < a_star_path[2]) else dijkstra_path

    '''
    Returns the path that minimizes elevation gain.
    Params:
        dijkstra_path: Path with the Dijkstra algorithm.
        a_star_path: Path with the A* algorithm.
    '''
    def get_best_minimize(self, dijkstra_path, a_star_path):
        # Find the better function among A-star and Dijkstra when minimizing
        return a_star_path if (dijkstra_path[2] != a_star_path[2] or dijkstra_path[1] > a_star_path[1]) and (dijkstra_path[2] > a_star_path[2]) else dijkstra_path
