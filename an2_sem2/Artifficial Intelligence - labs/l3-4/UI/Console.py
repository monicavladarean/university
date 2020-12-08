from UI.dialog import *
import sys
from Service import Controller

class Console(Ui_MainWindow):
    def __init__(self,window,ctrl):
        self.ctrl=ctrl
        self.setupUi(window)
        self.eaAlgButton.clicked.connect(self.doEa)
        self.hillAlgButton.clicked.connect(self.doHillClimbing)
        self.validateTestButton.clicked.connect(self.validateTest)

    def doEa(self):
        matrixDim=int(self.inputMatrixDim.text())
        mutation=float(self.inputMutation.text())
        crossover=float(self.inputCrossOver.text())
        trials=int(self.inputTrials.text())
        populationSize=int(self.inputPopulation.text())
        res=self.ctrl.doEA(matrixDim,populationSize,trials,mutation,crossover)
        self.solutionShowWidget.clear()
        self.solutionShowWidget.addItem(str(res))

    def doHillClimbing(self):
        number=int(self.inputMatrixDim.text())
        trials = int(self.inputTrials.text())
        res=self.ctrl.doHillAlg(number,trials)
        self.solutionShowWidget.clear()
        self.solutionShowWidget.addItem(str(res))

    def validateTest(self):
        matrixDim = int(self.inputMatrixDim.text())
        mutation = float(self.inputMutation.text())
        crossover = float(self.inputCrossOver.text())
        self.ctrl.validationTest(matrixDim,mutation,crossover)