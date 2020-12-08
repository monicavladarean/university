from graph import *

graph = Graph("graph.txt")
for start in range(6):
     MST = prim(graph,start)
     # print the edges of the MST
     print("Edges:")
     for edge in MST:
          print(edge)
