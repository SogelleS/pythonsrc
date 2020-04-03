class A:
    def __init__(self):
        self.num1 = 10
        self.__num2 = 100

    def __test(self):
        print('私有方法%d %d' % (self.num1, self.__num2))

        # 在外界不能访问或调用私有方法和私有属性
    def test(self):

        print('父类的公有方法私有属性%d' % self.__num2)

        self.__test()


class B(A):

    def demo(self):

        # 子类的方法中不能访问父类的私有属性
        # print('__num2=%d' % self.__num2)

        # 子类的方法中不能调用父类的私有方法
        # super.__test()

        # 访问共有属性
        print('子类方法%d' % self.num1)

        # 访问共有方法
        self.test()
        # 共有属性可以调用父类的私有方法和私有属性

        pass


b = B()
b.demo()




