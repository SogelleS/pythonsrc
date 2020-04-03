num = 10


def demo1():

    global num
    num=100        #许修改全局变量
    print(num)


def demo2():

    print(num)



demo1()
demo2()