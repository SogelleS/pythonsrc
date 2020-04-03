def demo1():
    return int(input('enter a int: '))


def demo2():
    return demo1()



try:
    print(demo2())

# except ValueError:
#     print('error')

except Exception as err:
    print('Error:[%s]' % err)

# 异常传递给调用的一方
# 利用异常的传递性可以在主程序捕获










