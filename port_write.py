import logging
logger = logging.getLogger(__name__)
# FORMAT = '%(levelname)s %(asctime)s %(name)s %(message)s'
# logging.basicConfig(level=logging.INFO, filemode='a',\
#                      filename= 'logs/logs_port_write.log',\
#                      encoding= 'utf-8', format= FORMAT)

def write_in_serial(connection: object, command:bytes)-> None:
    connection.write(command)
    logger.info(f'Данные {command=} записаны в порт')