# coding=gbk
# 本身脚本时utf-8的编码要求用gbk解释
# python3 内置会将utf-8转换为Unicode
# 字符串是以unicode在内存中储存

s = '小甲'
s2 = s.encode('utf-8')
with open('test.tpad','w',encoding='utf-8') as file:
    file.write(s)

