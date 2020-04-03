

#　创建一个生成器
def fibyield(maxnum):
    a = 1
    b = 1
    local = 1
    print('-------while外--------')
    # 第二次运行到这个函数时会直接从while循环开始因为while语句还没运行完
    while local < maxnum:
        print('-------while内-------%d' % local)
        data = a
        # 在a改变之前保存a的值

        a = b
        b = a + b
        local += 1
        print('-------while结束-----%d' % local)
        yield data
        print('-------yield外-------%d' % local)


if __name__ == '__main__':
    fib = fibyield(3)

    for i in range(5):
        a = next(fib)
        print(a)


