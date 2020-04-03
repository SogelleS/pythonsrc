class Tool(object):

    count=0

    @classmethod
    def printnum(cls):
        print('use %d'% (cls.count))

    # @classmethod
    # def XXXX(cls):
    # 定义一个类方法
    # 类方法可以用cls.count直接调用类属性
    # cls与self类似在外部调用时不用传入


    def __init__(self,name):

        self.name=name
        Tool.count += 1



ft=Tool('futou')
cz=Tool('chuizi')
daozi=Tool('daozi')


print(Tool.count)
Tool.printnum()