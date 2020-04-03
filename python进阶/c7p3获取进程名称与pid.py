"""
使用进程对象的multiprocessing.current_process()
获取当前进程对象,对进程对象使用.pid方法
可以获得进程pid
或者使用os模块获取
os.getpid()
os.getppid()可以获取父id

创建进程对象时使用name参数可以不使用默认进程名
使用自定义进程名

可以在终端或者任务管理器里kill进程



"""

import multiprocessing
import time,os

def test_fun(num):
    for i in range(num):
        print(i+1, '正在运行fun函数()......')
        #print(multiprocessing.current_process())
        #print(multiprocessing.current_process().pid)
        print(os.getpid())
        print(os.getppid())

        #time.sleep(0.25)
        time.sleep(5)
    time.sleep(10)


if __name__ == '__main__':
    #print(multiprocessing.current_process())
    #print(multiprocessing.current_process().pid)
    print(os.getpid())
    print(os.getppid())
    press_test = multiprocessing.Process(target=test_fun,\
                                         kwargs={"num":11},\
                                         name='haha')

    press_test.start()

    # 获取主进程名称


