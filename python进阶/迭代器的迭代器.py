
class test(object):
    def __init__(self):
        self.list = []

    def __iter__(self):
        re = MyIterIter(self.list)
        return re

    def additem(self,name):
        self.list.append(name)


class MyList(object):
    def __init__(self):
        self.data = []

    def __iter__(self):
        # 返回一个迭代器
        my_iter = MyIter(self.data)
        return my_iter

    def additem(self,thing):
        self.data.append(thing)
        # print(self.data)


class MyIter(object):
    def __init__(self,mylist):
        self.list_len = len(mylist)
        self.list = mylist
        self.local_index = 0

    def __iter__(self):
        iteriter = MyIterIter(self.list[self.local_index])

        return iteriter
    def __next__(self):
        # 判断是否越界 越界抛出异常
        if self.local_index < self.list_len:
            
            # 根据下标获取值
            data = self.list[self.local_index]

            # 下标位置加一
            self.local_index += 1
        else:
            raise StopIteration
            # 抛出停止迭代异常
        
        
        # 返回下标数据
        return data


class MyIterIter(object):
    def __init__(self, item):
        self.item = item
        self.len = len(item)
        self.index = 0

    def __next__(self):

        if self.index < self.len:
            next = self.item[self.index]
            # netx = 1
            self.index += 1

        else:
            raise StopIteration

        return next


mylist = MyList()
item1 = test()
item2 = test()
item3 = test()

item1.additem('hahaha')
item1.additem('yeyeye')
item1.additem('ohohoh')
item1.additem('nonono')

item2.additem('aaaaaa')
item2.additem('bbbbbb')
item2.additem('cccccc')
item2.additem('dddddd')

item3.additem('000000')
item3.additem('111111')
item3.additem('222222')
item3.additem('333333')

mylist.additem(item1)
mylist.additem(item2)
mylist.additem(item3)

em_list = []

for i in mylist:
    print(i)
    em_list.append(iter(i))
    for j in i:
        print(j)


print('\n' + '##' * 20)


mylist2 = MyList()
#
mylist2.additem('hello')
mylist2.additem('world')
mylist2.additem('i')
mylist2.additem('love')
mylist2.additem('you')
#


for i in mylist2:
    print(i)
    for j in i:
        print(j, end=' ')

print('\n' + '##'*20)
print(iter(iter(mylist2)))

a = iter(mylist2)
b = iter(iter(mylist2))


a1 = next(a)
for i in a1:
    print(i)
a2 = next(a)
for i in a2:
    print(i)

print('##'*20)
b = iter(iter(mylist2))

#while True:
    #b1 = next(b)
    #print(b1)

print('##'*20)
a = iter(mylist2)

while True:
    ax = next(a)
    print(ax)