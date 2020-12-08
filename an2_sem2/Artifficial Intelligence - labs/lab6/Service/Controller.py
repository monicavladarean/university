from Service.PracticeService import DecisionTreeClass
from numpy import random

class Controller(object):
    def __init__(self,practicePercentage):
        self.practiceNrRows=int(practicePercentage/100*625)
        self.testingNrRows=625-self.practiceNrRows
        self.listOfDataForPracticing=[]
        self.listOfDataForTesting=[]
        self.readFromFile()

    def readFromFile(self):
        file1 = open('C:\\Users\\Monica\\OneDrive\\Desktop\\AI\\lab6\\balance-scale.data', 'r')
        Lines = file1.readlines()
        bigArray=[]
        count = 0
        for l in Lines:
            rowInts=l.strip().split(",")
            array=[]
            array.append(str(rowInts[0]))
            for i in range(1,5):
                array.append(int(rowInts[i]))
            bigArray.append(array)
            count+=1
        random.shuffle(bigArray)
        for i in range(self.practiceNrRows):
            self.listOfDataForPracticing.append(bigArray[i])
        for i in range(self.practiceNrRows,625):
            self.listOfDataForTesting.append(bigArray[i])

    def decisionTreeFunction(self):
        decisionTree=DecisionTreeClass(self.listOfDataForPracticing,self.listOfDataForTesting)
        decisionTree.mainForMakingDecisionTree()
        print(decisionTree.mainForTestingTheDaata())


