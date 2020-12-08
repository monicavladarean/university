from random import randint, random
from copy import deepcopy

class Particle(object):
    #implements a particle (matrix of permutations)

    def __init__(self,matrixValues,n):

        self.n=n
        self.factor=(n*(n-1))*2
        self._matrixValues = matrixValues
        self.evaluate()
        self.velocity=[] # rate of change of its position with respect to a frame of reference
        for i in range(self.n*2):
            local_vel=[]
            for i in range(self.n):
                local_vel.append(0)
            self.velocity.append(local_vel)

        #memory of the particle
        self._bestPozition = self._matrixValues.copy()
        self._bestFitness = self._fitness

    def fitnessFunction(self,state):
        #the bigger, the better
        state_vals=[]
        for i in range(len(state)):
            local=[]
            for k in range(self.n):
                local.append(int(state[i][k]))
            state_vals.append(local)

        #check if it is in range:
        ok=0
        for i in range(len(state)):
            for k in range(self.n):
                if state[i][k] not in range(1,self.n+1):
                    ok=1
                    break
        if ok==1:
            return 0

        version1=0 #it would be perfect to remain 0 for it to be a sol

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

        #check that all pairs of permutations are different no matter the position
        version3=0
        l=[]
        for i in range(self.n):
            j=self.n+i #get the second part of the pair (i,j) from state
            for k in range(self.n):
                l.append((state_vals[i][k],state_vals[j][k])) #here we add pairs of permutations from the state
        version3+=len(l)-len(set(l))

        return self.factor-version3-version2-version1

    def get_velocity(self):
        return self.velocity

    def set_velocity(self,newVel):
        self.velocity=newVel

    def evaluate(self):
        """ evaluates the particle """
        self._fitness = self.fitnessFunction(self._matrixValues)

    @property
    def matrixValues(self):
        """ getter for values """
        return self._matrixValues

    @property
    def fitness(self):
        """ getter for fitness """
        return self._fitness

    @property
    def bestPozition(self):
        """ getter for best pozition """
        return self._bestPozition

    @property
    def bestFitness(self):
        """getter for best fitness """
        return self._bestFitness

    def set_matrixValues(self, newPozition):
        self._matrixValues = newPozition.copy()
        # automatic evaluation of particle's fitness
        self.evaluate()
        # automatic update of particle's memory
        if (self._fitness > self._bestFitness):
            self._bestPozition = self._matrixValues
            self._bestFitness = self._fitness

    def __str__(self):
        stringRepr = ""
        n=len(self.matrixValues)//2
        for i in range(n):
            j=n+i #it takes the second member of the pair
            s1=""
            for k in range(n):
                s1 += "("+str(self.matrixValues[i][k])+","+str(self.matrixValues[j][k])+")"
            s1 += "\n"
            stringRepr += s1
        return stringRepr

