from pynput.keyboard import Listener
import logging

logfile_path = 'E:/listen.txt'

logging.basicConfig(filename=logfile_path, \
                    level=logging.DEBUG, \
                    format='%(asctime)s:\t%(msg)s')


def press(key):
    
    print(key)

    #print(type(key))
    # logging.info(key)


with Listener(on_press=press) as lis:
    lis.join()

