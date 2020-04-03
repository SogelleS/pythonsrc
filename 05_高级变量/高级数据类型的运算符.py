list1=[1,2,3,4,5,'aaaa','bbbb','cccc']

tup1=(1,2,3,4,5)

str1='hello world'

dec1={
    'name':'2333',
    'qq':'123123'
}

print(str1+str1)
print(list1+list1)  #与.extend方法不同在+运算创造了一个新的列表而extend是使原列表拓展
print(tup1+tup1)    #append方法是在末尾插入元素可以是列表而extend只会拼接列表

print(str1*5)
print(list1*5)
print(tup1*5)
#print(dec1*5)       #报错子典不能使用*和+运算符

print('aaaa' in list1)
print('lo' in str1)
print(1 in tup1)
print('qq' in dec1)
print('2333' in dec1)   #对字典是针对key
