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

    pool = mp.Pool(2)
    # 创建进程池中的队列
    poolqueue = mp.Manager().Queue(5)

    # 同步方式
    print('--------同步--------')
    pool.apply(write,(poolqueue,))
    pool.apply(read,(poolqueue,))

    # 异步方式
    print('--------异步--------')
    resurt = pool.apply_async(write,(poolqueue,))
    resurt.wait()
    pool.apply_async(read,(poolqueue,))
    '''
    方法返回一个对象ApplyResult
    对象中有一个wait方法类似join方法
    '''

    # 不再接受新任务
    pool.close()
    # 堵塞主进程
    pool.join()

