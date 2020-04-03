"""


同步与异步
在多任务中任务的执行有先后顺序一个执行完毕再执行下一个任务
异步 多任务同时执行

如果应用了线程锁那么当一个线程访问资源时
其他的线程不能访问这些资源，当不需要访问后再接锁

当多个线程几乎同时修改某一个共享数据是，需要进行同步控制
最简单的同步控制就是引入互斥锁
互斥锁为资源引入 锁定/非锁定 的状态

    创建互斥锁的方法
    创建锁
    XXX = threading.Lock()
    锁定(使用前先锁定，用完后再解锁)
    XXX.acquire()
    释放
    XXX.release()



"""
import threading
from time import sleep

num = 0


def work1():
    global num
    for i in range(100000):
        # 上锁
        lock1.acquire()
        num += 1
        lock1.release()
    print('In work1 ', num)


def work2():
    global num
    for i in range(100000):
        # 同一把锁
        lock1.acquire()
        num += 1
        lock1.release()
    print('In work2 ', num)


if __name__ == '__main__':

    # 创建一把互斥锁(外部)
    lock1 = threading.Lock()

    t1 = threading.Thread(target=work1)
    t2 = threading.Thread(target=work2)

    t1.start()
    t2.start()

    while True:
        if len(threading.enumerate()) == 1:
            break

    print('main--------->', num)