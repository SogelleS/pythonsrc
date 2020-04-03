"""
在线程中传递参数有三种方法
1.使用元组传递
tmp = threading.Thread(target=XXXX, args=(x,...))
# 与参数顺序一致

2.使用字典传递
tmp = threading.Thread(target=XXXX, kwargs={'参数名'： 参数值,...})

3.混合使用元组与字典
tmp = threading.Thread(target=XXXX, args=(x,...), kwargs={'参数名'： 参数值,...})
有顺序的传递

"""

import time
import threading


def sing(a, b, c):
    print('参数:', (a, b, c))
    print('sing')
    time.sleep(0.5)


def dance(a, b):
    print('参数:', (a, b))
    print('dance')
    time.sleep(0.5)


if __name__ == '__main__':
    for i in range(5):
        A = threading.Thread(target=sing, \
                             args=(10, 100, 1000))
        B = threading.Thread(target=dance, \
                             kwargs={'a': 10, 'b': 100})
        c = threading.Thread(target=dance, args=(10,), kwargs={'b': 999})


        A.start()
        B.start()
        c.start()
