class Cat:

    def __init__(self):
        print('初始化')
        self.name='Tom'

        #在init方法内部使用self.属性名=xxx 可以初始化一个属性

    def eatfish(self):

        print('%s eat fish'%self.name)


tom=Cat()
print(tom.name)

tom.eatfish()