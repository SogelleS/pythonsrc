'''
=====+=====
     +
     +
     +
 +++++++++
 +   +   +
 +   +   +
 +   +   +
     +  子线程
     +
   主线程

子线程之间共享进程的资源
子线程的执行顺序是无序的
主线程退出，进程等待所有子线程执行完毕后才结束

'''

import time


def say_sorry():
    print('sorry')
    time.sleep(0.5)


if __name__=='__main__':
    for i in range(5):
        say_sorry()


