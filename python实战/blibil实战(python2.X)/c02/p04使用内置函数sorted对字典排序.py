from random import randint

dic = {x:randint(0,100) for x in 'adwrkhdqs'}

print(dic)
print(sorted(dic))
zdic = list(zip(dic.values(),dic.keys()))
print(zdic)
print(sorted(zdic))

print(dic.items())
print(sorted(dic.items(),key=lambda x: x[1]))
