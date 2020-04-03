def test(num):
    print('adress a(%d) in testfun'%(num), id(num))

    result='hello'
    print('result ad is',id(result))
    return result
#传递参数和返回值是通过引用传递的


a=10

print('adress a(%d):'%a,id(a))

ret=test(a)
print('ad(',ret,')is',id(ret))