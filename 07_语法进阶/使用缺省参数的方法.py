
def printInfo(name, sex=True):      #sex缺省为True

    text='boy'
    if not sex:
        text = 'girl'

    print('%s is %s'%(name,text))


printInfo('aaa')
printInfo('bbb',False)

