"""
创建一个自定义线程类

1.让自定义类继承 threading.Thread 类
2.重写父类（threading.Thread）的 run 方法
3.创建子类对象，调用.start()方法启动线程

def start(self):
    self.run()
    ......
start 方法内部一定调用了run方法

可以查看run方法的实现其实就是子线程调用的函数
对这个方法重写后如果不在内部实现对父类run的调用，那么不会执行target的函数
有run的实现可知，run只能调用一次
推测__init__方法会在内部调用run方法(X)
是我在target=demo1() 后面加了括号导致的

"""
import threading
from time import sleep


class Myth(threading.Thread):

    # 重写__init__方法时要用super().__init__来调用父类方法
    def __init__(self,num,target=None):
        super().__init__(target=target)
        self.num = num

    # 重写run方法
    def run(self) -> None:
        super().run()

        # for i in range(5):
        for i in range(self.num):
            print('working......(.run)', self.name)
            sleep(0.5)


def demo1():
    print('demo1...')


if __name__ == '__main__':
    # a = Myth(num=10)
    # a = Myth()
    a = Myth(num=3, target=demo1)
    a.start()


