"""
python 默认是贪婪模式 有的语言默认是非贪婪

满足正则的情况下总是尝试尽可能多的匹配字符

非贪婪则是尽可能少的匹配字符

切换贪婪与非贪婪模式需要 ?

在+ * ？ {} 后添加?可以变成非贪婪
在可以边长度的符号后加

"""
"""
a123456
a\d+        贪婪匹配    a123456
a\d+        非贪婪      a1

src="https://xxxxxxxxxxx/xxxx/xxxx/xxx.jpg"system="dddaaaa"
src=\".*?\" =========> "https://xxxxxxxxxxx/xxxx/xxxx/xxx.jpg"


"""
import re
str = 'a123456'
str2 = 'aa123aaaa12345'
src='src="https://xxxxxxxxxxx/xxxx/xxxx/xxx.jpg"system="dddaaaa"'

res = re.match('a\d+',str)
res2 = re.match('a(\d+?)',str)
res3 = re.match('a(\d+)?',str)
# 可以没有括号注意括号位置
res4 = re.match('aa.*?\d+',str2)
res6 = re.search('\".*?\"',src)
res5 = re.search('\".*\"',src)

print(res.group())
print(res2.group())
print(res3.group())
print(res4.group())
print(res5.group())
print(res6.group())

