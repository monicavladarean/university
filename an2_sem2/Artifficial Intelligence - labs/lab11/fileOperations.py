import csv

def readTrainingData():
    trainingData = []
    output = []
    with open('sensor_readings_24.data') as csv_file:
        for row in csv.reader(csv_file, delimiter=','):
            trainingData.append([float(row[i]) for i in range(24)])
            output.append(row[24])
    return trainingData, output

def readTestData():
    testingData = []
    output = []
    with open('test.in') as csv_file:
        for row in csv.reader(csv_file, delimiter=','):
            testingData.append([float(row[i]) for i in range(24)])
            output.append(row[24])
    return testingData