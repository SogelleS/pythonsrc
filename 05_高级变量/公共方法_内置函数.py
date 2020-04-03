str1='123456789abc'
str2=[1,2,3,4,5,6]
dec1={
    "aaa":1,
    'bbb':2,
    'ccc':3
}

print(len(str1))

del (str2[2])   #可以是关键字也可以是函数
print(str2)

print(max(str1))
print(max(str2))

print(min(str1))
print(min(str2))

print(max(dec1))    #字典只比较名片
print(min(dec1))