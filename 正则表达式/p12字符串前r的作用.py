"""
正则字符串前加r表示\不再具有转义的作用

\.由于时没有转义直接传入正则所以正则模块依然会转义

注意 要是不用r
使用正则匹配带有\的字符串要用 \\\\ 四个反斜杠
第一次处理字符串时处理成\\两个反斜杠传入正则模块
正则模块对\\转义成一个\
注意 字符串的结尾不能用奇数个\ 解释器会认为你在转义字符串结束符


"""

import re

str = '<html><h1>test</h1></html>'

a = re.match('<([a-zA-Z0-9]+)><([a-zA-Z0-9]+)>(.*)<(/\\2)><(/\\1)>',str)
b = re.match(r'<([a-zA-Z0-9]+)><([a-zA-Z0-9]+)>(.*)<(/\2)><(/\1)>',str)

c = re.match(r'a\'+','a\'')
d = re.match('aa\\\\','aa\\')
e = re.match(r'aa\\', 'aa\\')
f = re.match('a\'+', 'a\'dddd')
g = re.match('a.+', 'a..s...')


print(a.group())
print(b.group())
print(c.group())
print(d.group())
print(e.group())
print(f.group())
print(g.group())


