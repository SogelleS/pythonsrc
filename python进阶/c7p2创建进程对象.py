"""
进程模块的使用与线程类似

1导入multiprocessing模块
2创建对象
3启动进程
4


"""

import multiprocessing
import time

def test_fun(num):
    for i in range(num):
        print(i+1, '正在运行fun函数......')
        time.sleep(0.25)


if __name__ == '__main__':
    press_test = multiprocessing.Process(target=test_fun,\
                                         kwargs={"num":11})

    press_test.start()





