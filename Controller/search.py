from collections import defaultdict, deque
from heapq import heapify, heappush, heappop
# import pandas as pd

class Search:

    def __init__(self, Graph, x=0.0, elevation_type="maximize"):
        self.Graph = Graph
        self.x = x
        self.elevation_type = elevation_type
        self.start_node = None
        self.end_node = None
        self.best = [[], 0.0, float('-inf'), 0.0]
    
    def reset_graph(self, new_graph):
        self.Graph = new_graph
    
    def get_cost(self, node_a, node_b, cost_type = "normal"):

        def cost_normal():
            try : 
                return Graph.edges[node_a, node_b ,0]["length"]
            except : 
                return Graph.edges[node_a, node_b]["weight"]
        
        def cost_diff():
            return Graph.nodes[node_b]["elevation"] - Graph.nodes[node_a]["elevation"]
        
        def cost_gain():
            return max(0.0, Graph.nodes[node_b]["elevation"] - Graph.nodes[node_a]["elevation"])
        
        def cost_drop():
            return max(0.0, Graph.nodes[node_a]["elevation"] - Graph.nodes[node_b]["elevation"])
        
        def cost_default():
            return abs(Graph.nodes[node_a]["elevation"] - Graph.nodes[node_b]["elevation"])

        Graph = self.Graph
        if node_a is None or node_b is None : 
            return 
            
        switcher = {
            "normal": cost_normal(),
            "elevation_diff": cost_diff(),
            "elevation_gain": cost_gain(),
            "elevation_drop" : cost_drop()
        }
        return abs(Graph.nodes[node_a]["elevation"] - Graph.nodes[node_b]["elevation"])


    def get_elevation(self, route, cost_type = "both", is_total = False):

        def val_elev_normal():
            return self.get_cost(route[i], route[i+1], "normal")

        def val_elev_diff():
            return self.get_cost(route[i], route[i+1], "elevation_difference")
    
        def val_elev_gain():
            return self.get_cost(route[i], route[i+1], "elevation_gain")

        def val_elev_drop():
            return self.get_cost(route[i], route[i+1], "elevation_drop")

        total_elev = 0
        if not is_total:
            piece_elevation = []
        for i in range(len(route)-1):
            diff = 0
            switcher = {
                "normal": val_elev_normal(),
                "elevation_drop": val_elev_drop(),
                "elevation_gain": val_elev_gain(),
                "both" : val_elev_diff()
            }
            diff = switcher.get(cost_type, lambda: 0)
            total_elev += diff
            if not is_total:
                piece_elevation.append(diff)
        if not is_total:
            return total_elev, piece_elevation
        else:
            return total_elev
    

    def get_route(self, parent_node, end):
        
        path = [end]
        curr = parent_node[end]
        while curr!=-1:
            path.append(curr)
            curr = parent_node[curr]
        return path[::-1]

    def end_seach(self):
        return not (self.start_node == None or self.end_node == None)

    def dijkstra(self):

        if not self.start_node or not self.end_node:
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
                curr_edge_cost = self.get_cost(curr_node, neighbor, "normal")
                # maximize(subtract) or minimize elevation(add)
                if(elevation_type == "maximize"):
                    if(x<=0.5):
                        next_priority = curr_edge_cost*0.1 + self.get_cost(curr_node, n, "elevation_drop")
                        next_priority += curr_priority
                    else:
                        next_priority = (curr_edge_cost*0.1 - self.get_cost(curr_node, n, "elevation_difference"))* edge_len*0.1
                else:
                        next_priority = curr_edge_cost*0.1 + self.get_cost(curr_node, n, "elevation_gain")
                        next_priority += curr_priority

                next_distance = curr_distance + curr_edge_cost

                if(not prev_priority or next_priority < prev_priority) and next_distance <= shortest_dist*(1.0+x):
                    priority[neighbor] = next_priority
                    previous_node[neighbor] = curr_node
                    heappush(queue, (next_priority, next_distance, neighbour))

        if not curr_distance:
            return
            
        route = self.get_route(previous_node, self.end_node)
        elevation_dist, drop_distance = self.get_elevation(route, "elevation_gain"), self.get_elevation(route, "elevation_drop")
        self.best = [route[:], curr_distance, elevation_dist, drop_distance]            


# graph = pd.read_pickle('../Model/map.p')
# s = [42.3868, -72.5301]
# e = [42.22560, -72.31122]
# graph = g.get_graph(s,e)
# a = Search(graph)
# a.dijkstra()
# print(a.best) 
