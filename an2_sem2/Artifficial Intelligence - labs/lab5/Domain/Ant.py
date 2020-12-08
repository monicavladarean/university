from random import *
import numpy as np
from Domain.State import State

class ant(object):
    def __init__(self, n,dimIndivid,population):
        # constructor pentru clasa ant
        self.n = n
        self.dimIndividual = dimIndivid
        self.size = n * n
        self.path = [randint(0, self.size - 1)]
        self.pop=population
        """
        drumul construit de furnica initializat aleator pe prima pozitie
        drumul este o permutare de self.size elemente, fiecare numar reprezentand o casuta a tablei de sah:
        pt n=4, m=6
        0  este casuta 0, 0
        1  este casuta 0, 1
        ...
        5  este casuta 0, 5
        6  este casuta 1, 0
        ...
        23 este casuta 3, 5 (ultima din cele 24 de casute)
        """

    def getInitialIndivid(self):
        #gets an individ aka a matrix (everytime a different one)
        state = []
        for i in range(2*self.n): #we will have 2*n permutations
            permutation = np.random.permutation(self.n)
            for j in range(len(permutation)):
                #we just add 1 to be like in the example
                permutation[j]+=1
            permutation=tuple(permutation)
            state.append(permutation)
        individ=State(state,self.n)
        return individ

    def transformMatrixToPairs(self,matrix):
        matrixVals=matrix.get_vals()
        n = len(matrixVals) // 2
        newOne=[]
        for i in range(n):
            l=[]
            j = n + i  # it takes the second member of the pair
            for k in range(n):
                l.append([matrixVals[i][k],matrixVals[j][k]])
            newOne.append(l)
        return newOne

    def transformMatrixToPermutations(self,matrixVals):
        newOne=[]
        for i in range(self.n):
            perm1=[]
            for j in range(self.n):
                perm1.append(matrixVals[i][j][0])
            newOne.append(tuple(perm1))
        for i in range(self.n):
            perm1=[]
            for j in range(self.n):
                perm1.append(matrixVals[i][j][1])
            newOne.append(tuple(perm1))
        return newOne



    def nextMoves(self, a):
        # => a list of possible correct paths from position a
        new = []
        for i in range(self.size):
            if (i not in self.path):
                new.append(i)
        return new.copy()

    def distMove(self, a):
        #add step a in the path
        ## return an empirical distence made from the nr of possibile correct moves

        x = ant(self.n,self.dimIndividual,self.pop)
        x.path = self.path.copy()
        x.path.append(a)
        return (self.size - len(x.nextMoves(a)))

    def addMove(self, q0, trace, alpha, beta):
        #add a new pos in ant's sol, if it's possible
        p = [0 for i in range(self.size)]
        # for pos that are not valid we put 0
        nextSteps = self.nextMoves(self.path[len(self.path) - 1]).copy()
        #det next valid positions, in nextStep (if we don't have any, we exit)
        if (len(nextSteps) == 0):
            return False
        #on the valid pos, put the val of the empirical distance
        for i in nextSteps:
            p[i] = self.distMove(i)
        #applicate the formula
        p = [(p[i] ** beta) * (trace[self.path[-1]][i] ** alpha) for i in range(len(p))]

        # add the best possible move to the path
        p = [[i, p[i]] for i in range(len(p))]
        p = max(p, key=lambda a: a[1])
        self.path.append(p[0])


    def fitness(self):
        # un drum e cu atat mai bun cu cat este mai lung
        # problema de minimizare, drumul maxim e n * m
        # are max fitness din path
        #print(self.path)
        #fitness of an ant is basically maxFitness from the best matrix she passed through

        maxOfFit=self.pop[self.path[0]//self.n][int(self.path[0]%self.n)].fitnessFunction()
        for pat in self.path:
            fit=self.pop[pat//self.n][int(pat%self.n)].fitnessFunction()
            if fit>maxOfFit:
                maxOfFit=fit
        return maxOfFit

