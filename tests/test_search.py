import sys
import osmnx as ox
import networkx as nx
import pickle as p
import geopy
from geopy.geocoders import Nominatim
from Controller import *, utils
from Model import *

@Test("")
def test_reset_graph():

    Graph = nx.Graph()
    [Graph.add_node(i, elevation = 0.0) for i in range(5)]
    edges = [(0,1,1.0), (1,2,1.5), (1,4,2.0), (0,3,4.0), (4,2,3.0)]
    Graph.add_weighted_edges_from(edges)
    elevations = [0.0, 0.0,0.1,0.2,0.3]

    for i, elevation in enumerate(elevations):
        Graph.nodes[i]["elevation"] = elevation

    S = Search(Graph, x = 0.0, elevation_type = "maximize")

    reset_graph = nx.Graph()
    S.reset_graph(reset_graph)
    assert S.Graph == reset_graph

@Test("")
def test_end_search():

    Graph = nx.Graph()
    [Graph.add_node(i, elevation = 0.0) for i in range(5)]
    edges = [(0,1,1.0), (1,2,1.5), (1,4,2.0), (0,3,4.0), (4,2,3.0)]
    Graph.add_weighted_edges_from(edges)
    elevations = [0.0, 0.0,0.1,0.2,0.3]

    for i, elevation in enumerate(elevations):
        Graph.nodes[i]["elevation"] = elevation

    S = Search(Graph, x = 0.0, elevation_type = "maximize")

    actual_end_search = S.end_seach()

    assert False == actual_end_search

@Test("")
def test_end_search():

    Graph = nx.Graph()
    [Graph.add_node(i, elevation = 0.0) for i in range(5)]
    edges = [(0,1,1.0), (1,2,1.5), (1,4,2.0), (0,3,4.0), (4,2,3.0)]
    Graph.add_weighted_edges_from(edges)
    elevations = [0.0, 0.0,0.1,0.2,0.3]

    for i, elevation in enumerate(elevations):
        Graph.nodes[i]["elevation"] = elevation

    S = Search(Graph, x = 0.0, elevation_type = "maximize")

    actual_end_search = S.end_seach()

    assert False == actual_end_search