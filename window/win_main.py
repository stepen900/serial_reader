import sys
from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtCore  import *
from PyQt5.QtGui  import *
from untitled import *
import serial



class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('COM Connector')
        self.serial_ports()
        self.ui.pushButton.clicked.connect(self.get_combobox)

    
    def get_combobox(self):

        port = self.ui.portBox.currentText()
        speed = self.ui.speedBox_2.currentText()
        time_out =  self.ui.comboBox_3.currentText()
        self.ui.consoleBrowser.clear()
        self.ui.consoleBrowser.setText(f'{port=} {speed= } {time_out=}')
        print(port, speed, time_out)

    def serial_ports(self):
        from serial.tools import list_ports
        f = list_ports.comports()

        for i in f:
            g = str(i).split(' ')[0]
            self.ui.portBox.addItem(g)
    
        




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())