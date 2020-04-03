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

        print('我是哮天犬')


'''
如果哮天犬的叫声与普通狗叫不同
就需要对哮天犬子类里的bark方法的重写(overrides)

重新定义一个与父类重名的方法即可

'''

xtq=Xiaotian()

xtq.bark()