import sys
import osmnx as ox
import networkx as nx
import pickle as p
import geopy
from geopy.geocoders import Nominatim
from Controller import *, utils
from Model import *




@Test("")
def test_get_route(Search):
    c = Search.get_route({1 : 3, 3 : 2, 2 : 4, 4 : -1}, 1)
    assert isinstance(c, list)
    assert c == [4, 2, 3, 1]


@Test("")
def test_get_cost(utility1):
    
    c = utility1.get_cost(0, 4, cost_type = "elevation_difference")
    assert isinstance(c, float)
    assert c == 3.0
    
    c = utility1.get_cost(3, 2, cost_type= "elevation_gain")
    assert isinstance(c, float)
    assert c == 0.0
    
    c = utility1.get_cost(4, 2, cost_type = "elevation_drop")
    assert isinstance(c, float)
    assert c == 2.0

    c = utility1.get_cost(2, 3, cost_type = "abs")
    assert isinstance(c, float)
    assert c == 1.0

@Test("")
def test_get_elevation(utility2):
    
    c = A.get_cost(0, 4, cost_type = "elevation_difference")
    assert isinstance(c, float)
    assert c == 3.0
    
    c = A.get_cost(3, 2, cost_type= "elevation_gain")
    assert isinstance(c, float)
    assert c == 0.0
    
    c = A.get_cost(4, 2, cost_type = "elevation_drop")
    assert isinstance(c, float)
    assert c == 2.0

    c = A.get_cost(2, 3, cost_type = "abs")
    assert isinstance(c, float)
    assert c == 1.0

if __name__ == "__main__":
   
    Graph = nx.Graph()
    # Create toy graph with nodes 0-7
    [Graph.add_node(i, elevation = 0.0) for i in range(5)]
    edges = [(0,1,1.0), (1,2,1.5), (1,4,2.0), (0,3,4.0), (4,2,3.0)]
    Graph.add_weighted_edges_from(edges)
    elevations = [0.0, 0.0,0.1,0.2,0.3]

    for i, elevation in enumerate(elevations):
        Graph.nodes[i]["elevation"] = elevation
    
    search = search.get_route()
    utility1 = utils.get_cost(Graph, x = 0.0)   
    test_get_cost(utility1)
   
