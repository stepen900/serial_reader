import serial
import time
import logging

logger = logging.getLogger(__name__)
# FORMAT = '%(levelname)s %(asctime)s %(name)s %(message)s'
# logging.basicConfig(level=logging.INFO, filemode='a',\
#                      filename= 'logs/logs_port.log',\
#                      encoding= 'utf-8', format= FORMAT)


def open_port():
    '''
    Получает данные из файла конфига и открывает порт, возвращая объект соединения

    '''
    

    with open('config\conf.ini', 'r') as config:
        com = config.readline().strip()
        baud = config.readline().strip()
        logger.info(f'Получил данные конфига {com= } и {baud= }')

    try:
        ser = serial.Serial(port= com, baudrate= baud)
    except Exception:
        logger.critical(f'Не могу подключиться к {com= } и {baud= }, пытаюсь снова ...')
        time.sleep(2)
        open_port()

    if not ser.is_open:
        ser = serial.Serial(port= com, baudrate= baud)
        time.sleep(2)
        logger.critical(f'Не могу подключиться к {com= } и {baud= }, пытаюсь снова ...')
    logger.info(f'Установил подключение к {com= } и {baud= }')
    return ser


# if __name__ == '__main__':
    
#     open_port()
