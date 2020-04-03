"""
.search
会在字符串内查找模式匹配返回第一个匹配字符串，没有则返回None
与match不同在于match会从头开始查找
格式同match

.findall
搜索全部，返回一个列表
格式同match

.sub
字符串替换方法
按照正则查找替换为指定内容
re.sub(表达式,新内容,要替换的字符串)返回替换后的字符串

.split
字符串拆分方法
按照正则匹配的位置拆分字符串
返回一个列表



"""
import re

res = re.search('heh','rhelheheh@163.com')

res2 = re.search('[1-9]\\d*','次数a:9449 timesb:545 timesc:1466')

res3 = re.findall('[1-9]\\d*','次数a:9449 timesb:545 timesc:1466')

res4 = re.findall('heh','rhelheheh@163.com')

res5 = re.sub('[1-9]\\d*','1000000','次数a:9449 timesb:545 timesc:1466')

print(res.group())
print(res2.group())
print(res3)
print(res5)

# 使用sub方法
with open('test.txt','r') as filep:
    with open('test2.txt','w') as tfile:
        while True:
            fileline = filep.read()
            if fileline:
                fileline = re.sub('<[^>]*>| |\n','',fileline)
                tfile.write(fileline)
                print(fileline)
            else:
                break

# 使用split拆分字符串

str = 'hello world,ilove.you(python)haha'

res6 = re.split(' |,|\.|[(]|[)]', str)
print(res6)