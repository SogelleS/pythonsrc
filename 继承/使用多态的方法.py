class Dog:
    def __init__(self,name):
        self.name=name

    def play(self):
        print('dog[%s] is playing'%self.name)


class XT(Dog):

    def play(self):
        print('i can fly')
        super().play()

class Person:

    def __init__(self,name):
        self.name=name

    def play_with_dog(self, dog):

        print('%s play with %s'% (self.name, dog.name))
        dog.play()


xm=Person('XM')
wc=XT('XTwangcai')

xm.play_with_dog(wc)




