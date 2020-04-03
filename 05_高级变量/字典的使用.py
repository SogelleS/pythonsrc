xiaoming = {
    "name":"xiao ming",
    "age":18,
    "weight":75.5
    }

#增 删 改 查

print(xiaoming)

#取值
print(xiaoming['name']) #用中括号跟key（key当index用）

#增加与修改
#如果key存在会新增加否则修改

xiaoming['tall']=175
print(xiaoming)

xiaoming['age']=20
print(xiaoming['age'])

#删除

xiaoming.pop('name')
print(xiaoming)