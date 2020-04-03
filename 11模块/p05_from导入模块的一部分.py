from P01_测试模块1 import Dog
from P02_测试模块2 import Cat as kitty
from P02_测试模块2 import say_hello
from P01_测试模块1 import say_hello as say_dog

dog = Dog
kit = kitty
print(dog)
print(kit)
say_hello()
say_dog()


# form 模块 impor 工具
# 导入后可以直接使用不需要模块名.来调用
# 可以导入的工具 全局变量，函数，类
# 如果两个模块存在同名函数，后导入的会覆盖先导入的
# 如果命名冲突可以使用as定义一个别名
