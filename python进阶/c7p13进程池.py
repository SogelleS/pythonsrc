"""
1 创建一个函数模拟文件拷贝
2 创建一个进程池长度3(最多容纳三个进程)
3 先用进程池同步方式拷贝文件
4 再用异步方式

异步方式注意问题
先用.close()表示不再接受新任务
且使用异步方法主进程不会等待进程池结束后退出
可以使用pool.join()堵塞主进程

"""
import time,multiprocessing


def copyDome():
    print('copying......')
    print(multiprocessing.current_process())
    print('---'*20)
    time.sleep(0.1)

if __name__ == '__main__':

    # 进程单线程
    #for i in range(10):
    #    copyDome()
    # 创建进程池
    queinp = multiprocessing.Manager().Queue()
    que = multiprocessing.Queue()

    pool = multiprocessing.Pool(3)

    # 同步方式
    # 一个进程进行完后再进行第二个
    # pool.apply(函数名,(函数参数,......))
    #for i in range(10):
    #    pool.apply(copyDome)

    # 异步方式
    # 进程池最大进程数一起进行
    for i in range(15):
        pool.apply_async(copyDome)
    pool.close()
    pool.join()
