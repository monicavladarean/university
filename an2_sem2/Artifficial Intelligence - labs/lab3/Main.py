from PyQt5.uic.properties import QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from UI.Console import *

def window():

    app = QApplication(sys.argv)
    MainWindow = QWidget()
    ctrl = Controller()
    ui = Console(MainWindow, ctrl)

    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
   window()