import numpy as np
from Domain.State import State
from Domain.Ant import ant
from math import *

class Controller(object):
    def __init__(self , n,populationSize,trials,numberOfAnts,alpha, beta, q0, rho):
        self.population = [] #list of states (space for the ants to move)
        self.n = n  #dimensions for the matrix
        self.mutationFactor = (n*(n-1))*2  #number big enough for the fitness func to not return neg nrs
        self.current_generation = 0
        self.trials=trials
        self.nrOfStates=int(sqrt(populationSize))
        self.numberOfAnts=numberOfAnts
        self.alpha=alpha
        self.beta=beta
        self.q0=q0
        self.rho=rho
        self.traceForAnts = [[1 for i in range(self.nrOfStates*self.nrOfStates)] for j in range(self.nrOfStates*self.nrOfStates)]
        #print(self.traceForAnts)
        for i in range(self.nrOfStates):
            line=[]
            for j in range(self.nrOfStates):
                line.append(self.getInitialIndivid()) # a list of state objects
            self.population.append(line)



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

    def iterationForACO(self):
        ants = [ant(self.nrOfStates, self.n, self.population) for i in range(self.numberOfAnts)] #ant set

        for i in range(self.nrOfStates * self.nrOfStates):
            # max nr of iterations in an epoch is len(solution)
            for x in ants:
                x.addMove(self.q0, self.traceForAnts, self.alpha, self.beta)
        # actualize the trace with pheromones let from all ants
        trace = [1.0 / ants[i].fitness() for i in range(len(ants))]
        for i in range(self.nrOfStates * self.nrOfStates):
            for j in range(self.nrOfStates * self.nrOfStates):
                self.traceForAnts[i][j] = (1 - self.rho) * self.traceForAnts[i][j]
        for i in range(len(ants)):
            for j in range(len(ants[i].path) - 1):
                x = ants[i].path[j]
                y = ants[i].path[j + 1]
                self.traceForAnts[x][y] = self.traceForAnts[x][y] + trace[i]
        # return best ant that attempts to reach the solution

        f = [[ants[i].fitness(), i] for i in range(len(ants))]
        f = max(f)
        # return best ant path
        return ants[f[1]].path

    def mainForACO(self):
        bestSol = []

        for i in range(self.trials):
            #print(self.traceForAnts)
            sol = self.iterationForACO().copy()
            if len(sol) > len(bestSol):
                bestSol = sol.copy()

        maximumFitness=0

        for solution in bestSol:
            fit=self.population[solution//self.nrOfStates][solution%self.nrOfStates].fitnessFunction()
            if fit>maximumFitness:
                maximumFitness=fit
                eulerSquare=self.population[solution//self.nrOfStates][solution%self.nrOfStates]

        print(str(eulerSquare))

    def validateTest(self):
        # 1000 trials, for each population we do fitness and then at the end findout the mean and std deviation
        res = []
        while self.current_generation != self.trials:  # we have 1000 trials => 1000 generations
            sol = self.iterationForACO().copy()
            # compute mean and deviation
            for state in sol:
                res.append(self.population[state // self.nrOfStates][state % self.nrOfStates].fitnessFunction())
            self.current_generation += 1
        return (np.std(res), np.mean(res))










