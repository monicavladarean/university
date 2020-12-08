class Ui(object):
    def __init__(self,ctrl):
        self.ctrl=ctrl

    def runApp(self):
        print("Solve a simple regression problem - using an ANN with a hidden layer and linear activation function.")
        self.neuralNetwork()

    def neuralNetwork(self):
        nrOfTrials=int(input("Nr of trials:"))
        learningRate=0.0000001
        array=self.ctrl.doTheIterationsFunction(nrOfTrials,learningRate)
        best_error=array[1]
        guessedOutputs=array[0]
        print("Outputs found by the neural network:  " + str(guessedOutputs) )
        print("Best error:"+str(best_error))