"""
进程间是不能共享全局变量的
子进程对全局变量的访问实际上
是对资源的复制


"""


import multiprocessing,time
g_a = 10

def work1():
    print('---------work1---------')
    global g_a
    for i in range(10):
        g_a += 1
    print(g_a)
    print('---------work1---------')


def work2():
    print('---------work2---------')
    print(g_a)
    print('---------work2---------')


if __name__ == '__main__':


    pt1 = multiprocessing.Process(target=work1)
    pt2 = multiprocessing.Process(target=work2)

    pt1.start()
    pt2.start()
    time.sleep(0.5)

    print('in main',g_a)




