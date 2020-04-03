def sumNumber(*args):

    num=0
    print(args)
    for number in args:
        num+=number
    return num

resu=sumNumber(10,20,30,40)
print(resu)