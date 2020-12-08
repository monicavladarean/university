from Problem import *

class Controller():
    def __init__(self, problem):
        self._problem = problem
        n = self._problem.readFromFile()
        init = []
        for i in range(n):
            aux = []
            for j in range(n):
                aux.append(0)
            init.append(aux)
        init = State(init)
        self._problem.set_initial_state(init)

    def get_initial(self):
        return self._problem.get_initial_state()

    def dfs(self, root):
        stack = [root]
        visited = []
        while len(stack) > 0:
            node = stack.pop()
            #print(node)
            if self._problem.check_if_solution(node):
                return node
            visited.append(node)
            if self._problem.potential(node):
                sts = self._problem.expand(node)
                aux = []
                for x in sts:
                    if x not in visited:
                        aux.append(x)
                stack = stack + aux

    def gbfs(self, root):
        visited = []
        to_visit = [root]
        while len(to_visit) > 0:
            node = to_visit.pop(0)
            #print(node)
            visited = visited + [node]
            if self._problem.check_if_solution(node):
                return node
            if self._problem.potential(node):
                aux = []
                sts = self._problem.expand(node)

                for x in sts:
                    if x not in visited:
                        aux.append(x)
                aux = [[x, self._problem.heuristic(x)] for x in aux]
                aux.sort(key=lambda x: x[1])
                aux = [x[0] for x in aux]
                to_visit = aux[:] + to_visit

