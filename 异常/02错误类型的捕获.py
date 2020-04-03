# 用8除num后输出结果

try:
    num = int(input('enter a int: '))
    res = 8 / num
except ZeroDivisionError:
    print('div by 0')
    res = 'ERROR'
except ValueError:
    print('must be number')
    res = 'ERROR'

print(res)

# num不能为0，或者字母

# try的语法格式
#
# try:
#     code.....
#     pass
# except 错误类型:
#     code.....
#     pass
# except (错误类型1,错误类型2)
#     code....
#     pass
# except Exception as res:
#     未知错误
