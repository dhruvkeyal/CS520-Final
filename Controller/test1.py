import sys
# import osmnx as ox
import networkx as nx
import pickle as p
# import geopy
# from geopy.geocoders import Nominatim
# from Controller import *
# from Model import *
from search import Search
import utils
from dijkstra import Dijkstra
from shortest import ShortestPath
from astar import AStar
import unittest

# @Test("")
def test_get_route(S):
    print("route")
    c = S.get_route({1 : 3, 3 : 2, 2 : 4, 4 : -1}, 1)
    print(c)
    assert isinstance(c, list)
    assert c == [4, 2, 3, 1]

    c = S.get_route({2 : 3, 4 : 1, 3 : 4, 1 : -1}, 2 )
    assert isinstance(c, list)

    assert c == [1, 4 ,3 ,2]
    print(c)

# @Test("")
def test_get_cost(Graph):
    print("Testing the cost function")

    c = utils.get_cost(Graph, 0, 4, cost_type = "elevation_difference")
    assert isinstance(c, float)
    assert c == 0.3
    
    c = utils.get_cost(Graph, 3, 2, cost_type= "elevation_gain")
    assert isinstance(c, float)
    assert c == 0.0

    c = utils.get_cost(Graph, 2, 3, cost_type= "elevation_gain")
    assert isinstance(c, float)
    assert c == 0.1
    
    c = utils.get_cost(Graph, 4, 2, cost_type = "elevation_drop")
    assert isinstance(c, float)
    assert c == 0.2

    c = utils.get_cost(Graph, 2, 3)
    assert isinstance(c, float)
    assert c == 0.1

# @Test("")
def test_get_elevation(Graph):
    print("elevation")
    c = utils.get_cost(Graph, 0, 4, cost_type = "elevation_difference")
    assert isinstance(c, float)
    assert c == 0.3
    
    c = utils.get_cost(Graph, 3, 2, cost_type= "elevation_gain")
    assert isinstance(c, float)
    assert c == 0.0

    c = utils.get_cost(Graph, 2, 3, cost_type= "elevation_gain")
    assert isinstance(c, float)
    assert c == 0.1
    
    c = utils.get_cost(Graph, 4, 2, cost_type = "elevation_drop")
    assert isinstance(c, float)
    assert c == 0.2



# @Test("")
def test_get_shortest_distance(S):
    print("shortest")
    start_point = (24.3334, -32.5248)
    end_point = (25.3948, -42.5366)

    shortest_path, best_path = S.get_shortest_distance(start_point, end_point,S.x, elevation_type =  "maximize")
    assert best_path[1] <= (1 + S.x/100.0)*shortest_path[1]
    assert best_path[2] >= shortest_path[2]

    start_point = (24.3334, -32.5248)
    end_point = (25.3948, -42.5366)

    shortest_path, best_path = S.get_shortest_distance(start_point, end_point,S.x, elevation_type =  "minimize")
    assert best_path[1] <= (1 + S.x/100.0)*shortest_path[1]
    assert best_path[2] <= shortest_path[2]

if __name__ == "__main__":
   
    # Create a graph with 0 - 4 nodes
    Graph = nx.Graph()
    [Graph.add_node(i, elevation = 0.0) for i in range(5)]
    edges = [(0,1,1.0), (1,2,1.5), (1,4,2.0), (0,3,4.0), (4,2,3.0)]
    Graph.add_weighted_edges_from(edges)
    elevations = [0.0, 0.0,0.1,0.2,0.3]

    for i, elevation in enumerate(elevations):
        Graph.nodes[i]["elevation"] = elevation
    
    S = Search(Graph, x = 0.0, elevation_type = "maximize")
    # test_get_route(S)

    test_get_cost(Graph)
    # test_get_elevation(Graph)

    # S = ShortestPath(Graph, x = 50.0, elevation_type="maximize")
    # test_get_shortest_distance(S)

    D = Dijkstra(Graph, x = 0.0, elevation_type = "maximize")

    A = AStar(Graph, x = 0.0, elevation_type = "maximize")



