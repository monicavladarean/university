# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.solutionShowWidget = QtWidgets.QListWidget(self.centralwidget)
        self.solutionShowWidget.setGeometry(QtCore.QRect(405, 71, 361, 481))
        self.solutionShowWidget.setObjectName("solutionShowWidget")



        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(560, 40, 271, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 300, 271, 16))
        self.label_3.setObjectName("label_3")
        self.eaAlgButton = QtWidgets.QPushButton(self.centralwidget)
        self.eaAlgButton.setGeometry(QtCore.QRect(10, 320, 161, 28))
        self.eaAlgButton.setObjectName("eaAlgButton")
        self.hillAlgButton = QtWidgets.QPushButton(self.centralwidget)
        self.hillAlgButton.setGeometry(QtCore.QRect(10, 360, 241, 28))
        self.hillAlgButton.setObjectName("hillAlgButton")

        self.psoAlgButton = QtWidgets.QPushButton(self.centralwidget)
        self.psoAlgButton.setGeometry(QtCore.QRect(10, 390, 241, 28))
        self.psoAlgButton.setObjectName("psoAlgButton")


        self.inputMatrixDim = QtWidgets.QLineEdit(self.centralwidget)
        self.inputMatrixDim.setGeometry(QtCore.QRect(140, 30, 113, 22))
        self.inputMatrixDim.setObjectName("inputMatrixDim")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 131, 16))
        self.label.setObjectName("label")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 121, 16))
        self.label_4.setObjectName("label_4")
        self.inputMutation = QtWidgets.QLineEdit(self.centralwidget)
        self.inputMutation.setGeometry(QtCore.QRect(140, 60, 113, 22))
        self.inputMutation.setObjectName("inputMutation")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 131, 16))
        self.label_5.setObjectName("label_5")
        self.inputCrossOver = QtWidgets.QLineEdit(self.centralwidget)
        self.inputCrossOver.setGeometry(QtCore.QRect(140, 90, 113, 22))
        self.inputCrossOver.setObjectName("inputCrossOver")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 120, 111, 16))
        self.label_6.setObjectName("label_6")
        self.inputPopulation = QtWidgets.QLineEdit(self.centralwidget)
        self.inputPopulation.setGeometry(QtCore.QRect(140, 120, 113, 22))
        self.inputPopulation.setObjectName("inputPopulation")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 150, 111, 16))
        self.label_7.setObjectName("label_7")
        self.inputTrials = QtWidgets.QLineEdit(self.centralwidget)
        self.inputTrials.setGeometry(QtCore.QRect(140, 150, 113, 22))
        self.inputTrials.setObjectName("inputTrials")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 180, 111, 16))
        self.label_9.setObjectName("label_9")
        self.inputSizeOfNeighbourhood = QtWidgets.QLineEdit(self.centralwidget)
        self.inputSizeOfNeighbourhood.setGeometry(QtCore.QRect(140, 180, 113, 22))
        self.inputSizeOfNeighbourhood.setObjectName("inputSizeOfNeighbourhood")

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 210, 111, 16))
        self.label_10.setObjectName("label_10")
        self.inputW = QtWidgets.QLineEdit(self.centralwidget)
        self.inputW.setGeometry(QtCore.QRect(140, 210, 113, 22))
        self.inputW.setObjectName("inputW")

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 240, 111, 16))
        self.label_11.setObjectName("label_11")
        self.inputC1 = QtWidgets.QLineEdit(self.centralwidget)
        self.inputC1.setGeometry(QtCore.QRect(140, 240, 113, 22))
        self.inputC1.setObjectName("inputC1")

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 270, 111, 16))
        self.label_12.setObjectName("label_11")
        self.inputC2 = QtWidgets.QLineEdit(self.centralwidget)
        self.inputC2.setGeometry(QtCore.QRect(140, 270, 113, 22))
        self.inputC2.setObjectName("inputC2")

        self.validateTestButton = QtWidgets.QPushButton(self.centralwidget)
        self.validateTestButton.setGeometry(QtCore.QRect(250, 320, 110, 28))
        self.validateTestButton.setObjectName("validateTestButton")

        self.validateTestPSOButton = QtWidgets.QPushButton(self.centralwidget)
        self.validateTestPSOButton.setGeometry(QtCore.QRect(250, 390, 120, 28))
        self.validateTestPSOButton.setObjectName("validateTestPSOButton")

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "matrix dimensions:"))
        self.label_2.setText(_translate("MainWindow", "Solution"))
        self.label_3.setText(_translate("MainWindow", "Method:"))
        self.eaAlgButton.setText(_translate("MainWindow", "EvolutionaryAlgorithm"))
        self.hillAlgButton.setText(_translate("MainWindow", " HillClimbingAlgorithm"))
        self.label_4.setText(_translate("MainWindow", "mutation probabilty:"))
        self.label_5.setText(_translate("MainWindow", "crossover probability:"))
        self.label_6.setText(_translate("MainWindow", "population size:"))
        self.label_7.setText(_translate("MainWindow", "number of trials:"))
        self.label_9.setText(_translate("MainWindow", "size of neighbourhood:"))
        self.label_10.setText(_translate("MainWindow", "W:"))
        self.label_11.setText(_translate("MainWindow", "C1:"))
        self.label_12.setText(_translate("MainWindow", "C2:"))
        self.validateTestButton.setText(_translate("MainWindow", "Validate Test EA"))
        self.psoAlgButton.setText(_translate("MainWindow", "ParticleSwarmAlgorithm"))
        self.validateTestPSOButton.setText(_translate("MainWindow", "Validate Test PSO"))

