class A:
    def __init__(self):
        self.num1 = 10
        self.__num2 = 100

    def __test(self):
        print('私有方法' % (self.num1, self.__num2))

        # 在外界不能访问或调用私有方法和私有属性



class B(A):

    def demo(self):

        # 子类的方法中不能访问父类的私有属性
        print('__num2=%d' % self.__num2)


        # 子类的方法中不能调用父类的私有方法
        super.__test()





b = B()
b.demo()
