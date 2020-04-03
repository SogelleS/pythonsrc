name_list=['zhangsan','lisi','wangwu']

print(name_list)

#取值
print(name_list[0])

#取索引
print(name_list.index('lisi'))

#修改
name_list[1]='newlisi'
print(name_list)

#添加
#append
name_list.append('dog')
print(name_list)
#insert
name_list.insert(0,'first')
print(name_list)
#extend
tempList=['nt','sb','nmsl']
name_list.extend(tempList)
print(name_list)

#删除.pop.remove.clear

name_list.remove('nt')
print(name_list)

name_list.pop()
print(name_list)

name_list.pop(2)
print(name_list)

name_list.clear()
print(name_list)