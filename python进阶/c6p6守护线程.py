"""
将一个子线程设置为守护线程
那么守护线程会在主线程结束后自动退出
主线程退出，进程等待所有子线程执行完毕后才结束
线程守护是子线程守护主线程
如果子线程有没有设置线程守护的
那么所有的子线程的守护失效(在主线程结束后依然会执行)


设置方法
在创建线程对象后 使用线程对象调用
.setDaemon(True)方法
默认为False 也就是主线程结束时的子线程依然在运行




"""

import time
import threading


def work1():
    for i in range(10):
        print('正在执行work1......')
        time.sleep(0.5)


def work2():
    for i in range(10):
        print('work2......')
        time.sleep(0.5)


if __name__=='__main__':

    WorkA = threading.Thread(target=work1)
    WorkA.setDaemon(True)

    WorkB = threading.Thread(target=work2)
    WorkB.setDaemon(True)

    # 设置守护线程

    WorkA.start()
    WorkB.start()
    time.sleep(2)
    print('\033[7;31m主线程死了...\033[0m')
    exit()
    # 让程序退出




