"""
在多线程应用中
如果多个线程各占有资源的一部分并且同时等待对方的资源（或者等待环：类似十字路口）
就会造成死锁，应用会停止响应

下面是一个简单的列子

"""

import threading


def getv(index):
    data = [x for x in range(1,11) if x % 2]
    lock1.acquire()
    if index >= len(data):
        print('下标越界',index)

        # 解决死锁
        lock1.release()

        return
    print(data[index])
    lock1.release()

if __name__ == '__main__':

    lock1 = threading.Lock()
    for i in range(10):
        t1 = threading.Thread(target=getv, args=(i, ))
        t1 .start()



