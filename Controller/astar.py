import pandas as pd
from search import Search
from heapq import heapify, heappop, heappush
from collections import defaultdict
import utils
# from memory_profiler import profile

'''
Class for the A* search algorithm.
Inherits the "Search" class from search.py
'''
class AStar(Search):

    '''
    Calculates using the A* algorithm.
    profiler to get the space usage for a_star function
    '''
    # @profile
    def a_star(self):
        shortest_dist = self.shortest_dist
        open_list = [[0, self.start_node]]
        open_nodes = [self.start_node]
        # Using priority queue to get minimum cost nodes (shortest)
        heapify(open_list)
        closed_nodes = set()
        parent_node = defaultdict()
        parent_node[self.start_node] = -1
        # While nodes are available to explore
        while open_list:
            cost, curr_node = heappop(open_list)
            open_nodes.remove(curr_node)
            closed_nodes.add(curr_node)
            
            if curr_node == self.end_node:
                self.found_end(parent_node, cost)
                return
            
            # find all neighbors and add to the open list
            for neighbor in self.Graph.neighbors(curr_node):
                if neighbor in closed_nodes:
                    continue
                estimated_cost = 0
                if self.elevation_type == "minimize":
                    estimated_cost = cost + utils.get_cost(self.Graph, curr_node, neighbor, "elevation_gain")
                elif self.elevation_type == "maximize":
                    estimated_cost = cost + utils.get_cost(self.Graph, curr_node, neighbor, "elevation_drop")
               
                normal_cost = cost + utils.get_cost(self.Graph, curr_node, neighbor, "normal")
                
                if neighbor in open_nodes:# and normal_cost<=(1+self.x)*shortest_dist:
                    # find if neighbor already in open list, update only if score is less
                    for actual_next,node_next in open_list:
                        if node_next == neighbor and (cost >= actual_next):# or normal_cost>=(1+self.x)*shortest_dist):
                                continue
                heappush(open_list, [estimated_cost, neighbor])
                open_nodes.append(neighbor)
                parent_node[neighbor] = curr_node
    