"""
进程之间不能共享全局变量
进程之间参数传递同线程一样
args 传递元组
kwargs 传递字典
混合使用


"""

import time,multiprocessing

def workprocess(a,b,c):
    print(a,b,c,sep='\t')

if __name__ == '__main__':
    pa = multiprocessing.Process(\
        target=workprocess,\
        args=('aaa','bbb','ccc'))

    pb = multiprocessing.Process( \
        target=workprocess, \
        kwargs={'a': 'aaa', 'b': 'bbb', 'c':'ccc'})

    pc = multiprocessing.Process( \
        target=workprocess, \
        args=(10,),\
        kwargs={'b':100,'c':1000})

    pa.start()
    pb.start()
    pc.start()
