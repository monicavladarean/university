class Graph():
    def __init__(self, file_name):
        self.ins={}
        self.outs={}
        self.costs={}

        f = open(file_name, "r")
        lines = f.read().split("\n")
        self.vertices=int(lines[0].split()[0])
        for i in range(self.vertices):
            self.ins[i] = []
            self.outs[i] = []
        self.read_graph(file_name)

    def read_graph(self, file_name):
        #reands a graph from the file
        #preconditions: file_name - name.txt, from where it takes all the information about the graph

        f = open(file_name, "r")
        lines = f.readline().strip()
        lines = f.readline().strip()
        while lines != "":
            line = lines.split(" ")
            x = int(line[0])
            y = int(line[1])
            cost = int(line[2])

            self.ins[y].append(x)
            self.outs[x].append(y)
            self.costs[(x, y)] = cost
            lines = f.readline().strip()

    def add_edge(self,x,y,c):
        # adds an edge to the graph, if this doesn't already exist. if it exists, it exits the function
        # preconditions: x,y - an integers, 2 vertexes and c - integer, the cost

        if self.exist_edge(x,y):
            return False
        if self.exist_vertex(x)==False or self.exist_vertex(y)==False:
            return False
        self.ins[y].append(x)
        self.outs[x].append(y)
        self.costs[(x,y)]=c
        return True

    def parse(self):
        #parses the graph and returns all the vertexes

        return list(self.ins.keys())

    def print(self):
        #prints the graph

        for i in self.parse():
            if len(self.ins[i]) == 0 and len(self.outs[i]) == 0:
                print(i, "is an isolated vertex")
            else:
                for j in self.outs[i]:
                    if self.exist_edge(i, j):
                        print(i, "->", j, "cost:", self.costs[(i, j)])

    def get_number(self):
        #returns the number of vertexis in the graph

        return len(self.ins.keys())

    def exist_vertex(self,x):
        # checks if a vertex exists. returns True if it exists and False if not
        # preconditions: x - integer, representing a vertex

        if x in self.parse():
            return True
        return False

    def exist_edge(self,x,y):
        # checks if an edge exists. returns True if it exists and False if not
        # preconditions: x,y - integers, representing 2 vertexis, x being the begining of the edge, and y the final

        if self.exist_vertex(x) and self.exist_vertex(y):
            for i in self.outs[x]:
                if i==y:
                    return True
            return False
        return False

    def get_cost(self,x,y):
        # gets the cost for an edge, if this already exists. if not, it exits the function
        # preconditions: x,y - integers, representing 2 vertexis, x being the begining of the edge, and y the final

        if(self.exist_edge(x,y)):
            return self.costs[(x,y)]
        return False

    def set_cost(self,x,y,cost):
        # sets the cost for an edge, if this already exists. if not, it exits the function
        # preconditions: x,y - integers, representing 2 vertexis, x being the begining of the edge, and y the final

        if (self.exist_edge(x, y)):
            self.costs[(x, y)]=cost
            return True
        return False

    def add_vertex(self,x):
        # adds a vertex to the graph, if this doesn't already exist. if it exists, it exits the function
        # preconditions: x - an integer, a vertex

        if self.exist_vertex(x):
            return False
        self.ins[x]=[]
        self.outs[x]=[]
        return True

    def indegree(self,x):
        # parses the indegree of a vertex, if this already exists exists. if not, it exits the function
        # preconditions: x - an integer, a vertex

        if self.exist_vertex(x)==False:
            return False
        return len(self.ins[x])

    def outdegree(self,x):
        # parses the outdegree of a vertex, if this already exists exists. if not, it exits the function
        # preconditions: x - an integer, a vertex

        if self.exist_vertex(x)==False:
            return False
        return len(self.outs[x])

    def parse_in(self,x):
        # parses the inbound edges of a vertex, and returns the list of the vertexes that go in, if this already exists. if not, it exists the function
        # preconditions: x - an integer, a vertex

        if self.exist_vertex(x)==False:
            return False
        return self.ins[x]

    def parse_out(self,x):
        #parses the outbound edges of a vertex, and returns the list of the vertexes that go out, if this already exists. if not, it exists the function
        #preconditions: x - an integer, a vertex

        if self.exist_vertex(x)==False:
            return False
        return self.outs[x]

    def remove_edge(self,x,y):
        #removes an edge from the graph, if this already exists exists. if not, it exits the function
        #preconditions: x,y - integers, representing 2 vertexis, x being the begining of the edge, and y the final

        if self.exist_edge(x,y)==False:
            return False
        self.ins[y].remove(x)
        self.outs[x].remove(y)
        del self.costs[(x, y)]
        return True

    def remove_vertex(self,x):
        #removes a vertex from the graph, if this already exists exists. if not, it exits the function
        #preconditions: x - an integer, a vertex to be removed

        if self.exist_vertex(x)==False:
            return False
        for i in self.parse_out(x):
            self.remove_edge(x,i)
        for i in self.parse_in(x):
            self.remove_edge(i,x)
        del self.ins[x]
        del self.outs[x]
        return True