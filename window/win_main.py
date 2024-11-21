import sys
from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtCore  import *
from PyQt5.QtGui  import *
from untitled import *



class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('COM Connector')
        self.ui

    # def mbox(self, body, title = 'Erroe'):
    #     dialog = QMessage


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())