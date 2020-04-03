"""
cpu处理多线程时不是同时进行的
且运行速度不同
可能cpu在线程1在切换到线程2之前还没有对线程1累加
在线程2完成累加后又跳回到线程1再对线程1累加
累加的次数依然时200w次但是数变小了不是200w
共享全局变量造成了资源竞争的问题


"""
import threading

num = 0


def work1():
    global num
    for i in range(10000000):
        num += 1
    print('In work1 ', num)


def work2():
    global num
    for i in range(10000000):
        num += 1
    print('In work2 ', num)


if __name__ == '__main__':

    t1 = threading.Thread(target=work1)
    t2 = threading.Thread(target=work2)

    t1.start()
    t1.join()
    # 优先让t1执行
    # 违背了多线程的初衷，不推荐

    t2.start()

    while True:
        if len(threading.enumerate()) == 1:
            break

    print('main--------->', num)
