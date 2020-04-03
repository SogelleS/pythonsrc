'''
例1 找出一个随机序列出现频率
最高的三个元素，与出现的次数

'''
from random import randint

# 生成一个随机列表
data = [randint(0, 5) \
        for x in range(30)]

print(data)

# 最后统计的应该是一个字典
# dic = {1:X, 2:X, ...}

c = dict.fromkeys(data, 0)
# 创建一个key为data元素，值为0的字典


for x in data:
    c[x] += 1
# 遍历data
print(c)
# cmax = 0
# cmaxk =0
# for x in list(c):
#     if c[x] > cmax:
#         cmax = c[x]
#         cmaxk = x
#
# nc = [x for x in list(c) if x != cmaxk]
#
# cmax2 = 0
# for x in nc:
#     if c[x] > cmax2:
#         cmax2 = c[x]
# print(cmax)
# print(cmax2)

# cmax = [(k, v) for k, v in c.items() if v > 5]
# print(cmax)
# 使用字典解析

# 直接使用counter

from collections import Counter

c2 = Counter(data)
print(c2.most_common(3))
# 打印出现频率最高的元素 元组

