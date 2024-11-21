import logging
logger = logging.getLogger(__name__)

def checksum(command: str) -> str:
    '''Принимает строку команды и возвращает ее вместе с контрольной суммой

    
>>> checksum('$012')
'$012B7'
>>> checksum('!01070600')
'!010706001AF'

'''
    sum=0
    for i in command:
        sum  += int(hex(ord(i)), 16)

    logger.info(f'Добавил чексумму к команде')
    return command + str(hex(sum))[2:].upper()

# запуск теста
# if __name__ == '__main__':
#     import doctest
#     doctest.testmod(verbose=True)
