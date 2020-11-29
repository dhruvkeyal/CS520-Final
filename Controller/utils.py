def get_cost(Graph, node_a, node_b, cost_type = "normal"):
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

    if node_a is None or node_b is None : 
        return 
    
    switcher = {
        "normal": cost_normal(),
        "elevation_diff": cost_diff(),
        "elevation_gain": cost_gain(),
        "elevation_drop" : cost_drop()
    }
    return abs(Graph.nodes[node_a]["elevation"] - Graph.nodes[node_b]["elevation"])


def get_elevation(Graph, route, cost_type = "both", is_total = False):
    def val_elev_normal():
        return get_cost(Graph, route[i], route[i+1], "normal")
    def val_elev_diff():
        return get_cost(Graph, route[i], route[i+1], "elevation_difference")
    def val_elev_gain():
        return get_cost(Graph, route[i], route[i+1], "elevation_gain")
    def val_elev_drop():
        return get_cost(Graph, route[i], route[i+1], "elevation_drop")

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

