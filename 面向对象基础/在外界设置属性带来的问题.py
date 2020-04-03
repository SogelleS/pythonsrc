class Cat:

    def eatf(self):
        print('%s eat fish'%self.name)

    def drink(self):
        print('cat must drink')


tom = Cat()
# tom.name='TOM'
tom.eatf()
tom.name='TOM'
#name属性在调用之后会报错


input()