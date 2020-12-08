from Service.EvolutionaryAlgorithm import EvolutionaryAlgorithm
from Service.HillClimbingAlgorithm import HillClimbingAlgorithm
import matplotlib.pyplot as plt

class Controller(object):
    def __init__(self):
        pass

    def doEA(self, n,population,trials,mutation,crossover):
        ea=EvolutionaryAlgorithm(n,population,trials,mutation,crossover)
        return ea.mainForEvolutionaryAlg()

    def doHillAlg(self,n,nrOfTrials):
        hill=HillClimbingAlgorithm(n,nrOfTrials)
        return hill.greedyHillClimbing()

    def validationTest(self,n,mutation,crossover):
        std=[]
        mean=[] #avg
        #we apply 30 runs:
        for i in range(4):
            #keep the fitness of every state in every pop in a run
            ea = EvolutionaryAlgorithm(n, 40, 1000, mutation, crossover)
            std1,mean1=ea.validateTest()
            std.append(std1)
            mean.append(mean1)
            print(i)

        plt.plot(std)
        stdd=plt.plot(std,label="Standard Deviation")
        avg=plt.plot(mean,label="Average")
        plt.legend(handles=[stdd,avg])
        plt.show()
