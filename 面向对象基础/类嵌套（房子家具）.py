class HouseItem:

    def __init__(self,name,area):
        self.name=name
        self.area=area

    def __str__(self):

        return '%s 占地 %.2f'%(self.name,self.area)

class House:
    def __init__(self, type, area):
        self.area=area
        self.type=type

        self.free=area
        self.itemlist=[]

    def __str__(self):

        return ('housetype[%-5s][%.2f]free area is %.2f list=%s'
                % (self.type,self.area, self.free, self.itemlist))

    def addItem(self,item):

        if self.free<item.area:
            print('cat add item %s'%item.name)

        else:
            print('添加了[%-10s]占地%.2f'%(item.name,item.area))
            self.itemlist.append(item.name)
            self.free-=item.area


bad = HouseItem('ximengsi', 4)
cheat = HouseItem('yigui', 2)
table = HouseItem('canzhuo', 1.5)
shit = HouseItem('shit',100)


my_home = House('1', 60)

my_home.addItem(bad)
my_home.addItem(cheat)
my_home.addItem(table)
my_home.addItem(shit)

print(my_home)




















