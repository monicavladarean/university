from controller import Population
from fileOperations import *

epsilon = 0.6

if __name__ == '__main__':
    (trainingData,output) = readTrainingData()
    population=Population(trainingData,output)
    i=1
    while True:
        error = population.train()
        print(error)
        i+=1
        if error<epsilon:
            break
    testData = readTestData()
    allOutput=[]
    for i in range(len(testData)):
        output = population.predict(testData[i])
        print(output)
        allOutput.append(output)