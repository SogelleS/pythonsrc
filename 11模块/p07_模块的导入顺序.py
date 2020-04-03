import random

while True:
    rand = random.randint(0,10)
    print(rand)
    if rand == 2:
        break
print(random.__file__)

# python会先在当前工作目录寻找模块
# 如果没有才会在系统目录下寻找模块
# 使用 __file 可以查看模块目录


