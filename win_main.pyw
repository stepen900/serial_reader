import sys
from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtCore  import *
from PyQt5.QtGui  import *
from untitled import *


from checksum import checksum
import logging
from serial.tools import list_ports
import serial
import time
import _thread


logger = logging.getLogger(__name__)
FORMAT = '%(levelname)s %(asctime)s %(name)s %(message)s'
logging.basicConfig(level=logging.INFO, filemode='a',\
                     filename= 'logs/logs_port.log',\
                     encoding= 'utf-8', format= FORMAT)




class MyWin(QtWidgets.QMainWindow):


    def __init__(self, parent = None):
        self.classport = Port()
        self.classport.serial_ports()
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('COM Connector')
        self.add_item()
        self.ui.pushButton.clicked.connect(self.get_combobox)
    
    @pyqtSlot()
    def update_text_browzer(self):
        
        #self.ui.consoleBrowser.clear()
        self.ui.consoleBrowser.setText(f'Data is --- {self.classport.read_in_serial()}')#.decode()}')
        QtCore.QTimer.singleShot(100, self.update_text_browzer)

        
    def add_item(self):
        self.ui.portBox.clear()
        for i in self.classport.ports:
                self.ui.portBox.addItem(i)
    
    
    def get_combobox(self):


        global port, speed, time_out, port_thread
        
        port = self.ui.portBox.currentText()
        speed = self.ui.speedBox_2.currentText()
        time_out =  self.ui.comboBox_3.currentText()
        self.ui.consoleBrowser.clear()

        try:
            connect = self.classport.ser.close()
            time.sleep(0.2)
            connect = self.classport.open_port(port, int(speed), float(time_out))
        except Exception:
            time.sleep(0.2)
            connect = self.classport.open_port(port, int(speed), float(time_out))
        try:
            QtCore.QTimer.stop()
        except Exception:
            pass
        self.ui.consoleBrowser.setText(f'Connection is {connect}')
        # time.sleep(3)
        if connect:
            # QtCore.QTimer.singleShot(0, self.update_text_browzer)
            self.update_text_browzer()
            
        
    # def thread_for_browzer(self):
    #     if self.classport.ser.is_open:
    #         _thread.start_new_thread(self.update_text_browzer, ())


    
    

class Port():

    def __init__(self):
        self.ser = None

    def serial_ports(self):


        '''Возвращает список COM'''

        f = list_ports.comports()
        current_ports = []
        for i in f:
            g = str(i).split(' ')[0]
            current_ports.append(g)
        self.ports = current_ports


    def open_port(self, port:str, baud:int, time_out:float):


        ''' Получает данные из файла конфига 
        и открывает порт, возвращая объект соединения'''

        try:
            ser = serial.Serial(port= port, baudrate= baud, timeout= time_out)
            logger.info(f'Установил подключение к {com= } \
                        на скорости {baud= } c  {time_out= }')
            
        except Exception:
            logger.critical(f'Не могу подключиться к {port= } на \
                            скорости {baud= } c  {time_out= }, пытаюсь снова ...')
        self.ser = ser
        return ser

    def write_in_serial(self, command:bytes)-> None:


        '''Записывает данные в COM'''


        self.ser.write(command)
        logger.info(f'Данные {command=} записаны в порт')


    def read_in_serial(self)-> bytes:


        '''Читает данные из COM'''

        logger.info('получаем данные из COM')
        return self.ser.readline()

   


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())