# 使用print 输出对象变量时会得到这样的输出
# <__main__.Cat object at 0x0000028940768400>
#           对象的类        内存位置
#
# 如果希望修改print的打印内容可以修改__str__方法(必须返回一个字符串)

class Cat:

    def __init__(self,name):
        self.name=name
        print('%s coming'%name)

    def __del__(self):
        print('i am gone')

    def __str__(self):
        return 'i am a cat'+self.name


tom=Cat("TOM")

print(tom)















