import math
from numpy import *


class GradientDescentAlgorithm(object):
    def __init__(self,xValues,yValues):
        self.functionCoefficients=[0,0,0,0,0,0] #6 coefficients; f=c1*x^5 + c2*x^4 + c3*x^3 + c4*x^2 + c5*x + c6
        self.xValues=xValues
        self.yValues=yValues
        self.m=6 #nr of coefficients
        self.learningRate=0.0003
        self.error=100   #sum of errors
        self.currentTrial=0

    def computeCurrentError(self):
        #take all points from database and sum of squares of errors for every row from the data
        totalError=0
        for i in range(len(self.yValues)):
            outputForRow=0
            for j in range(self.m):
                if j<=4:
                    outputForRow+=self.functionCoefficients[j]*self.xValues[i][j]
                else:
                    outputForRow+=self.functionCoefficients[j]
            totalError+=(self.yValues[i]-outputForRow)**2

        return totalError/len(self.yValues)

    def getFunctionValForARow(self,i):
        outputForRow = 0
        for j in range(self.m):
            if j <= 4:
                outputForRow += self.functionCoefficients[j] * self.xValues[i][j]
            else:
                outputForRow += self.functionCoefficients[j]
        return outputForRow

    def changingTheCoefficients(self):
        #gradient descent method
        weightsModifiers = [0, 0, 0, 0, 0, 0]  # keeps the value with which we modify the coeffs after every row
        for i in range(len(self.yValues)):
            #for every row
            for j in range(self.m):
                #take the gradients for every row in order to modify after the weights
                if j<=4:
                    prev=weightsModifiers[j]
                    weightsModifiers[j]= prev + (-2)*(1/len(self.yValues))*(self.yValues[i]-self.getFunctionValForARow(i))*self.xValues[i][j]
                else:
                    prev = weightsModifiers[j]
                    weightsModifiers[j] = prev + (-2) * (1 / len(self.yValues)) * (self.yValues[i] - self.getFunctionValForARow(i))
        for i in range(self.m):
            prev_coeff=self.functionCoefficients[i]
            self.functionCoefficients[i]=prev_coeff-(self.learningRate*weightsModifiers[i])

    def main(self):
        while self.currentTrial<10000  and self.error>0.3:
            print("iteration:"+str(self.currentTrial))
            print("error:"+str(self.error))
            print()
            print()
            self.changingTheCoefficients()
            self.error = self.computeCurrentError()
            self.currentTrial+=1

        array=[]
        array.append(self.error)
        array.append(self.functionCoefficients)
        return array