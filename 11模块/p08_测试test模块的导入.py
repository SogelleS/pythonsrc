print('$'*50)

import p08_test模块 as Test
# 导入函数，类，全局变量（工具）
# 模块中没有缩进的代码会执行一遍
# 导入的直接执行的代码不是工具且不需要执行

print('$'*50)
Test.hello()
print(Test.__name__)
print(Test.__file__)
