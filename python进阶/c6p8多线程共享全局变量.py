"""
全局变量可以在线程中共享全局变量的

"""

import threading
from time import sleep

num = 0


def work1():
    global num
    for i in range(10):
        num += 1
    print('In work1 ',num)


def work2():
    for i in range(10):
        print('In work2 ',num)


if __name__ == '__main__':

    t1 = threading.Thread(target=work1)
    t2 = threading.Thread(target=work2)

    # t1.setDaemon(True)
    # t2.setDaemon(True)

    t1.start()
    t2.start()

    while True:
        if len(threading.enumerate()) == 1:
            break

    print('main--------->', num)

