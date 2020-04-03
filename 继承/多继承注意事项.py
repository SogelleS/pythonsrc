class A:

    def test(self):
        print('A test')

    def demo(self):
        print('A demo')


class B:

    def demo(self):
        print('B demo')

    def test(self):
        print('B test')


'''
应尽量避免父类中方法重名
MRO methor resolution order

类存在一个内置属性__mro__
有调用顺序的元组
(<class '__main__.C'>, <class '__main__.A'>, 
<class '__main__.B'>, <class 'object'>)

'''


class C(A, B):

    pass

class D(B, A):

    pass


c = C()
d = D()

c.test()
c.demo()
d.test()
d.demo()
print('*'*50)
print(C.__mro__)

