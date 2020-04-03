class person:

    def __init__(self, name, weight):

        self.name=name
        self.weight=weight

    def __str__(self):

        return '我叫%s体重是%.2fKG'%(self.name,self.weight)

    def run(self):

        print('%s is runing'%self.name)
        self.weight-=0.5


    def eat(self):

        print('%s is eating'%self.name)
        self.weight+=1




ming=person('ming',75.0)
mei=person('mei',45.0)

print(ming)
print(mei)

ming.run()
mei.run()
ming.eat()
mei.eat()

print(ming)
print(mei)
# ming和mei 的属性不会互相影响


