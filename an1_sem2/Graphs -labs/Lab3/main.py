# 2. Write a program that, given a graph with positive costs and two vertices,
# finds a lowest cost walk between the given vertices, using a
# "backwards" Dijkstra algorithm (Dijkstra algorithm that searches backwards, from the ending vertex).

from graph import Graph
from alg import *

graph = Graph("graph1k.txt")
x = int(input("x:"))
y = int(input("y: "))
if dijkstra(graph, x, y, graph.getCosts()) == None:
    print("No path!")
else:
    print(dijkstra(graph, x, y, graph.getCosts()))