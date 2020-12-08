import numpy as np
from Domain.State import State
import matplotlib.pyplot as pltt

class EvolutionaryAlgorithm(object):
    def __init__(self , n,populationSize,trials,mutation,crossover):

        self.population = []
        self.n = n
        self.mutation = mutation
        # a number big enough for the fitness func to not return neg nrs
        self.mutationFactor = (n*(n-1))*2
        self.current_generation = 0
        self.trials=trials
        self.nrOfStates=populationSize
        self.crossoverProbability=crossover
        self.standardDeviation=0
        self.mean=0
        for i in range(self.nrOfStates):
            self.population.append(self.getInitialIndivid()) # a list of state objects
        self.population.sort(key=self.keyGeneratorForSorting,reverse=True)


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
        individ=State(state)
        return individ

    def fitnessFunction(self,state):
        #the bigger, the better (checks the permutations in the state and gives a result based on how close to the sol is this state)
        state_vals=state.get_vals()
        version1=0 #if it remains 0 => it is a sol

        #check the lines
        for i in range(self.n):
            l=[]
            for j in range(self.n):
                l.append(state_vals[i][j]) #put the permutations from lines in l
            #get how many perms are the same: if 0 => all unique => very close to sol
            version1+=len(l)-len(set(l))

        #check the columns
        version2=0
        for i in range(self.n):
            l=[]
            for j in range(self.n,self.n*2):
                l.append(state_vals[j][i]) #perms from columns in l
            version2+=len(l)-len(set(l))

        #check that all pairs of permutations are different, no matter the position
        version3=0
        l=[]
        for i in range(self.n):
            j=self.n+i #get the second part of the pair (i,j) from state
            for k in range(self.n):
                l.append((state_vals[i][k],state_vals[j][k])) #add pairs of permutations from the state
        version3+=len(l)-len(set(l))

        return self.mutationFactor-version3-version2-version1


    def keyGeneratorForSorting(self,state):
        #returns the fitness of a state
        return self.fitnessFunction(state)

    def mutate(self,state):
        #gives a state a random mutation (change 2 permutations for a random first pos from a pair and a random second pos from a pair)

        poz1=np.random.randint(0,self.n)
        poz2=np.random.randint(self.n,self.n*2)
        permutation1=np.random.permutation(self.n)
        permutation2=np.random.permutation(self.n)
        for i in range(self.n):
            #change them as in the example
            permutation1[i]+=1
            permutation2[i]+=1
        state_vals=state.get_vals()
        state_vals[poz1]=permutation1
        state_vals[poz2]=permutation2
        state.set_vals(state_vals)

        return state

    def crossPermutations(self,perm1,perm2):
        #take 2 indexes from the first perm (including middle),put it in the res
            #then take for the remaining positions from the second perm numbers, from the end

        n=len(perm1) #len of the perm
        i1=np.random.randint(0,n//2)  #random pos from the first perm
        i2=i1+n//2 #second pos from the perm
        child=[0]*self.n #preparing child
        for i in range(i1,i2):
            child[i]=perm1[i] #put the vals first from the perm1
        index=i2
        #now put vals from perm2 from the 0,i1 and i2,n ranges
        for i in range(i2,n):
            if child[i]==0:
                while perm2[index%n] in  child:  #while we have that in child, we look for an unused elem
                    index+=1
                child[i]=perm2[index%n]
        for i in range(i1):
            if child[i]==0:
                while perm2[index%n] in  child:  #while we have that in child, we look for an unused elem
                    index+=1
                child[i]=perm2[index%n]

        return child


    def crossOver2Parents(self,parent1,parent2):
        #cross all permutations => a child
        valsFromFirstParent=parent1.get_vals()
        valsFromSecondParent = parent2.get_vals()
        child_vals=[]
        ran=np.random.random()
        if self.crossoverProbability>ran:
            for i in range(len(valsFromFirstParent)):
                child_vals.append(self.crossPermutations(valsFromFirstParent[i],valsFromSecondParent[i]))
        child=State(child_vals)
        return child

    def createNewPopulation(self):
        #change the self.population

        length=len(self.population)
        #cut the old and bad states, and keep the first ones (the best)
        if length>self.nrOfStates:
            length=self.nrOfStates
        else:
            length=length//2
        population=self.population[0:length]
        nextPopulation=[]
        #create the new population:
        for i in range(length):
            for j in range(length):
                #crossover all the people and give the children to the next generation
                if i!=j:
                    kid=self.crossOver2Parents(population[i],population[j])
                    if kid.get_vals()!=[]:
                        #randomly mutate it or not
                        if(np.random.random()<self.mutation):
                            kid=self.mutate(kid)
                        nextPopulation.append(kid)
        #sort by the fitness (best => in front)
        nextPopulation.sort(key=self.keyGeneratorForSorting,reverse=True)
        return nextPopulation

    def mainForEvolutionaryAlg(self):
        #here we have a number of trials in which we try to find a solution by forming new and new generations
        while self.current_generation!=self.trials: #we have 1000 trials => 1000 generations
            if self.fitnessFunction(self.population[0])==self.mutationFactor: #we found our sol if the best state is ok in the fitness func
                print("solution:\n"+str(self.population[0]))
                return self.population[0]
            self.population=self.createNewPopulation()
            #compute mean and deviation
            res=[]
            for state in self.population:
                res.append(self.fitnessFunction(state))
            self.current_generation+=1
        print("no sol,but the closest is:\n")

    def validateTest(self):
        # 1000 trials, for each population we do fitness and then at the end findout the mean and std deviation
        res = []
        while self.current_generation != self.trials:  #1000 trials => 1000 generations

            self.population = self.createNewPopulation()
            # compute mean and deviation
            for state in self.population:
                res.append(self.fitnessFunction(state))
            self.current_generation += 1
            if self.fitnessFunction(self.population[0]) == self.mutationFactor:
                break

        return (np.std(res), np.mean(res))





