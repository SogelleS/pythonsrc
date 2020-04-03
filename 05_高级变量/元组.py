name=('aaa', 'bbb', 'ccc',111,222,333.333)
name_l=['aaa', 'bbb', 'ccc']
#使用小括号，不能修改，也能保存不同类型的数据 索引元组
#也要使用[]

empty_tuple=()
single_tuple=(5)            #是整数不是一个元组
real_single_tuple=(5,)      #单元素元组

print(type(name))
print(type(name_l))
print(type(single_tuple))
print(type(real_single_tuple))

print(name[0])

for chstr in name:

    print(chstr, end=' ')