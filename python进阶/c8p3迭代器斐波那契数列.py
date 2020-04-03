"""
使用迭代器打印斐波那契数列


1 1 2 3 5 8 13 21 34 ......

a = b

b = a + b

最后输出a所有的值

a       b

1       1
1       2
2       3
3       5
5       8



定义一个迭代器类


实现效果

fib = Iterfib(10)

for i in range(10)
    print(exit(fib))

打印十个

"""


class IterFib(object):

    def __init__(self, max_num):
        self.max_mun = max_num

        self.a = 1

        self.b = 1

        self.index = 1

    def __next__(self):

        if self.index <= self.max_mun:

            if self.index == 1 or self.index == 2:
                re = 1

            else:
                re = self.a + self.b
                self.a, self.b = self.b, re
                # self.a = self.b
                # self.b = re
            self.index += 1

        else:
            raise StopIteration

        return re


class IterFib2(object):

    def __init__(self, max_num):
        self.max_mun = max_num
        self.a = 1
        self.b = 1
        self.index = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.index <= self.max_mun:
            re = self.a

            self.a, self.b = self.b, self.a + self.b
            # 使用元组的方式赋值

            self.index += 1
        else:
            raise StopIteration

        return re


fib = IterFib2(100)

for i in range(20):
    print(next(fib), end=' ')

print('\n'+'##'*20)
fib2 = IterFib2(10)

for i in fib2:
    print(i, end=' ')

