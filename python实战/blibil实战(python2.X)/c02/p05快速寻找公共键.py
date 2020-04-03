from random import randint,sample


dic = {x:randint(1,4) for x in sample('abcdefg',randint(3,6))}
dic2 = {x:randint(1,4) for x in sample('abcdefg',randint(3,6))}
dic3 = {x:randint(1,4) for x in sample('abcdefg',randint(3,6))}
print(dic,dic2,dic3,sep='\n')

# 方法一
res = []
for i in dic:
    if i in dic2 and i in dic3:
        res.append(i)

print(res)

#方法二




