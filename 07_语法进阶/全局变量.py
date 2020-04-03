num = 10

def demo1():
    print(num)
def demo2():
    global num
    num+=10
    print(num)

# 要在函数中修改全局变量 在前面加global

demo1()
demo2()