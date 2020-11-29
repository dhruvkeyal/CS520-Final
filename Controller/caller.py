from shortest import ShortestPath
import pandas as pd

graph = pd.read_pickle('../Model/map.p')
sp = ShortestPath(graph)
s = [42.3868, -72.5301]
e = [42.22560, -72.31122]
path, best = sp.get_shortest_distance(s,e,0)
# print(path)
# print(best)