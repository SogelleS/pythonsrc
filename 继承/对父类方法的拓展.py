class ani:

    def eat(self):

        print('eat')

    def drink(self):

        print('drink')

    def run(self):

        print('run')

    def sleep(self):

        print('sleep')


class Dog(ani):

    def bark(self):

        print('bark!!!')


class Xiaotian(Dog):

    def fly(self):
        print('i can fly')

    def bark(self):

        print('哮天犬要叫了......')

        super().bark()
        # 调用父类方法
        # Dog.bark(self) python2.X 的写法 不推荐使用
        # 如果使用递归调用子类的方法要注意递归出口的设置


        print('我是哮天犬')


'''
如果子类方法需要完成父类的方法并且需要增加其他功能
就需要对子类里的方法进行拓展

重新定义一个同名方法
1，针对子类需求编写方法
2，使用super(). 调用父类的方法
3，编写其他子类方法代码

'''

xtq=Xiaotian()

xtq.bark()