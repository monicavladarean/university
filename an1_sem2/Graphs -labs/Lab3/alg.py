import heapq

def getPath(prev, final):
        #preconditions: prev is the dictionary of parent nodes for each node of a graph and final is the final node of a path
        #returns a list of vertices representign the shortest path from final to start
        #returns a list of nodes

    path = []
    if final not in prev:
        return None # the path could not be found
    while final != None:
        path.append(final)
        final = prev[final]
    return path

def dijkstra(graph, start, final, costs):
    """
        preconditions:
            - graph is the graph on which we find the shortest path
            - start is the starting node of the path
            - final is the end point of the path
            - costs is the cost dictionary, having as keys pairs of vertices representing edges x->y

        returns a tuple made of path(a list of vertices representing the mincost path) and pCost(the cost of the path) / None if there is no path between the given vertices
    """
    dist = {}
    prev = {}
    prev[final] = None
    q = []
    dist[final] = 0
    heapq.heappush(q, (dist[final], final))
    while len(q) > 0:
        dummy, x = heapq.heappop(q)
        if(dummy == dist[x]):
            for y in graph.parseIn(x):
                if y not in prev or dist[y] > dist[x] + costs[(y, x)]:
                    prev[y] = x
                    dist[y] = dist[x] + costs[(y, x)]
                    heapq.heappush(q, (dist[y], y))
    if getPath(prev, start) is None:
        return None
    return (getPath(prev, start), dist[start])