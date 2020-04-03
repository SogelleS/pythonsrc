"""
1 创建2个进程
2 创建1个队列
3 一个进程写队列,另一个读队列
4 使用.join()堵塞程序主进程


"""

import multiprocessing as mp
import time


def write(que):

    for i in range(10):
        if que.full():
            print('队列已满')
            break
        que.put(i)
        print('已写入:',i)
        time.sleep(0.25)


def read(que):

    while True:
        if que.empty():
            print('队列已空')
            break
        val = que.get()
        print('已读取到',val)


if __name__ == '__main__':

    queue = mp.Queue(5)
    mp1 = mp.Process(target=write, args=(queue,))
    mp2 = mp.Process(target=read, args=(queue,))

    mp1.start()
    # 优先写入
    mp1.join()
    mp2.start()

