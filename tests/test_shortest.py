import sys
import osmnx as ox
import networkx as nx
import pickle as p
import geopy
from geopy.geocoders import Nominatim
from Controller import *, utils
from Model import *

@Test("")
def test_set_best_path_for_maximize():

    Graph = nx.Graph()
    [Graph.add_node(i, elevation = 0.0) for i in range(5)]
    edges = [(0,1,1.0), (1,2,1.5), (1,4,2.0), (0,3,4.0), (4,2,3.0)]
    Graph.add_weighted_edges_from(edges)
    elevations = [0.0, 0.0,0.1,0.2,0.3]

    for i, elevation in enumerate(elevations):
        Graph.nodes[i]["elevation"] = elevation

    S = ShortestPath(Graph, x = 0.0, elevation_type = "maximize")

    S.set_best_path("maximize")

    expected_best = [[], 0.0, float('-inf'), float('-inf')]

    assert expected_best == S.best

@Test("")
def test_set_best_path_for_minimize():

    Graph = nx.Graph()
    [Graph.add_node(i, elevation = 0.0) for i in range(5)]
    edges = [(0,1,1.0), (1,2,1.5), (1,4,2.0), (0,3,4.0), (4,2,3.0)]
    Graph.add_weighted_edges_from(edges)
    elevations = [0.0, 0.0,0.1,0.2,0.3]

    for i, elevation in enumerate(elevations):
        Graph.nodes[i]["elevation"] = elevation

    S = ShortestPath(Graph, x = 0.0, elevation_type = "minimize")

    S.set_best_path("minimize")

    expected_best = [[], 0.0, float('-inf'), float('-inf')]

    assert expected_best == S.best

@Test("")
def test_get_best_maximize():

    Graph = nx.Graph()
    [Graph.add_node(i, elevation = 0.0) for i in range(5)]
    edges = [(0,1,1.0), (1,2,1.5), (1,4,2.0), (0,3,4.0), (4,2,3.0)]
    Graph.add_weighted_edges_from(edges)
    elevations = [0.0, 0.0,0.1,0.2,0.3]

    for i, elevation in enumerate(elevations):
        Graph.nodes[i]["elevation"] = elevation

    S = ShortestPath(Graph, x = 0.0, elevation_type = "minimize")

    dijkstra_path = [1, 2, 3, 4]
    a_star_path = [4, 5, 6, 7]

    assert dijkstra_path == S.get_best_maximize(dijkstra_path, a_star_path)

    dijkstra_path = [1, 2, 3, 4]
    a_star_path = [4, 5, 2, 7]

    assert a_star_path == S.get_best_maximize(dijkstra_path, a_star_path)

@Test("")
def test_get_best_minimize():

    Graph = nx.Graph()
    [Graph.add_node(i, elevation = 0.0) for i in range(5)]
    edges = [(0,1,1.0), (1,2,1.5), (1,4,2.0), (0,3,4.0), (4,2,3.0)]
    Graph.add_weighted_edges_from(edges)
    elevations = [0.0, 0.0,0.1,0.2,0.3]

    for i, elevation in enumerate(elevations):
        Graph.nodes[i]["elevation"] = elevation

    S = ShortestPath(Graph, x = 0.0, elevation_type = "minimize")

    dijkstra_path = [1, 2, 3, 4]
    a_star_path = [4, 5, 6, 7]

    assert a_star_path == S.get_best_minimize(dijkstra_path, a_star_path)

    dijkstra_path = [1, 2, 3, 4]
    a_star_path = [4, 5, 2, 7]

    assert dijkstra_path == S.get_best_minimize(dijkstra_path, a_star_path)
