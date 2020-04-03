class Cat:

    # def __init__(self):
    #     self.name=input('enter name:')
    #     #一种设置的方法

    def __init__(self,name='Tom'):      #默认tom

        self.name=name

    def eatfish(self):

        print('%s eat fish'%self.name)


tom=Cat('Tom')
tom2=Cat('Tom2')
tom3=Cat()

print(tom.name)
print(tom2.name)
print(tom3.name)

tom.eatfish()