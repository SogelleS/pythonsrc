str1='\thello world\n\ti love you \n\t\tdong'

print(str1)

list1=str1.split()          #字符串拆分
print(list1)

str2='  '.join(list1)       #字符串合并
print(str2)