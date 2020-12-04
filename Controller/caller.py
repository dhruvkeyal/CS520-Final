from shortest import ShortestPath
import pandas as pd

# File for calling the search algorithms

# Load the cached map
graph = pd.read_pickle('../Model/map.p')
sp = ShortestPath(graph)

# start and end point for the search
s = [42.374471, -72.491495]
e = [42.084108, -72.761578]

path, best = sp.get_shortest_distance(s,e,60)
# print("path:", path)
# print("best: ", best)