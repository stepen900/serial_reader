import sys
from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtCore  import *
from PyQt5.QtGui  import *
from untitled import *

from open_port import open_port
from port_read import read_in_serial
from port_write import write_in_serial
from checksum import checksum
import logging
from  port_read import *
from  open_port import *
from  port_write import *
import threading

logger = logging.getLogger(__name__)
FORMAT = '%(levelname)s %(asctime)s %(name)s %(message)s'
logging.basicConfig(level=logging.INFO, filemode='a',\
                     filename= 'logs/logs_port.log',\
                     encoding= 'utf-8', format= FORMAT)




class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('COM Connector')
        self.serial_ports()
        self.ui.pushButton.clicked.connect(self.get_combobox)

    
    def get_combobox(self):


        global port, speed, time_out, port_thread
        port = self.ui.portBox.currentText()
        speed = self.ui.speedBox_2.currentText()
        time_out =  self.ui.comboBox_3.currentText()
        self.ui.consoleBrowser.clear()
        self.ui.consoleBrowser.setText(f'{port=} {speed= } {time_out=}')

        ser = open_port(port, int(speed), float(time_out))

    def serial_ports(self):
        from serial.tools import list_ports
        f = list_ports.comports()

        for i in f:
            g = str(i).split(' ')[0]
            self.ui.portBox.addItem(g)
    
        





def window_com():
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())



if __name__ == '__main__':

    window_com()
    




    # ser = open_port()
    # command = checksum('!AA')
    # write_in_serial(ser, 0x23)
    # read_in_serial(ser)