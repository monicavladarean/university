import re

class Graph:
    def __init__(self, path):

        file = open(path, "r")
        p = re.compile("\d+")

        self.vertices, self.edges = map(int, p.findall(file.readline()))

        self.graph = [[0]*self.vertices for _ in range(self.vertices)]

        for i in range(self.edges):
            u, v, weight = map(int, p.findall(file.readline()))
            self.graph[u][v] = weight
            self.graph[v][u] = weight
    def cost(self,x,y):
        return self.graph[x][y]

# prim's algorithm
def prim(G,start):
    #Input: a weighted graph G
    #Output: the MST made from the graph G, using Prim's algorithm

    # initialize the MST and the set of nodes
    cost=0
    MST = list()
    nodes = set()

    # we begin from the "first" vertex (0)
    nodes.add(start)
    while len(nodes) != G.vertices:
        crossing = set()
        # for each element x in nodes, we add the edge (x, k) to crossing if k is not in nodes
        for x in nodes:
            for k in range(G.vertices):
                if k not in nodes and G.graph[x][k] != 0:
                    crossing.add((x, k))
        # find the edge with the smallest weight in crossing
        edge = sorted(crossing, key=lambda e:G.graph[e[0]][e[1]])[0]
        cost+=G.cost(edge[0],edge[1])
        # add this edge to MST
        MST.append(edge)
        # add the new vertex to nodes
        nodes.add(edge[1])
    print("Cost:",cost)

    return MST