from open_port import open_port
from port_read import read_in_serial
from port_write import write_in_serial
from checksum import checksum
import logging

logger = logging.getLogger(__name__)
FORMAT = '%(levelname)s %(asctime)s %(name)s %(message)s'
logging.basicConfig(level=logging.INFO, filemode='a',\
                     filename= 'logs/logs_port.log',\
                     encoding= 'utf-8', format= FORMAT)

ser = open_port()
command = checksum('!AA')
write_in_serial(ser, 0x23)
read_in_serial(ser)

