xiaoming = {
    "name":"xiao ming",
    "age":18,
    "weight":75.5
    }

temp = { "height":175}

#统计键值对数量

print(len(xiaoming))


#合并字典
#键冲突会使用新的值

xiaoming.update(temp)
print(xiaoming)

#清空字典

xiaoming.clear()
print(xiaoming)