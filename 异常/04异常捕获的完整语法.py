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
#     print('unknow Error %s' % XXXX)
#     pass
# else:
# 没有异常才会执行的代码
#   pass
# finally:
# 无论是否有异常都会执行的代码
#   pass


try:
    num = int(input('enter a int: '))
    res = 8 / num

# except ZeroDivisionError:
#     print('div by 0')

except ValueError:
    print('must be number')

except Exception as ress:
    print('unknow err %s' % ress)
else:
    print('good no error')
    pass
finally:
    print('i must run')
    pass

print('+'*50)