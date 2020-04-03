class Tool(object):

    count=0
    # 使用赋值语句创造一个类属性

    def __init__(self,name):

        self.name=name
        Tool.count += 1
        # 使用 类名.类属性 更改类属性


ft=Tool('futou')
cz=Tool('chuizi')
daozi=Tool('daozi')


print(Tool.count)

# 使用实例名也可以访问类属性
# 对象的属性获取采取向上查找机制
# 首先在对象内部查找属性如果没有
# 会在类定义中查找类属性
# 实例方法可以用类名.xxx来访问类方法
# 不建议使用对象名访问类属性的这种方法
# 会带来下面的问题

ft.count=99
# 为ft对象新建了一个count的新属性，不是类属性

print(ft.count)
print(Tool.count)


