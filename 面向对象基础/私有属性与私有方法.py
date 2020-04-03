class woman:

    def __init__(self,name,age=18):

        self.name=name
        self.__age=age

    def unsecert(self):
        # 对象的方法内部可以访问私有属性
        print('%s age is %d'%(self.name,self.__age))

    def __secert(self):
        # 外部不能访问私有方法
        print('%s age is %d'%(self.name,self.__age))


xf=woman("xiaofang",20)

# print(xf.__age)
# 私有属性在外界不允许访问

xf.unsecert()

# 访问私有方法的方法 xf._类名私有方法名
xf._woman__secert()
print(xf._woman__age)




