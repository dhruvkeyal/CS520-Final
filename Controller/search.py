
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
    



    def get_elevation(self, route, cost_type = "both", is_total = False):

        def val_elev_normal():
            return self.get_cost_switch(route[i], route[i+1], "normal")

        def val_elev_diff():
        return self.get_cost_switch(route[i], route[i+1], "elevation_difference")
    
        def val_elev_gain():
            return self.get_cost_switch(route[i], route[i+1], "elevation_gain")

        def val_elev_drop():
            return self.get_cost_switch(route[i], route[i+1], "elevation_drop")

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

    def dijkstra(self):

        if not self.start_node or not self.end_node:
            return
        
        
