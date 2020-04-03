str1='hello world'

print(str1.startswith("he"))    #以he开头检测

print(str1.endswith('ld'))      #以ld结尾检测

print(str1.find('llo'))         #查找索引

print(str1.find('abc'))         #不会报错会返回-1

print(str1.replace("world",'python'))   #返回一个替换过的字符串

print(str1)

str1=str1.replace("world","python")

print(str1)