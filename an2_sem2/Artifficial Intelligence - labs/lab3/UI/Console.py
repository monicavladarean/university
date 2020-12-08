
from Service.Controller import Controller
from UI.dialog import Ui_MainWindow


class Console(Ui_MainWindow):
    def __init__(self,window,ctrl):
        self.ctrl=ctrl
        self.setupUi(window)
        self.eaAlgButton.clicked.connect(self.doEa)
        self.hillAlgButton.clicked.connect(self.doHillClimbing)
        self.psoAlgButton.clicked.connect(self.doPSO)
        self.validateTestButton.clicked.connect(self.validateTest)
        self.validateTestPSOButton.clicked.connect(self.validateTestPSO)

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

    def doPSO(self):
        n=int(self.inputMatrixDim.text())
        nrOfTrials=int(self.inputTrials.text())
        c1=float(self.inputC1.text())
        c2=float(self.inputC2.text())
        w=float(self.inputW.text())
        sizeOfNeighbourhood=int(self.inputSizeOfNeighbourhood.text())
        noParticles=int(self.inputPopulation.text())
        res=self.ctrl.doPSO(n, noParticles, sizeOfNeighbourhood , w, c1, c2, nrOfTrials)
        self.solutionShowWidget.clear()
        self.solutionShowWidget.addItem(str(res))

    def validateTest(self):
        matrixDim = int(self.inputMatrixDim.text())
        mutation = float(self.inputMutation.text())
        crossover = float(self.inputCrossOver.text())
        self.ctrl.validationTest(matrixDim,mutation,crossover)

    def validateTestPSO(self):
        n = int(self.inputMatrixDim.text())
        sizeOfNeighbourhood = int(self.inputSizeOfNeighbourhood.text())
        c1 = float(self.inputC1.text())
        c2 = float(self.inputC2.text())
        w = float(self.inputW.text())
        self.ctrl.validationTestPSO(n, sizeOfNeighbourhood, w, c1, c2)