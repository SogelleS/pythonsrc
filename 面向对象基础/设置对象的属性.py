class Cat:

    def eatf(self):
        print('%s eat fish'%self.name)

    #那个对象调用的方法self就是那个对象的引用
    def drink(self):
        print('cat must drink')



tom = Cat()
lazy=Cat()
tom.name='TOM'
lazy.name="LAZY"
tom.drink()
tom.eatf()

#可是使用 .属性名 创建属性


input()