class Cat:

    def __init__(self,name):
        self.name=name
        print('%s coming'%name)

    def __del__(self):
        print('i am gone')


tom=Cat("TOM")

print(tom.name)
print(tom)

del tom

# 使用del会从内存中删除tom导致提前调用__del__方法

print('-'*50)       # 如果没有del tom ,i am gone 会在最后输出


