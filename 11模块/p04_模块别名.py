import P01_测试模块1 as Mou1
import P02_测试模块2 as Mou2

# 使用as为模块定义别名
# 别名应满足大驼峰命名法

Mou1.say_hello()
Mou2.say_hello()

dog = Mou1.Dog()
cat = Mou2.Cat()