"""
a = re.match(pattern,string,flags=0)
pattern 正则模型
string  待匹配字符串
flags   匹配模式

匹配成功会返回match对象有以下方法
不成功会返回None

group()     返回被匹配的字符串
start()     返回匹配开始的位置
end()       返回匹配结束的位置
span()      返回元组(匹配开始的位置,匹配结束的位置)


"""

import re
str = 'test dqweq'

a = re.match('test',str)
# 从头开始匹配
b = re.search('test',str)
# 查找匹配
if a:
    print(a.group())
else:
    print('cant match')
    print(a.group())






