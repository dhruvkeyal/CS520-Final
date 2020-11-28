import pandas as pd
from search import Search
from heapq import heapify, heappop, heappush
from collections import defaultdict

class AStar(Search):
    def a_star(self):
        shortest_dist = self.shortest_dist
        open_list = [[0, self.start_node]]
        open_nodes = {self.start_node}
        heapify(open_list)
        closed_nodes = set()
        parent_node = defaultdict()
        parent_node[self.start_node] = -1
        while open_list:
            cost, curr_node = heappop(open_list)
            open_nodes.remove(curr_node)
            closed_nodes.add(curr_node)
            
            if curr_node == self.end_node:
                self.found_end(parent_node, cost)
                return
            
            for neighbor in self.Graph.neighbors(curr_node):
                if neighbor in closed_nodes:
                    continue
                estimated_cost = 0
                if self.elevation_type == "minimize":
                    estimated_cost = cost + self.get_cost(curr_node, neighbor, "elevation_gain")
                elif self.elevation_type == "maximize":
                    estimated_cost = cost + self.get_cost(curr_node, neighbor, "elevation_drop")
               
               normal_cost = cost + self.get_cost(curr_node, neighbor, "normal")
                
                if neighbor in open_nodes and normal_cost<=(1+self.x)*shortest_dist:
                    for actual_next,node_next in open_list:
                        if node_next == neighbor and (cost >= actual_next or normal_cost>=(1+self.x)*shortest_dist:
                                continue
                heappush(open_list, [estimated_cost, neighbor])
                parent_node[neighbor] = curr_node



# graph = pd.read_pickle(r'../Model/map.p')
# a = AStar(graph)
# a.a_star()
# print(a.best) 
    