import pandas as pd
from search import Search
from heapq import heapify, heappop, heappush
from collections import defaultdict
import utils
# from memory_profiler import profile

'''
Class for the Dijkstra search algorithm.
'''
class Dijkstra(Search):

    '''
    Calculates distance using the Dijkstra algorithm.
    '''
    # @profile
    def dijkstra(self):
        if self.end_seach():
            return
        Graph = self.Graph
        x = self.x
        shortest_dist = self.shortest_dist
        elevation_type = self.elevation_type

        start_node, end_node = self.start_node, self.end_node
        queue = [(0.0,0.0, start_node)]
        visited = set()
        priority = {start_node:0}
        previous_node = defaultdict()
        previous_node[start_node] = -1

        while queue:
            curr_priority, curr_distance, curr_node = heappop(queue)

            if(curr_node == end_node):
                break
            
            if(curr_node not in visited):
                visited.add(curr_node)
            
            for neighbor in Graph.neighbors(curr_node):
                if neighbor in visited:
                    continue
                prev_priority =  priority.get(neighbor, None)
                curr_edge_cost = utils.get_cost(Graph, curr_node, neighbor, "normal")
                # maximize(subtract) or minimize elevation(add)
                if(elevation_type == "maximize"):
                    if(x<=0.5):
                        next_priority = curr_edge_cost*0.1 + utils.get_cost(Graph, curr_node, neighbor, "elevation_drop")
                        next_priority += curr_priority
                    else:
                        next_priority = (curr_edge_cost*0.1 - utils.get_cost(Graph, curr_node, neighbor, "elevation_difference"))* curr_edge_cost*0.1
                else:
                        next_priority = curr_edge_cost*0.1 + utils.get_cost(Graph, curr_node, neighbor, "elevation_gain")
                        next_priority += curr_priority

                next_distance = curr_distance + curr_edge_cost

                if(not prev_priority or next_priority < prev_priority) and next_distance <= shortest_dist*(1.0+x):
                    priority[neighbor] = next_priority
                    previous_node[neighbor] = curr_node
                    heappush(queue, (next_priority, next_distance, neighbor))

        if not curr_distance:
            return
        print(previous_node)
        self.found_end(previous_node, curr_distance)

# graph = pd.read_pickle(r'../Model/map.p')
# a = Dijkstra(graph)
# a.dijkstra()
# print(a.best) 
