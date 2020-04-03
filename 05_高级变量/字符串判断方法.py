spaceStr='   '
unspace='  1'

print(spaceStr.isspace())
print("\n\t\r".isspace())

numStr='1'
print(numStr)
print(numStr.isdecimal())   #单纯判断数字
print(numStr.isdigit())
print(numStr.isnumeric())

numStr2='2.2'
                            #这三个不能判断小数
print(numStr2)
print(numStr2.isdecimal())
print(numStr2.isdigit())
print(numStr2.isnumeric())

numStr3 = "\u00b2"          #numStr3="(1)"
print(numStr3)
print(numStr3.isdecimal())
print(numStr3.isdigit())    #可以检测unicode的数字
print(numStr3.isnumeric())  #可以检测unicode的数字

numStr4='一千零一'
print(numStr4)
print(numStr4.isdecimal())
print(numStr4.isdigit())
print(numStr4.isnumeric())  #可以检测中文