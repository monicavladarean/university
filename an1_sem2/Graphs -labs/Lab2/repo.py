class Graph():
    def __init__(self, file_name):
        self.ins={}

        f = open(file_name, "r")
        lines = f.read().split("\n")
        self.vertices=int(lines[0].split()[0])
        for i in range(self.vertices):
            self.ins[i] = []
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
            self.ins[y].append(x)
            self.ins[x].append(y)
            lines = f.readline().strip()

    def add_edge(self,x,y):
        # adds an edge to the graph, if this doesn't already exist. if it exists, it exits the function
        # preconditions: x,y - an integers, 2 vertexes and c - integer, the cost

        if self.exist_edge(x,y):
            return False
        if self.exist_vertex(x)==False or self.exist_vertex(y)==False:
            return False
        self.ins[y].append(x)
        return True

    def parse(self):
        #parses the graph and returns all the vertexes

        return list(self.ins.keys())

    def print(self):
        #prints the graph

        for i in self.parse():
            if len(self.ins[i]) == 0:
                print(i, "is an isolated vertex")
            else:
                for j in self.ins[i]:
                    if self.exist_edge(i, j):
                        print(i, "-", j)

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
            for i in self.ins[x]:
                if i==y:
                    return True
            return False
        return False


    def parse_in(self,x):
        # parses the inbound edges of a vertex, and returns the list of the vertexes that go in, if this already exists. if not, it exists the function
        # preconditions: x - an integer, a vertex

        if self.exist_vertex(x)==False:
            return False
        return self.ins[x]

    def BFS(self, temp,s):
        q = [s]
        while q:
            v = q.pop(0)
            if not v in temp:
                temp = temp + [v]
                q = q + self.ins[v]
        temp.sort()
        return temp

    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(self.get_number()):
            visited.append(False)
        for v in range(self.get_number()):
            if visited[v] == False:
                temp = []
                aux=self.BFS(temp, v)
                if aux not in cc:
                    cc.append(aux)
        return cc
