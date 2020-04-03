student = ('Jim', 18, '1140880507')
student2 = ('Lucy', 17, '470571449')


##################第一种解决方案##########################
print('#'*50)

NAME = 0
AGE = 1
QQ = 2

# NAME, AGE, QQ = range(3)

# name
print(student[NAME])

# age
if student[AGE] >= 17:
    print(student[AGE])
    # ...

# qq
print(student[QQ])
print('#'*50)
##################第二种方案##########################

from collections import namedtuple
Stu = namedtuple('Student', ['name', 'age', 'qq'])

s = Stu('Jim', 18, '1140880507')
s2 = Stu(name='Alex', age=17, qq='470571749')
# 可以使用位置传参或者关键字传参

print(s, s2, sep='\n')

print(s.name, s2.name,sep='\t')

print(s[0], s2[0])

print('#'*50)
