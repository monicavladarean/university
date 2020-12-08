from copy import deepcopy
from State import *

class Problem():
    def __init__(self):
        self._values = None
        self._initial_state = None
        self._final_state = None

    def set_initial_state(self, init):
        self._initial_state = init

    def get_initial_state(self):
        return self._initial_state

    def expand(self, a_state):
        #returns a list of states
        positions = []
        current = a_state.get_values()
        ones = 0
        for i in range(len(current)):
            for j in range(len(current[i])):
                if current[i][j] == 0:
                    positions.append((i, j))
                else:
                    ones += 1
        if ones >= len(current):
            return []

        result = []
        for coordinates in positions:
            aux = deepcopy(a_state)
            aux.add_to_table(coordinates[0], coordinates[1])
            result.append(aux)

        return result

    def check_if_solution(self, state):
        matrix = state.get_values()
        # check for sum on lines, columns and all types of diagonals
        for l in matrix:
            if sum(l) != 1:
                return False
        for j in range(len(matrix)):
            s = 0
            for i in range(len(matrix)):
                s += matrix[i][j]
            if s != 1:
                return False

        for i in range(len(matrix) - 1):
            for j in range(len(matrix) - 1):
                for k in range(len(matrix)):
                    for l in range(len(matrix)):
                        if abs(i - k) - abs(j - l) == 0 and (i != k or j != l):
                            if matrix[i][j] == 1 and matrix[k][l]:
                                return False

        return True

    def potential(self, state):
        matr = state.get_values()

        for l in matr:
            if sum(l) > 1:
                return False
        for j in range(len(matr)):
            s = 0
            for i in range(len(matr)):
                s += matr[i][j]
            if s > 1:
                return False

        return True

    def heuristic(self, another_state):
        result = 0
        if self.potential(another_state) == False:
            return 100
        m = another_state.get_values()
        for i in m:
            for j in i:
                if j == 0:
                    result += 1

        return result

    def readFromFile(self):
        f = open("pb.txt")
        n = int(f.readline())
        f.close()
        return n
