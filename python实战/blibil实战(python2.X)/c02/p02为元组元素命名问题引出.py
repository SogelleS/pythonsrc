
# 使用元组储存数据占用内存小灵活

student = ('Jim', '18', '1140880507')
student2 = ('Lucy', '17', '470571449')

# name
print(student[0])

# age
if student[1] >= 17:
    print(student[1])
    # ...

# qq
print(student[2])

# 索引值不方便维护
# c语言可以使用define 预处理定义或者enum类型







