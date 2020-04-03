#函数不能直接修改全局变量

num = 10


def demo1():

    num=100         #不允许修改全局变量,只会定义一个新的局部变量
    print(num)


def demo2():

    print(num)



demo1()
demo2()

