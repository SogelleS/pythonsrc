"""
threading.enumerate()
获取当前的活跃的线程对象列表
可以使用len()查看个数

print(threading.current_thread())
打印调用这个方法的的线程对象

"""

import time
import threading


def sing():
    print('sing------>')
    #time.sleep(0.5)


def dance():
    print('dance----->')
    #time.sleep(0.5)


if __name__ == '__main__':
    print(threading.current_thread())
    # 打印调用这个方法的的线程对象

    print('线程数量:%d' % len(threading.enumerate()))

    A = threading.Thread(target=sing)
    B = threading.Thread(target=dance)
    A.start()
    B.start()
    print('线程数量:%d' % len(threading.enumerate()))
    print(threading.enumerate())
