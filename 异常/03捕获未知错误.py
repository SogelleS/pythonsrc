# 用8除num后输出结果

try:
    num = int(input('enter a int: '))
    res = 8 / num

# except ZeroDivisionError:
#     print('div by 0')

except ValueError:
    print('must be number')

except Exception as ress:
    print('unknow err %s' % ress)



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
# except Exception as XXXX:    # (xxx为变量名)
#     未知错误
