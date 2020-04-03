from random import randint
import timeit


def check(list):    # 通用方法
    res = []

    for i in list:
        if i <= 0:
            res.append(i)
    return res


a = [randint(-10, 10) for i in range(0, 10)]
print('a =', a)
# 使用列表解析List Comprehensions创建随机列表
# 也可以使用列表解析来筛选

b = [i for i in a if i >= 0]
print(b)

# print(timeit.timeit(stmt='[i for i in a if i >= 0]',number=100))

b = filter(lambda x: x >= 0, a)
print(list(b))

# lambda 为匿名函数 冒号前为参数，后为返回值
# 列表解析比使用匿名函数更快

print(check(a))


dic = {x: randint(0, 100) for x in range(1,21)}
print(dic)
# 使用字典解析生成字典

dic2 = {i: v for i, v in dic.items() if v < 60}
print(dic2)
# .items 返回一个迭代器
# 字典使用迭代器会返回元组
# 使用字典解析筛选

# 集合解析

a2 = set(a)
print(a2)
# 转换集合
a2 = {x for x in a2 if x <= 0}
print(a2)

