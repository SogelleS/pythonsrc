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







wangcai=Dog()
wangcai.eat()
wangcai.drink()
wangcai.bark()

print('#'*50)

xioat=Xiaotian()
xioat.eat()
xioat.bark()
xioat.fly()

