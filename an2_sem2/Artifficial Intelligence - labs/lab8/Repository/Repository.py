class Repository(object):
    def __init__(self):
        self.xValues=[]
        self.yValues=[]
        self.readFromFile()

    def readFromFile(self):
        file1 = open('C:\\Users\\Monica\\OneDrive\\Desktop\\AI\\lab7\\database.txt', 'r')
        Lines = file1.readlines()
        count=0
        for line in Lines:
            if count%2==0:
                rowInts = line.strip().split(" ")
                array = []
                self.yValues.append([float(rowInts[5])])
                for i in range(0, 5):
                    array.append(float(rowInts[i]))
                self.xValues.append(array)
            count+=1

    def getXValues(self):
        return self.xValues

    def getYValues(self):
        return self.yValues
