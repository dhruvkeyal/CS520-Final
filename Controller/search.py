import osmnx as ox
import networkx as nx
from collections import defaultdict, deque
from heapq import heapify, heappush, heappop
import pandas as pd
import utils

'''
Class for the path search between two nodes.
This is the super class, abstraction for extensibility.
Dijkstra and AStar exdend this implementation.
'''
class Search:
    # Constructor for Search objects 
    def __init__(self, Graph, start, end, shortest_dist=None, x=0.0, elevation_type="maximize"):
        self.Graph = Graph
        self.x = x
        self.elevation_type = elevation_type
        self.start_node = start
        self.end_node = end
        self.best = [[], 0.0, float('-inf'), 0.0]
        self.shortest_dist = shortest_dist

    '''
    Resets the graph.
    Params:
        new_graph: The graph to reset to.
    '''
    def reset_graph(self, new_graph):
        self.Graph = new_graph

    '''
    Obtains the best route between two points.
    Params:
        parent_node: The start node.
        end: The end node.
    Return: The best route between two points.
    '''
    def get_route(self, parent_node, end):
        path = [end]
        curr = parent_node[end]
        # backtrack until the start is reached to find the route
        while curr!=-1:
            path.append(curr)
            curr = parent_node[curr]
        return path[::-1]

    '''
    Base condition to end the search algorithm.
    '''
    def end_search(self):
        return self.start_node == None or self.end_node == None

    '''
    Returns the best elevation.
        Params:
            parent_node: The start node.
            cost: The elevation cost of the path.
    '''
    def found_end(self, parent_node, cost):
        route = self.get_route(parent_node, self.end_node)
        elevation_dist, drop_distance = utils.get_elevation(self.Graph, route, "elevation_gain"), utils.get_elevation(self.Graph, route, "elevation_drop")
        # updates the best found route/cost and data
        self.best = [route[:], cost, elevation_dist, drop_distance]       

