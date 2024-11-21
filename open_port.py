import serial
import time
import logging

logger = logging.getLogger(__name__)
# FORMAT = '%(levelname)s %(asctime)s %(name)s %(message)s'
# logging.basicConfig(level=logging.INFO, filemode='a',\
#                      filename= 'logs/logs_port.log',\
#                      encoding= 'utf-8', format= FORMAT)


def open_port(com: str, baud:int, time_out:float):
    '''
    Получает данные из файла конфига и открывает порт, возвращая объект соединения

    '''
    print('Открываю порт')
    # with open('config\conf.ini', 'r') as config:
    #     com = config.readline().strip()
    #     baud = config.readline().strip()
    #     logger.info(f'Получил данные конфига {com= } и {baud= }')

    try:
        # ser = serial.Serial(port= com, baudrate= baud)
        ser = serial.Serial(port= com, baudrate= baud, timeout= time_out)
    except Exception:
        logger.critical(f'Не могу подключиться к {com= } на скорости {baud= } c  {time_out= }, пытаюсь снова ...')
        time.sleep(2)
        open_port(com, baud, time_out)

    if not ser.is_open:
        # ser = serial.Serial(port= com, baudrate= baud)
        ser = serial.Serial(port= com, baudrate= baud, timeout= time_out)
        time.sleep(2)
        logger.critical(f'Не могу подключиться к {com= } на скорости {baud= } c  {time_out= }, пытаюсь снова ...')
    logger.info(f'Установил подключение к {com= } на скорости {baud= } c  {time_out= }')
    return ser


# if __name__ == '__main__':
    
#     open_port()
