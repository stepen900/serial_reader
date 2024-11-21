import logging
logger = logging.getLogger(__name__)
# FORMAT = '%(levelname)s %(asctime)s %(name)s %(message)s'
# logging.basicConfig(level=logging.INFO, filemode='a',\
#                      filename= 'logs/logs_port_read.log',\
#                      encoding= 'utf-8', format= FORMAT)

def read_in_serial(connection: object)-> bytes:
    logger.info('получаем данные из COM')
    return connection.readline()
