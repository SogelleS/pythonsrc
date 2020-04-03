def input_password():

    password = input('enter password: ')
    if len(password) >= 8:
        return password
    else:
        print('发生异常')
        ex = Exception('密码太短')
        raise ex
        # 使用Exception类创建异常对象
        # 使用raise抛出异常对象


try:
    print(input_password())

except Exception as res:
    print(res)
    print(type(res))





