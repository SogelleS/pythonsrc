class Cat:

    def eatf(self):
        print('cat eat fish')

    def drink(self):
        print('cat must drink')



tom = Cat()
print(tom)
print('%x'%id(tom))
print(id(tom))


tom.drink()
tom.eatf()

lazy=Cat()
lazy2=lazy
lazy.eatf()
lazy.drink()
print(lazy)
print(lazy2)
#lazy 与 tom 不是一个对象 但是lazy2与lazy是一个对象


