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

子线程创建步骤
1. 导入threading 模块
2. 使用threading.Thread() 创建子进程对象
传递的参数 target=函数名


3. 指定子线程执行的分支
4. 启动子线程 对象.start()

进程程会在所有子线程结束后再结束
进程与线程不一样
主线程退出，进程等待所有子线程执行完毕后才结束

'''

import time
import threading


def say_sorry():
    print('sorry')
    time.sleep(0.5)


if __name__=='__main__':
    for i in range(5):
        th_ob = threading.Thread(target=say_sorry)
        th_ob.start()

print('xxxxxx')