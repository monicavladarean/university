class State(object):
    #the configuration for a matrix

    def __init__(self, matrixValues):
        self.values = matrixValues

    def get_vals(self):
        return self.values

    def set_vals(self,v):
        self.values=v

    def __str__(self):
        stringRepr = ""
        n= len(self.values) // 2
        for i in range(n):
            j=n+i
            s1=""
            for k in range(n):
                s1 += "(" + str(self.values[i][k]) + "," + str(self.values[j][k]) + ")"
            s1 += "\n"
            stringRepr += s1
        return stringRepr

    def __eq__(self, otherMatrix):
        if otherMatrix==None:
            return False

        otherMatrixVals = otherMatrix.get_vals()

        for i in range(len(self.values)):
                if self.values[i] != otherMatrixVals[i]:
                    return False
        return True