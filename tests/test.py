import sys
import osmnx as ox
import networkx as nx
import pickle as p
import geopy
from geopy.geocoders import Nominatim
from Controller import *
from Model import *




@Test("")
def test_get_route(Search):
    c = Search.get_route({1 : 3, 3 : 2, 2 : 4, 4 : -1}, 1)
    assert isinstance(c, list)
    assert c == [4, 2, 3, 1]