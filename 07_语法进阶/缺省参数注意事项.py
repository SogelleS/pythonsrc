
def printInfo(name,title,sex=True):      #sex缺省为True
                                        #缺省参数后不能跟正常参数
                                        #只能跟缺省参数

    text='boy'
    if not sex:
        text = 'girl'

    print('[%-10s]%s is %s'%(title,name,text))


printInfo('aaa','shit')
printInfo('bbb','shit too',False)
#参数的传递是按顺序的如果title也是一个缺省参数那么
#使用printInfo('bbb',False)这种写法会导致title参数为‘False’
#正确的使用方法是 printInfo('bbb',gender=False)

