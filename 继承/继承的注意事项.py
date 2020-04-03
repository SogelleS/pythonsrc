class ani:

    def eat(self):

        print('eat')

    def drink(self):

        print('drink')

    def run(self):

        print('run')

    def sleep(self):

        print('sleep')


# 使用继承的写法
class Dog(ani):

    def bark(self):

        print('bark!!!')


class Xiaotian(Dog):
    # 父类的属性会一直传递
    def fly(self):
        print('i can fly')


class Cat(ani):

    def catch(self):
        print('抓老鼠')


xtq=Xiaotian()

# 对象不能调用类里没有的方法如猫类里的catch方法
# xtq.catch()

