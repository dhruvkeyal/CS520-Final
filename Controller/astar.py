import pandas as pd
from search import Search
from heapq import heapify, heappop, heappush
from collections import defaultdict

class AStar(Search):
    def astar(self):
        open_list = [[0, 0, self.start_node]]
        open_nodes = {self.start_node}
        heapify(open_list)
        closed_nodes = set()
        parent_node = defaultdict()
        parent_node[self.start_node] = -1
        while open_list:
            cost, actual, curr_node = heappop(open_list)
            open_nodes.remove(curr_node)
            closed_nodes.add(curr_node)
            
            if curr_node == self.end_node:
                route = self.get_route(parent_node, self.end_node)
                elevation_dist, drop_distance = self.get_elevation(route, "elevation_gain"), self.get_elevation(route, "elevation_drop")
                self.best = [route[:], actual, elevation_dist, drop_distance]
                return
            
            for neighbor in self.Graph.neighbors(curr_node):
                if neighbor in closed_nodes:
                    continue
                estimated_cost = 0
                if self.elevation_type == "minimize":
                    estimated_cost = cost + self.get_cost(curr_node, neighbor, "elevation_gain")
                elif self.elevation_type == "maximize":
                    estimated_cost = cost + self.get_cost(curr_node, neighbor, "elevation_drop")
                else:
                    estimated_cost = cost + self.get_cost(curr_node, neighbor, "normal")
                
                if neighbor in open_nodes:
                    for estimated_next, actual_next,node_next in open_list:
                        if node_next == neighbor and cost > actual_next:
                                continue
                heappush(open_list, [estimated_cost, cost, neighbor])
                parent_node[neighbor] = curr_node

# graph = pd.read_pickle(r'../Model/map.p')
# a = AStar(graph)
# a.astar()
# print(a.best) 
    