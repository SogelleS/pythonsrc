list1=[1,2,3,4,5,'aaaa','bbbb','cccc']

list2=[{"name":'xiaoming',
        'gander':True,
        "height":1.75},
       {"name":'zhangsan',
        'gander':True,
        "height":1.45},
       {"name":'lisi',
        'gander':False,
        "height":1.85}
]

'''

for 变量 in 集合：
    
    代码......
    
else:
    没有通过 break 
    且循环遍历完集合正常结束才会执行

'''

for temp in list1:
    #if temp == 'aaaa':
        #break
    pass

else:
    print('temp is :',temp)

print('done!!! temp is ',temp)

for temp2 in list1:
    if temp2 == 'aaaa':
        break

else:
    print('temp is ',temp2)

print('done!!! temp2 is ',temp2)

find_name='lisi'

for std_dic in list2:
    print(std_dic)
    if std_dic['name']==find_name:
        print('find %s'%find_name)
        break

else:
    print('没找到',find_name)
