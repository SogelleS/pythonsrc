import re

msg = 'da骄傲地i啊今晚isdada1231'
patt = re.compile('da')     # 'da'为正则表达式
res = patt.match(msg)
# 没有匹配会返回空
# 必须从开头匹配,匹配不成功返回None

print(res)

res = re.match('da', '骄傲地i啊今晚isdada1231')
# 第一个为正则，第二个为字符串

print(res)

res = re.search('sas','骄傲地i啊今晚isasdad1231')


print(res)
print(res.span())
# 返回位置

print(res.group())
# 使用group提取匹配到的内容


msg = 'abc 7jhd7as 8as we4w'
# 想从msg提取里面 字母+数字+字母的内容
res = re.search('[a-z][0-9][a-z]',msg)

print(res.group())


