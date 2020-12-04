# get the cost between two given nodes 
def get_cost(Graph, node_a, node_b, cost_type = "normal"):

    if not node_a or not node_b:
        return
    if cost_type == "elevation_difference":
        return Graph.nodes[node_b]["elevation"] - Graph.nodes[node_a]["elevation"]
    elif cost_type == "elevation_gain":
        return max(0.0, Graph.nodes[node_b]["elevation"] - Graph.nodes[node_a]["elevation"])
    elif cost_type =="normal":
        try : 
            return Graph.edges[node_a, node_b ,0]["length"]
        except : 
            return Graph.edges[node_a, node_b]["weight"]
    elif cost_type == "elevation_drop":
        return max(0.0, Graph.nodes[node_a]["elevation"] - Graph.nodes[node_b]["elevation"])
    else:
        return abs(Graph.nodes[node_a]["elevation"] - Graph.nodes[node_b]["elevation"])


# find elevations for the graph route using the specified elevation - minimize, maximize 
def get_elevation(Graph, route, cost_type = "both", is_total = False):
    total_elev = 0
    if is_total:
        piece_elevation = []
    for i in range(len(route)-1):
        if cost_type == "normal":
            change = get_cost(Graph, route[i], route[i+1], "normal")
        elif cost_type == "elevation_gain":
            change = get_cost(Graph, route[i], route[i+1], "elevation_gain")
        elif cost_type == "elevation_drop":
            change = get_cost(Graph, route[i], route[i+1], "elevation_drop")
        elif cost_type == "both":
            change = get_cost(Graph, route[i], route[i+1], "elevation_difference")
        total_elev += change
        if is_total:
            piece_elevation.append(change)
    if is_total:
        return total_elev, piece_elevation
    else:
        return total_elev